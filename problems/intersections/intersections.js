const intersections = (arr1, arr2) => arr1.filter(element => arr2.includes(element));

console.log(intersections(["dog", "cat", "egg"], ["cat", "dog", "chicken"])); // ["dog", "cat"]
