/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxProfit = 0;
    let min = prices[0];

    for (let i = 1;i < prices.length; i++) {
     if (min > prices[i]) {
        min = prices[i];
     } else {
        maxProfit = Math.max(maxProfit, prices[i] - min);
     }
    }
  return maxProfit;  
};

/*
최소값을 갱신하고부터 최대값만 저장하는 max변수를 생성하여 알고리즘을 조금 바꾸어도 되지만, 굳이 그럴 필요가 없어 조건문을 간단하게 만들었다.

작은 수가 앞으로 나올때마다 최소값을 갱신시키고, 
maxprofit에 최소값과 현재값을 뺀 값을 비교하여 최대값을 확인하는 방식
*/