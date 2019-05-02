const atbash = originalString => {
   const upperCasedLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
   
   return originalString.toUpperCase()
                        .split("")
                        .map(letter => upperCasedLetters[upperCasedLetters.length - 1 - upperCasedLetters.indexOf(letter)])
                        .join("");
}

console.log(atbash("irk"));    // RIP
console.log(atbash("low"));    // OLD
console.log(atbash("hob"));    // SLY
console.log(atbash("hold"));   // SLOW
console.log(atbash("holy"));   // SLOB
console.log(atbash("horn"));   // SLIM
console.log(atbash("glow"));   // TOLD
console.log(atbash("grog"));   // TILT
console.log(atbash("zoo"));    // ALL
console.log(atbash("wizard")); // DRAZIW