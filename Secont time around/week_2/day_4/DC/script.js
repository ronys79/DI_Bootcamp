console.log("\n****** Week02 Day 04 - Daily Challenge: Words In The Stars ******");


function starFrame(){
  let userInput = prompt("Input as many words but separated by commas without any spaces: ").split(',');
  //Catch largest word
  let wordLargest = 0;
  for (item of userInput){
      if (item.length>wordLargest){
          wordLargest = item.length;
      }
  }
  //output frame
  console.log("*".repeat(wordLargest+4));
  for (let i=0; i<userInput.length;i++){
      console.log("* " + userInput[i] + " ".repeat(wordLargest-userInput[i].length) + " *");
  }
  console.log("*".repeat(wordLargest+4));
  }
  
  starFrame();