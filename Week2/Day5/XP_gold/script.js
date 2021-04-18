let equation = []

function number(num) {
    console.log(num);
    equation.push(num);
}

function operator(symbol){
    console.log(symbol);
    equation.push(symbol);
}

function equal(){
    let result = eval(equation.join(" "));
    alert(result);
    equation=[]
}