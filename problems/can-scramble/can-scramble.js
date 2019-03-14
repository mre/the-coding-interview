const can_scramble = (a, b) => 
    a.split("").sort().join("") == b.split("").sort().join("");
    
console.log(can_scramble("abc", "cba")); // true
console.log(can_scramble("aab", "bba")); // false
console.log(can_scramble("xyzxyz", "zzyyxx")); //true
console.log(can_scramble("xyzbbxyz", "zzyyxxaa")); //false
