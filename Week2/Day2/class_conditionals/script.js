/*  if (expression) {
 Statement(s) to be excecuted if expresion is true
}


 if (statement === True)
*/



let age = +prompt('How old are you?');
console.log(typeof(age));

if (age >= 19) {
    console.log('Powering On. Enjoy the ride!');
}

else if (age < 18){
    console.log('Sorry, you are too young to drive this car. Powering off')
}

else {
    console.log('Congratulations on your first year of driving. Enjoy the ride!')
}

// else if (age < 5){
//     console.log('You are the next Michael Schumacher in no less than')

/*
 let isTeacher = confirm('Are you a teacher?');
console.log('I am at Dev Inst');

if (isTeacher) {
    console.log('and you are a teacher');
}
*/