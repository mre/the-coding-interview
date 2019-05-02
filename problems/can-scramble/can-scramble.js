const canScramble = (originalString, scrambledString) => {
   if(originalString.length !== scrambledString.length) return false;

   const sortedOriginalStringArray = originalString.split("").sort(),
         sortedScrambledStringArray = scrambledString.split("").sort();

   return sortedOriginalStringArray.every((letter, index) => letter === sortedScrambledStringArray[index]);
}

console.log(canScramble("abc", "cba")); // true
console.log(canScramble("aab", "bba")); // false
console.log(canScramble("xyzxyz", "zzyyxx")); //true
console.log(canScramble("xyzbbxyz", "zzyyxxaa")); //false