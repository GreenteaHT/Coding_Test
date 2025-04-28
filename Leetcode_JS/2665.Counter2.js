// https://leetcode.com/problems/counter-ii/

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (init) {
  const initValue = init;
  var count = init;

  function increment() {
    return ++count;
  }

  function reset() {
    count = initValue;
    return count;
  }

  function decrement() {
    return --count;
  }

  return {
    increment: increment,
    reset: reset,
    decrement: decrement,
  };
};

//Test
const counter = createCounter(5);
counter.increment(); // 6
counter.reset(); // 5
counter.decrement(); // 4

//
/*
function을 만들고 반환하는 대신에
객체를 반환할 때 function을 넣어도됨ㅁ
*/
