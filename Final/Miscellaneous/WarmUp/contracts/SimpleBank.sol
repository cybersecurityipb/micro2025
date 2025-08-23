// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SimpleBank {

    struct User {
        address addr;
        uint256 amount;
    }

    User[] private users;

    function deposit() external payable {
        users.push(User({addr: msg.sender, amount: msg.value}));
    }

    function withdraw(uint256 index) external {
        User storage user = users[index];
        require(user.addr == msg.sender);
        uint256 amount = user.amount;

        user = users[users.length - 1];
        users.pop();

        (bool success,) = msg.sender.call{value: amount}("");
        require(success);
    }

}
