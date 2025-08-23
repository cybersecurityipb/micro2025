// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

import {SimpleBank} from "./SimpleBank.sol";
import {Gov} from "./Gov.sol";


contract Setup {
    SimpleBank public simpleBank;
    Gov public gov;
    
    constructor() payable {

        simpleBank = new SimpleBank();
        gov = new Gov();

        simpleBank.deposit{value: 72_000 ether}();

        (bool success,) = address(gov).call{value: 3_000 ether}("");
        require(success);
    }

    function isSolved() external view returns (bool) {
        return address(gov).balance == 0;
    }
}