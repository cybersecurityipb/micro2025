// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Gov {

    function createAndExecute(address target, uint256 amount, bytes memory data) external payable {
        require(msg.value == 42069 ether, "not enough ether");

        (bool success, ) = target.call{value: amount}(data);
        require(success);
    }

    receive() external payable {}
}
