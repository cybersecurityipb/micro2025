// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SimpleBank {

    mapping(address => uint256) private _balances;

    function balanceOf(address _who) external view returns(uint256) {
        return _balances[_who];
    }

    function deposit() external payable {
        _balances[msg.sender] += msg.value;
    }

    // Reentrancy can't drain Ether here as it will revert on underflow (check the compiler version).
    function withdraw(uint256 amount) external {
        require(_balances[msg.sender] >= amount, "not enough amount");

        (bool success,) = payable(msg.sender).call{value: amount}("");
        require(success, "eth not sent");

        _balances[msg.sender] -= amount;
    }
}
