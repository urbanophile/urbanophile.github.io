// get id div #demo and change text
let some_soft_colours = ["#D9EDBF", "#FFB996", "#FFCF81", "#FEFBC9B", "#FBF3D5", "#D6DAC8", "#79AC78"];
let some_text = ["Hello", "World", "How", "Are", "You", "Today", "?"];

function myCallback() {
  // cycle through the colours and text sequentially
  let colour = some_soft_colours.shift();
  let text = some_text.shift();
  some_soft_colours.push(colour);
  some_text.push(text);
  // get the div element
  let div = document.getElementById("demo");
  // change the text and colour
  div.innerHTML = text;
  div.style.color = colour;
  div.style.backgroundColor = "navy";
  // set max width
  div.style.maxWidth = "80px";


}


const intervalID = setInterval(myCallback, 1000, "Parameter 1", "Parameter 2");

