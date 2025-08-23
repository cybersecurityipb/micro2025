// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

import {SimpleBank} from "./SimpleBank.sol";

contract Setup {
    SimpleBank public simpleBank;    
    constructor() payable {

        simpleBank = new SimpleBank();
        simpleBank.deposit{value: 10 ether}();
    }

    function isSolved() external view returns (bool) {
        return address(simpleBank).balance == 0;
    }
}