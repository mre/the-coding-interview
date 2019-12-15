#!/usr/bin/env node

const z = 'z'.charCodeAt(0);
const a = 'a'.charCodeAt(0);
const s = process.argv[2];
for (let i = 0; i < s.length; ++i) {
    process.stdout.write(s[i] === '\n' ? '\n' : String.fromCharCode(z - (s.charCodeAt(i) - a)));
}
