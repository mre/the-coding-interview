function array_sum(arr) {
  return arr.toString().split(',').reduce((total, num) => {
    return total += Number(num);
  }, 0)
}

console.log(array_sum([1,2,[3,4,[5]]]))