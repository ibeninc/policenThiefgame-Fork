// SPDX-License-Identifier: MIT LICENSE

pragma solidity ^0.8.0;

interface IBank {
    function addManyToBankAndPack(address account, uint16[] calldata tokenIds)
        external;

    function randomPoliceOwner(uint256 seed) external view returns (address);
}
