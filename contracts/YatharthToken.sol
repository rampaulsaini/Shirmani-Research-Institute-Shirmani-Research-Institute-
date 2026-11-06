// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

// Source-only test artifact. Pin OpenZeppelin Contracts v5 before compiling.
// This contract is NOT deployed, audited, activated, or connected to a public chain.
import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {ERC20Capped} from "@openzeppelin/contracts/token/ERC20/extensions/ERC20Capped.sol";
import {AccessControl} from "@openzeppelin/contracts/access/AccessControl.sol";
import {Pausable} from "@openzeppelin/contracts/utils/Pausable.sol";

/// @notice YTH v0.1 capped token scaffold. Minting is disabled at construction.
contract YatharthToken is ERC20, ERC20Capped, AccessControl, Pausable {
    uint256 public constant MAX_SUPPLY = 100_000 * 10 ** 18;

    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");

    bool public mintingEnabled; // defaults to false
    mapping(bytes32 => bool) public usedEvidenceIds;

    event MintingStatusChanged(bool enabled, address indexed governance);
    event VerifiedContributionMint(
        address indexed recipient,
        uint256 amount,
        bytes32 indexed evidenceId,
        address indexed authorizedMinter
    );

    error ZeroGovernanceAddress();
    error GovernanceMustBeContract();
    error MintingDisabled();
    error InvalidRecipient();
    error InvalidAmount();
    error EmptyEvidenceId();
    error EvidenceAlreadyUsed(bytes32 evidenceId);

    /// @param governanceMultisig A deployed governance contract; independently verify its threshold and signer separation before use.
    constructor(address governanceMultisig)
        ERC20("Yatharth", "YTH")
        ERC20Capped(MAX_SUPPLY)
    {
        if (governanceMultisig == address(0)) revert ZeroGovernanceAddress();
        if (governanceMultisig.code.length == 0) revert GovernanceMustBeContract();

        _grantRole(DEFAULT_ADMIN_ROLE, governanceMultisig);
        _grantRole(MINTER_ROLE, governanceMultisig);
        _grantRole(PAUSER_ROLE, governanceMultisig);
    }

    /// @notice Requires threshold multisig approval. Not callable by an AI agent or API server.
    function setMintingEnabled(bool enabled) external onlyRole(DEFAULT_ADMIN_ROLE) {
        mintingEnabled = enabled;
        emit MintingStatusChanged(enabled, msg.sender);
    }

    /// @notice Records one authorized allocation against a unique evidence bundle hash.
    /// @dev Independent human review and governance approval occur off-chain before this call.
    function mintVerified(address recipient, uint256 amount, bytes32 evidenceId)
        external
        onlyRole(MINTER_ROLE)
        whenNotPaused
    {
        if (!mintingEnabled) revert MintingDisabled();
        if (recipient == address(0)) revert InvalidRecipient();
        if (amount == 0) revert InvalidAmount();
        if (evidenceId == bytes32(0)) revert EmptyEvidenceId();
        if (usedEvidenceIds[evidenceId]) revert EvidenceAlreadyUsed(evidenceId);

        usedEvidenceIds[evidenceId] = true;
        _mint(recipient, amount);
        emit VerifiedContributionMint(recipient, amount, evidenceId, msg.sender);
    }

    function pause() external onlyRole(PAUSER_ROLE) {
        _pause();
    }

    function unpause() external onlyRole(DEFAULT_ADMIN_ROLE) {
        _unpause();
    }

    function _update(address from, address to, uint256 value)
        internal
        override(ERC20, ERC20Capped)
    {
        require(!paused(), "YTH: token paused");
        super._update(from, to, value);
    }
}
