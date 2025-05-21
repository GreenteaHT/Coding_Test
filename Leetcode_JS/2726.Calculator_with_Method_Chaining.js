// https://leetcode.com/problems/calculator-with-method-chaining

class Calculator {
  /**
   * @param {number} value
   */
  constructor(value) {
    this.alu = value;
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  add(value) {
    this.alu += value;
    return this;
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  subtract(value) {
    this.alu -= value;
    return this;
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  multiply(value) {
    this.alu *= value;
    return this;
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  divide(value) {
    if (value === 0) {
      throw new Error("Division by zero is not allowed");
    }

    this.alu /= value;

    return this;
  }

  /**
   * @param {number} value
   * @return {Calculator}
   */
  power(value) {
    this.alu **= value;
    return this;
  }

  /**
   * @return {number}
   */
  getResult() {
    return this.alu;
  }
}
