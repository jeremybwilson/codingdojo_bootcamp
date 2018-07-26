const swapPairs = require('../intermediateAlgos').swapPairs;

describe("swapPairs", function(){
  it("it should return [2,1,4,3] when [1,2,3,4] is passed", function() {
    expect(swapPairs([1,2,3,4])).toEqual([2,1,4,3]);
  })
  it("it should return [2,1,4,3,5] when [1,2,3,4,5] is passed", function() {
    expect(swapPairs([1,2,3,4,5])).toEqual([2,1,4,3,5]);
  });
  it("it should return [true,'Jeremy',42] when ['Jeremy',true,42] is passed", function(){
    expect(swapPairs(['Jeremy',true,42])).toEqual([true,'Jeremy',42]);
  });
});