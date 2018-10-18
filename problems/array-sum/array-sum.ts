function arraySum(arr):number {
    let sum: number = 0;
    let dArr: number[] = [...arr];
    let dimension: number = 3;
    let flatArr = dArr.reduce((acc, val) => acc.concat(val), []);
  
    for (let i = 0; i < dimension; i++) {
      flatArr = flatArr.reduce((acc, val) => acc.concat(val), []);
    }
  
    flatArr.forEach(ele => sum += ele);
                    
    return sum;
  }
  
  console.log(arraySum([1,2,[3,4,[5]]]));