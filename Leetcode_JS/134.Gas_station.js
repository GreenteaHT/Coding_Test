// https://leetcode.com/problems/gas-station/

/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    var alu = 0;
    var answer = 0;

    for (var i = 0; i < gas.length; i++) {

        if (alu < 0) {
            answer = i + 1;
            alu = 0;
        };
    }

    return 

};