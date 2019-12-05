const firstGreater = (arr, n) => arr.find(num => num > n);

console.log(firstGreater([2, 10,5,6,80], 6));   // 10
console.log(firstGreater([2, 10,5,6,80], 20));  // 80
console.log(firstGreater([2, 10,5,6,80], 100)); // undefined