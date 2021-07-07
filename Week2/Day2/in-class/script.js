const prices = [20, 12, 5, 4, 2];
const reducer = (accumulator, currentValue) => accumulator + currentValue;

console.log(prices.reduce(reducer));

// now in a loop;

// var total = [20, 12, 5, 4, 2];

// for (let i=0; i < total.length; i++){
//    total  += total[i];
// }
// console.log(total);

