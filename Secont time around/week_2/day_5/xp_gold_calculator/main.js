let equation = [];
let operation = document.getElementById("display");
let results = document.getElementById('results');
let span = document.createElement("span");

function number(num) {
    equation.push(num);
    operation.value = equation.join("");
} 

function operator(symbol){
    equation.push(symbol);
    operation.value = symbol;
}

function equal(){
    let result = eval(equation.join(""));
    span.textContent = result;
    operation.value = equation.join("")
    results.appendChild(span)
}

function reset(){
    operation.value = ''
    equation = []
}

function backspace(){
    equation.pop();
    operation.value = equation.join("");
}