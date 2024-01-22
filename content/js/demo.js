// get id div #demo and change text

function myCallback() {
  const elt = document.getElementById("demo");
  if (elt.innerHTML == "Hello JavaScript") {
    elt.innerHTML = "Hello World";
    elt.style.backgroundColor = "#64a6ea";
    elt.style.maxWidth = "7em";
  } else {
    elt.innerHTML = "Hello JavaScript";
    elt.style.backgroundColor = "#7eed94";
    elt.style.maxWidth = "10em";
  }

}


const intervalID = setInterval(myCallback, 1000, "Parameter 1", "Parameter 2");

