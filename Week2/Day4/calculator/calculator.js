function math() {
    let num1 = [];
    let sym1 = prompt("what ya want to do with it");
    let num2 = +prompt("Type second number");
    
    let results;

    // find a way to use .strip

    if (sym1 == "+") {
        results = num1 + num2
        console.log(results)
    } else if (sym1 == "-") {
        results = num1 - num2
        console.log(results)
    } else if (sym1 == "*") {
        results = num1 * num2
        console.log(results)
    } else if (sym1 == "/") {
        results = num1 / num2
        console.log(results)
    } else {
        console.log("Sorry...try again")
    }
}
math()