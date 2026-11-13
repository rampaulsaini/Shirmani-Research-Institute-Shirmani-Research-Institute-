const assert = require("node:assert/strict");
const { ethers } = require("hardhat");

describe("YatharthToken — local disposable-chain tests", function () {
  let owner;
  let recipient;
  let other;
  let governance;
  let token;

  async function governanceCall(functionName, args = []) {
    const data = token.interface.encodeFunctionData(functionName, args);
    return governance.execute(await token.getAddress(), data);
  }

  beforeEach(async function () {
    [owner, recipient, other] = await ethers.getSigners();
    const Governance = await ethers.getContractFactory("MockGovernanceExecutor");
    governance = await Governance.deploy();
    await governance.waitForDeployment();

    const Token = await ethers.getContractFactory("YatharthToken");
    token = await Token.deploy(await governance.getAddress());
    await token.waitForDeployment();
  });

  it("rejects an EOA as the governance address", async function () {
    const Token = await ethers.getContractFactory("YatharthToken");
    await assert.rejects(Token.deploy(owner.address));
  });

  it("starts with minting disabled and blocks unilateral enablement", async function () {
    assert.equal(await token.mintingEnabled(), false);
    await assert.rejects(token.connect(owner).setMintingEnabled(true));
    await governanceCall("setMintingEnabled", [true]);
    assert.equal(await token.mintingEnabled(), true);
  });

  it("blocks direct minting by an account without the governance role", async function () {
    const evidenceId = ethers.keccak256(ethers.toUtf8Bytes("local-test-evidence-1"));
    await assert.rejects(token.connect(owner).mintVerified(recipient.address, 1n, evidenceId));
  });

  it("mints once per evidence ID and enforces the hard supply cap", async function () {
    await governanceCall("setMintingEnabled", [true]);
    const evidenceId = ethers.keccak256(ethers.toUtf8Bytes("local-test-evidence-2"));
    const allocation = ethers.parseEther("10");

    await governanceCall("mintVerified", [recipient.address, allocation, evidenceId]);
    assert.equal(await token.balanceOf(recipient.address), allocation);
    assert.equal(await token.totalSupply(), allocation);

    await assert.rejects(
      governanceCall("mintVerified", [recipient.address, allocation, evidenceId])
    );

    const cap = await token.MAX_SUPPLY();
    const secondEvidenceId = ethers.keccak256(ethers.toUtf8Bytes("local-test-evidence-3"));
    await assert.rejects(
      governanceCall("mintVerified", [recipient.address, cap, secondEvidenceId])
    );
  });

  it("pauses transfers and requires governance to unpause", async function () {
    await governanceCall("setMintingEnabled", [true]);
    const evidenceId = ethers.keccak256(ethers.toUtf8Bytes("local-test-evidence-4"));
    await governanceCall("mintVerified", [owner.address, ethers.parseEther("2"), evidenceId]);

    await governanceCall("pause");
    await assert.rejects(token.connect(owner).transfer(recipient.address, 1n));
    await governanceCall("unpause");
    await token.connect(owner).transfer(recipient.address, 1n);
    assert.equal(await token.balanceOf(recipient.address), 1n);
  });
});
