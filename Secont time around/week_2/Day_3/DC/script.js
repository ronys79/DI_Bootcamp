let n = 5; // Use to increase stars

let starPattern = "";

for (let i = 1; i <= n; i++) {
  for (let j = 0; j < i; j++) {
    starPattern += "*" + " ";
  }
  starPattern += "\n";
}
console.log(starPattern);