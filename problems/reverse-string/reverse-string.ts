function reverseString(str: string): string {
  let strReverse: string = "";
  let strArr: string[] = str.split('');

  strReverse = strArr.reverse().join('');

  return strReverse;
}

const str: string = "Hello World!";

console.log(reverseString(str));
