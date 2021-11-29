// Keeps track of whether each piece is gold.
// TODO use this to recognize faces/cases.
let colors = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]];
let identifyType = "Face";
let $outputSpan;

function onClickClicker(e) {
  toggleColor($(e.target));
}

function toggleColor($section) {
  const id = $section.attr("id");
  const y = Number.parseInt(id.charAt(id.length - 1));
  const x = id.indexOf("top") === 0 ? 0 : 1;
  const wasGold = colors[x][y];

  $section.css("fill", wasGold ? "white" : "gold");
  colors[x][y] = 1 - wasGold;
  
  console.log(colors);
}

function onClickFaceOrCase() {
  const wasFace = identifyType === "Face";
  $("#botWrapper").css("opacity", wasFace ? 1 : 0);
  $(".faceOrCase").text("Identify " + (wasFace ? "Case" : "Face"));
  identifyType = wasFace ? "Case" : "Face";
}

function onClickSubmit() {
  // TODO
  $outputSpan.text("Sorry, this functionality has not yet been implemented...");
}

function onClickReset() {
  colors = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]];
  $(".section").css("fill", "white");
}

$(document).ready(() => {
  $(".section").click(onClickClicker);
  $(".faceOrCase").click(onClickFaceOrCase);
  $(".submit").click(onClickSubmit);
  $(".reset").click(onClickReset);

  $outputSpan = $("#outputSpan");
});
