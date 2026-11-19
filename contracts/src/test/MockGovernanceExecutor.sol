// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

/// @notice TEST-ONLY fixture. Never deploy to a public or value-bearing network.
contract MockGovernanceExecutor {
    function execute(address target, bytes calldata data) external returns (bytes memory) {
        (bool success, bytes memory result) = target.call(data);
        require(success, "TEST_EXECUTION_FAILED");
        return result;
    }
}
