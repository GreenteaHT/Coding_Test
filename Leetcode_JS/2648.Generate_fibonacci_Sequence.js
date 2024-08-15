// https://leetcode.com/problems/generate-fibonacci-sequence

/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let n1=0, n2=1;
    while(true) {
        yield n1;
        let temp = n2;
        n2 = n1 + n2;
        n1 = temp;
    }
};

//test
/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */

/*
yeild를 앞쪽에 해줌으로서 n1 = 0 부터 출력 가능
*/