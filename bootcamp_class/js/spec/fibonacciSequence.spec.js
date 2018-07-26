const fibonacciSequence = require('../intermediateAlgos').fibonacciSequence;

describe("fibonacciSequence", function(){
  it("when given a value of 0, it should return a value of 0", function() {
    expect(fibonacciSequence(0)).toEqual(0);
  })
  it("when given a value of 1, it should return a value of 1", function() {
    expect(fibonacciSequence(1)).toEqual(1);
  });
  it("when given a value of 7, it should return a value of 13", function(){
    expect(fibonacciSequence(7)).toEqual(13);
  });
});