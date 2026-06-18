let box = document.getElementById("box");
let score = document.getElementById("score");

let points = 0;

function moveBox() {
  let x = Math.random() * 90;
  let y = Math.random() * 90;

  box.style.left = x + "%";
  box.style.top = y + "%";
}

box.addEventListener("click", () => {
  points++;
  score.textContent = points;
  moveBox();
});

// старт
moveBox();