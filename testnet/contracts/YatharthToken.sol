// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

// Testnet reference only. Pin OpenZeppelin Contracts v5.x in the test project.
// No deployment or public minting is authorized by this source file.
import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {ERC20Burnable} from "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import {AccessControl} from "@openzeppelin/contracts/access/AccessControl.sol";
import {Pausable} from "@openzeppelin/contracts/utils/Pausable.sol";

contract YatharthToken is ERC20, ERC20Burnable, AccessControl, Pausable {
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");

    uint256 public constant TOKEN_DECIMALS = 8;
    uint256 public constant MAX_SUPPLY = 100_000 * 10 ** TOKEN_DECIMALS;

    // Lifetime issuance never decreases, even if a holder burns tokens.
    uint256 public lifetimeMinted;

    mapping(bytes32 allocationId => bool used) public usedAllocations;

    error InvalidAddress();
    error InvalidAllocation();
    error InvalidEvidenceDigest();
    error LifetimeCapExceeded();

    event VerifiedAllocationMinted(
        bytes32 indexed allocationId,
        address indexed recipient,
        uint256 amount,
        bytes32 indexed evidenceDigest
    );

    constructor(address governanceSafe, address timelockMinter)
        ERC20("Yatharth Mudra Test", "tYTH")
    {
        if (governanceSafe == address(0) || timelockMinter == address(0)) {
            revert InvalidAddress();
        }

        _grantRole(DEFAULT_ADMIN_ROLE, governanceSafe);
        _grantRole(PAUSER_ROLE, governanceSafe);
        _grantRole(MINTER_ROLE, timelockMinter);
    }

    function decimals() public pure override returns (uint8) {
        return uint8(TOKEN_DECIMALS);
    }

    /// @notice Mint only for a verified, governance-approved allocation.
    /// @dev MINTER_ROLE must be held by a timelock executor controlled by a 3-of-5 Safe.
    ///      AI services and ordinary API servers must never hold this role.
    function mintVerified(
        address recipient,
        uint256 amount,
        bytes32 allocationId,
        bytes32 evidenceDigest
    ) external onlyRole(MINTER_ROLE) whenNotPaused {
        if (recipient == address(0) || amount == 0) revert InvalidAddress();
        if (allocationId == bytes32(0) || usedAllocations[allocationId]) {
            revert InvalidAllocation();
        }
        if (evidenceDigest == bytes32(0)) revert InvalidEvidenceDigest();
        if (lifetimeMinted + amount > MAX_SUPPLY) revert LifetimeCapExceeded();

        usedAllocations[allocationId] = true;
        lifetimeMinted += amount;
        _mint(recipient, amount);

        emit VerifiedAllocationMinted(allocationId, recipient, amount, evidenceDigest);
    }

    function pause() external onlyRole(PAUSER_ROLE) {
        _pause();
    }

    function unpause() external onlyRole(DEFAULT_ADMIN_ROLE) {
        _unpause();
    }

    function _update(address from, address to, uint256 value)
        internal
        override
    {
        _requireNotPaused();
        super._update(from, to, value);
    }
}
