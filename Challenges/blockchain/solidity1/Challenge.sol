// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Crowdfunding {
    string public name;
    string public description;
    uint256 public goal; 
    uint256 public deadline;
    address public owner; //storing the blockchain address 

    // a modiefer -> can be used as interface for restrictions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the Owner");
        _; //run the remainder of the mother function, else case
    }

    constructor (
        string memory _name,
        string memory _description,
        uint256 _goal,
        uint256 _durationInDays
    ) {
        name = _name;
        description = _description;
        goal = _goal;
        deadline = block.timestamp + (_durationInDays * 1 days);
        owner = msg.sender;
    }

    // this our funding function for users to add money
    function fund() public payable {
        require(block.timestamp < deadline, "Crowdfunding has exceeded.");

    }

    // !!! Challenge  
    // -> This function seems to be unsafe, but why?
    function withdraw() public {
        require(address(this).balance >= goal, "Goal has not been reached");
        uint256 balance = address(this).balance;
        require(balance > 0, "Please withdraw more than 0");

        payable(msg.sender).transfer(balance);
    }

    function getContractBalance () public view returns (uint256) {
        return address(this).balance;
    }
}