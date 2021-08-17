function onClickClicker(e) {
  const x = e.offsetX - 100;
  const y = e.offsetY - 100;
  // console.log("(x=" + x + ",y=" + y + ")");

  let section = 1;
  let atan;
  if (x === 0) {
    section = y > 0 ? 0 : 4;
  } else {
    atan = Math.atan(y/x);
    if (atan < 0) {
      atan += Math.PI;
    }
    if (atan > line0) {
      section = 5;
    }
  }
  console.log("(x=" + x + ",y=" + y + ")", "atan:" + atan, "section:" + section);

  console.log(section);
  toggleColor(section);
}

function toggleColor(sectionNum) {
  const $section = $("#clicker1").find("div.section.section" + sectionNum);
  const was_top = $section.text() === "top";
  $section.text(was_top ? "bottom" : "top")
    .css("color", was_top ? "gold" : "");
}

const line0 = Math.atan(Math.PI/12);
const line1 = Math.atan(5 * Math.PI/12);
const line2 = Math.atan(7 * Math.PI/12);
const line3 = Math.atan(11 * Math.PI/12);

$(document).ready(() => {
  $("#clicker1").click(onClickClicker);
  console.log(line0, line1, line2, line3);
});
