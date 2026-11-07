// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Test} from "forge-std/Test.sol";
import {YatharthToken} from "../contracts/YatharthToken.sol";

contract YatharthTokenTest is Test {
    YatharthToken internal token;
    address internal governance = makeAddr("governance-safe");
    address internal timelock = makeAddr("timelock-minter");
    address internal alice = makeAddr("alice");
    address internal bob = makeAddr("bob");
    bytes32 internal allocation = keccak256("allocation-001");
    bytes32 internal evidence = keccak256("evidence-digest-001");

    function setUp() public {
        token = new YatharthToken(governance, timelock);
    }

    function testConstructorRejectsZeroGovernanceOrMinter() public {
        vm.expectRevert(YatharthToken.InvalidAddress.selector);
        new YatharthToken(address(0), timelock);

        vm.expectRevert(YatharthToken.InvalidAddress.selector);
        new YatharthToken(governance, address(0));
    }

    function testRejectsZeroRecipientAndZeroAmount() public {
        vm.startPrank(timelock);
        vm.expectRevert(YatharthToken.InvalidAddress.selector);
        token.mintVerified(address(0), 1, keccak256("allocation-zero-recipient"), evidence);

        vm.expectRevert(YatharthToken.InvalidAmount.selector);
        token.mintVerified(alice, 0, keccak256("allocation-zero-amount"), evidence);
        vm.stopPrank();
    }

    function testInitialStateAndCap() public view {
        assertEq(token.totalSupply(), 0);
        assertEq(token.lifetimeMinted(), 0);
        assertEq(token.MAX_SUPPLY(), 100_000 * 10 ** 8);
        assertEq(token.decimals(), 8);
        assertTrue(token.hasRole(token.DEFAULT_ADMIN_ROLE(), governance));
        assertTrue(token.hasRole(token.MINTER_ROLE(), timelock));
        assertFalse(token.hasRole(token.MINTER_ROLE(), address(this)));
    }

    function testOnlyTimelockMinterCanMint() public {
        vm.expectRevert();
        token.mintVerified(alice, 1, allocation, evidence);

        vm.prank(timelock);
        token.mintVerified(alice, 1, allocation, evidence);
        assertEq(token.balanceOf(alice), 1);
    }

    function testRejectsReusedAllocationId() public {
        vm.startPrank(timelock);
        token.mintVerified(alice, 1, allocation, evidence);
        vm.expectRevert(YatharthToken.InvalidAllocation.selector);
        token.mintVerified(bob, 1, allocation, evidence);
        vm.stopPrank();
    }

    function testRejectsZeroEvidenceDigest() public {
        vm.prank(timelock);
        vm.expectRevert(YatharthToken.InvalidEvidenceDigest.selector);
        token.mintVerified(alice, 1, keccak256("allocation"), bytes32(0));
    }

    function testLifetimeCapCannotBeRecycledByBurning() public {
        vm.prank(timelock);
        token.mintVerified(alice, token.MAX_SUPPLY(), allocation, evidence);

        vm.prank(alice);
        token.burn(1);

        vm.prank(timelock);
        vm.expectRevert(YatharthToken.LifetimeCapExceeded.selector);
        token.mintVerified(bob, 1, keccak256("allocation-002"), keccak256("evidence-002"));
    }

    function testPauseBlocksMintTransferAndBurn() public {
        vm.prank(timelock);
        token.mintVerified(alice, 10, allocation, evidence);

        vm.prank(governance);
        token.pause();

        vm.prank(timelock);
        vm.expectRevert();
        token.mintVerified(bob, 1, keccak256("allocation-002"), keccak256("evidence-002"));

        vm.prank(alice);
        vm.expectRevert();
        token.transfer(bob, 1);

        vm.prank(alice);
        vm.expectRevert();
        token.burn(1);
    }

    function testOnlyGovernanceCanPauseAndUnpause() public {
        vm.prank(alice);
        vm.expectRevert();
        token.pause();

        vm.prank(governance);
        token.pause();

        vm.prank(alice);
        vm.expectRevert();
        token.unpause();

        vm.prank(governance);
        token.unpause();
        assertFalse(token.paused());
    }
}
