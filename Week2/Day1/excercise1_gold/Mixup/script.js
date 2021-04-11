let str1 = "mix";
let chunk1 = str1.slice(0, 2);
let str2 = "pod";
let chunk2 = str2.slice(0, 2);

console.log(chunk1)
console.log(chunk2)

let chunk3 = str1.slice(2);
let chunk4 = str2.slice(2);

console.log(chunk3)
console.log(chunk4)

let final1 = chunk2 + chunk3
let final2 = chunk1 + chunk4

console.log(final1)
console.log(final2)