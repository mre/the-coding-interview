function arraySum(arr) {
  let sum = 0;
  const slicedArray = arr.slice();
  const dimension = 3;
  let flatArray = slicedArray.reduce((acc, val) => acc.concat(val), []);

  for (let i = 0; i < dimension; i++) {
      flatArray = flatArray.reduce((acc, val) => acc.concat(val), []);
  }

  flatArray.forEach((element) => sum += element)
  return sum;
}

console.log(arraySum([1, 2, [3, 4, [5]]]));
