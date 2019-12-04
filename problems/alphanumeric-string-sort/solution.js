#!/usr/bin/env node

let lower = '';
let upper = '';
let even = '';
let odd = '';
process.argv[2].split('').sort((a, b) => a.localeCompare(b)).forEach(c => {
    if ('a' <= c && c <= 'z') {
        lower += c;
    } else if ('A' <= c && c <= 'Z') {
        upper += c;
    } else if ('02468'.includes(c)) {
        even += c;
    } else {
        odd += c;
    }
});
console.log(lower + upper + even + odd);
