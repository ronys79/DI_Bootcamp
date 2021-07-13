let beerWall = +prompt("Give a number to begin counting down bottles");
let beerSubtract = 0;
let bottleGrammar = "bottles"
let downGrammar = "it"

while (beerWall > 0){
    if (beerWall > beerSubtract){
    beerWall= beerWall - beerSubtract;
    beerSubtract++;
        if (beerWall == 1){
            bottleGrammar = "bottle";
        }
        else if (beerSubtract > 1){
            downGrammar = "them"
        }
        console.log(`${beerWall}  ${bottleGrammar} of beer on the wall`);
        console.log(`${beerWall}  ${bottleGrammar} of beer`);
    }
        if (beerWall > beerSubtract){
        console.log(`Take  ${beerSubtract}  down, pass ${downGrammar} around`)
    }
        else {
            console.log(`Only ${beerWall} ${bottleGrammar} left! Let's finish them all and drink ${beerWall} ${bottleGrammar} !!!`);
            console.log('No more beers on the wall!')
            break
        }
}