/*
    Converting n-ary argument function to Unary(1-ary) argument function
*/

// n-ary a
// const add = (a, b, c) => a + b + c;
// console.log(add(1, 2, 3));

const add = (a) => (b) => (c) => a + b + c;

console.log(add(1));       // returns b
console.log(add(1)(2));    // returns c
console.log(add(1)(2)(3)); // returns 6