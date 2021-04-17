// Instructions
// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out “nested for loops” on Google).
// Do this Daily Challenge by youself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *

1.
for(var i=1; i<=6; i++){
    console.log("* ".repeat(i));
 }
 
 2. 

 var a,b,c;
for(a=1; a <=6; a++)
{
   for (b=1; b < a; b++)
     {
    c=c+("* ");        
      }
 console.log(c);
 c='';     
}

---

 var a,

------------------------

var star = "*"
    function addStar(star){
        star += "*";
    }
    addStar()