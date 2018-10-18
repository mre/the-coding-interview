function atbash(str: string): string {
  let lcStr: string = str.toLowerCase();
  let cipherStr: string = ""; 

  if (str === undefined) {
    return "";
  } 

  for (let i = 0; i < lcStr.length; i++) {
    cipherStr += String.fromCharCode(97 - (lcStr.charCodeAt(i) - 90));
  }

  return cipherStr;
}

console.log(atbash("irk"));
console.log(atbash("low"));
console.log(atbash("hob"));
console.log(atbash("hold"));
console.log(atbash("holy"));
console.log(atbash("horn"));
console.log(atbash("glow"));
console.log(atbash("grog"));
console.log(atbash("zoo"));
console.log(atbash("wizard"));
