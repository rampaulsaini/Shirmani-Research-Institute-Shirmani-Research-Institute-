// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

/// @notice TEST-ONLY call-forwarding fixture. Never deploy this contract to any
/// public or value-bearing network: it has no signer threshold or multisig logic.
contract MockGovernanceExecutor {
    function execute(address target, bytes calldata data) external returns (bytes memory) {
        (bool success, bytes memory result) = target.call(data);
        require(success, "TEST_EXECUTION_FAILED");
        return result;
    }
}
