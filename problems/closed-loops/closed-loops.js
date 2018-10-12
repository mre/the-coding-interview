let closedLoops = (number) => {
  let splitNumber = number.toString().split('');
  return splitNumber.reduce((totalLoops, currentNumber) => {
    if(currentNumber === '0' || currentNumber === '6' || currentNumber === '9') {totalLoops++;}
    else if(currentNumber === '8') {totalLoops += 2;}

    return totalLoops;
  }, 0);
};

console.log(`2876 should give us 3 loops`);
console.log(`Program gives us: ${closedLoops(2876)} loops`);
