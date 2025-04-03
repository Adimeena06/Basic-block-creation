// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TrafficVerifier {
    struct Request {
        address sender;
        uint256 timestamp;
        bool verified;
    }

    mapping(address => Request) public requests;
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function verifyRequest() public {
        require(requests[msg.sender].timestamp == 0, "Request already exists");
        requests[msg.sender] = Request(msg.sender, block.timestamp, true);
    }

    function isVerified(address user) public view returns (bool) {
        return requests[user].verified;
    }
}
