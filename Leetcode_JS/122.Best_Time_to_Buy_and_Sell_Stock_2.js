// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let toTalProfit = 0;

    for (let i = 1;i < prices.length; i++) {
        if (prices[i-1] < prices[i]) {
            toTalProfit += prices[i] - prices[i-1];
        } 
    }
  return toTalProfit;  
};

/*
하루간격으로 오를때만 단타를 치면된다.
*/

