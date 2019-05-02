const alphanumericStringSort = stringToSort => {
   let lowercaseLetters = [],
       uppercaseLetters = [],
       evenDigits       = [],
       oddDigits        = [];

   stringToSort.split("").forEach(character => {
      if(Number(character) == character){
         if(character % 2 === 0) evenDigits.push(character);
         else oddDigits.push(character);
      }
      else if(character.toUpperCase() === character) uppercaseLetters.push(character);
      else lowercaseLetters.push(character);
   })

   return lowercaseLetters.sort().concat(uppercaseLetters.sort()).concat(evenDigits.sort()).concat(oddDigits.sort()).join("");
}

console.log(alphanumericStringSort("Sorting0123456789"));            // ginortS0246813579
console.log(alphanumericStringSort("foobar1237348421"));             // abfoor2244811337
console.log(alphanumericStringSort("789765445whjdbjwhwfbs977865"));  // bbdfhhjjswww446688555777799