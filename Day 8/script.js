const container = document.querySelectorAll(".grid-item");


for(let i of container){
  i.addEventListener("click", function(){
    this.classList.toggle("selected");
  })

}