// https://leetcode.com/problems/gas-station/

/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    var total = 0;
    var startGasStation = 0;
    var sumGas = 0
    var sumCost = 0

    for (var i = 0; i < gas.length; i++) {
        // 총합을 이용하면 현재 인덱스가 한바퀴를 돌아도 문제가 없는지 확인 할 수 있음
        sumGas += gas[i];
        sumCost += cost[i];
        total += gas[i] - cost[i];
        if (total < 0) {
            startGasStation = i + 1;
            total = 0;
        };
    };
    return (sumGas >= sumCost) ? startGasStation : -1;
};