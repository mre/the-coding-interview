const getIndex = (i, N) => parseInt((i%3)*N + (i/3)),
      getSwapIndex = (i, N) => getIndex(i, N) < i ? getSwapIndex(getIndex(i, N), N) : i,
      convert_array = (arr) => {
          for (let i=0; i<arr.length; i++){
              let swapIndex = getSwapIndex(i, parseInt(arr.length/3));
              [arr[i], arr[swapIndex]] = [arr[swapIndex], arr[i]];
          }
          return arr;
      };
