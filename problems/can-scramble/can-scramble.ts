function sortString(str: string): string {
  let strSorted: string = '';
  let strArr: string[] = str.split('');

  strSorted = strArr.sort().join('');

  return strSorted;
}

function can_scramble(str1:string, str2:string): boolean {
  if (str1.length !== str2.length) {
    return false;
  }

  let str1Sorted = sortString(str1);
  let str2Sorted = sortString(str2);

  for (let i = 0; i < str1Sorted.length; i++) {
    if (str1Sorted !== str2Sorted) {
      return false;
    }
  }

  return true;
}

console.log(can_scramble("abc", "cba")); // true
console.log(can_scramble("aab", "bba")); // false
console.log(can_scramble("xyzxyz", "zzyyxx")); //true
console.log(can_scramble("xyzbbxyz", "zzyyxxaa")); //false