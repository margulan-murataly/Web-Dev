/* function onClickButton(){
    alert("Button pressed!");

} */

var power = 0;
var num = 2;

function onClickButton(obj){

    ++power;
    num = 2 ** power;
    obj.innerHTML = "2^" + power + ": " + num;
    obj.style.background = `rgb(${power * 4}, ${power * 3}, ${power * 5})`;
    let radius = power * 0.5;
    obj.style.borderRadius = `${radius}px`;
    obj.style.color = "red";

}

function onInput(obj){

    if(obj.value == "hey" || obj.value == "hello"){
        alert("Hii");
    }
    console.log(obj.value);

}

function GreedyAlgorithm(x){

  while (true) {
    let xx = x;
    x++
    if (x < 101) {
      break;
    }
  }

  console.log(x);
  if (x == 0) {

  }
  else{
    console.log("Error cause it, x: " + x)
    console.console.error("caused by" + x);
  }


}
