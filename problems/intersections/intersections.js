const intersections = (arr1, arr2) => arr1.filter(element => arr2.indexOf(element) > -1);

console.log(intersections(['dog', 'cat', 'egg'], ['cat', 'dog', 'chicken'])); // ["dog", "cat"]