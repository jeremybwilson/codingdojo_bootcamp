function swapPairs(array){
  debugger; // optional debugger statement for testing
  let i = 0;
  // using a while loop to iterate through the array
  while (array[i] && array[i + 1]) {
    // create temp variable to store array index
    let temp = array[i];
    array[i] = array[i + 1];
    array[i + 1] = temp;
    // increment i by +2 with each loop
    i += 2;
  }
  // return the updated array
  return array;
}
// Test cases
// console.log(swapPairs([1,2,3,4]));            // Expected result => [2,1,4,3]
// console.log(swapPairs([1,2,3,4,5]));          // Expected result => [2,1,4,3,5]
// console.log(swapPairs(['Jeremy',true,42]));   // Expected result => [true,'Jeremy',42]

function reverseArray(arr){ 
  for(var i=0; i<arr.length/2; i++) { 
    temp = arr[arr.length-i-1]; 
    arr[arr.length-i-1] = arr[i]; 
    arr[i] = temp; 
  } 
  return arr; 
}
// b = reverseArray([1,2,3]);
// Test case
// console.log('b is', b);

// Fabulous Fibonacci
// Expected output => 0,1,1,2,3,5,8,13,21

function fibonacciSequence(num){
  // set variables a and b
  // set a to b and b to 1
  let a = 0;
  let b = 1;
  // loop while num >= 0 
  while(num > 0){
    // set sum to a+b
    let sum = a + b;
    // set a to b
    a = b;
    // set b to sum
    b = sum;
    // decrement num
    num--;
  }
  // return value
  return a;
}

module.exports = {
  swapPairs,
  reverseArray,
  fibonacciSequence
};