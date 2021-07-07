// Exercise 1 : Checking The BMI

// Outside of the objects, create a JS function that compares 
// the BMI of both objects.
// Display the name of the person who has the largest BMI.
// BMI = (Mass) / (Height * Height)

// var person1 = {
//     FullName: "John",
//     Mass: "60",
//     Height: "1.70",
//     BMI: function BMICalc(){
//         let bmi = this.Mass/(this.Height*this.Height);
//         return bmi;
//     }
// };

// var person2 = {
//     FullName: "Anna",
//     Mass: "50",
//     Height: "1.60",
//     BMI: function BMICalc(){
//         let bmi = this.Mass/(this.Height*this.Height);
//         return bmi;
//     }
        
// };

// function compareBMI(bmi1, bmi2){
//     if (bmi1 > bmi2){
//         return bmi1;
//     }
//     else if (bmi < bmi2){
//         return bmi2;
// }
// };

// let higher = compareBMI(person1.BMI(),person2.BMI());

// if (person1.BMI() == higher){
//     console.log(`${person1.FullName} has the higher BMI.`);
// }
// else{
//     console.log(`${person2.FullName} has the higher BMI.`);  
// }


// Exercise 2 : Grade Average

gradesList = [70, 70, 70 , 70]

function findAvg(array){
    let i = 0, sum = 0, len = array.length,gpa;
    while (i < len) {
        sum = sum + array[i];
        gpa = sum / len;
        i++;
    }
    return gpa;
}
let student1 = findAvg(gradesList)
console.log(typeof(student1))


function passed(studentGpa) {
    if ( studentGpa > 65){
        console.log(`You passed!`);
    }
    else{
        console.log(`ya failed!`);  
    }
}

passed(student1)