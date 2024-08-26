/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const ALPHA = /^[a-z|A-Z|0-9]+$/;
    let pointerL = 0;
    let pointerR = s.length - 1;
    while(pointerL <= pointerR) {
        if (ALPHA.test(s[pointerL]) === false) {
            pointerL += 1;
            continue;
        } else if (ALPHA.test(s[pointerR]) === false) {
            pointerR -= 1;
            continue;
        }

        if (s[pointerL].toLowerCase() !== s[pointerR].toLowerCase()) {
            return false;
        } else {
            pointerL += 1;
            pointerR -= 1;
        }
    }
    return true;
};


/*
투 포인터 문제이기 때문에 포인터를 이용하여 풀었음
*/