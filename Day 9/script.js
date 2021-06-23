const container = document.querySelectorAll(".grid");
let count = 0;

for(let i of container){
  i.addEventListener("click", function(){
    this.classList.toggle("selected");
    if (this.classList.contains("selected")){
      count++;
    }
    else{
      count--
    }
    // count++;
    document.getElementById("booked").innerText="Number of seats reserved: "+ count; 
    document.getElementById("remaining").innerText="Number of seats left: "+(36- count); 
  })

}

