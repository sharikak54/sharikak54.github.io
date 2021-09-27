$(document).ready(() => {
  $("#hamburger").click(onClickHamburger);
  $(".mobileSubheader").click(onClickSubheader);
});

function onClickHamburger(e) {
  $(this).parent().find("ul.mobileMenu")
    .toggle(true)
    .css("opacity", 1)
    .css("pointer-events", "auto");
}

function onClickSubheader(e) {
  const id = $(this).attr("id");
  const $submenu = $(this).parent().find(`ul#submenu-${id}`);

  // Toggle visibility of corresponding submenu
  if (parseInt($submenu.css("opacity"))) {
    $submenu.hide()
      .css("opacity", 0)
      .css("pointer-events", "none")
  } else {
    $submenu.show()
      .css("opacity", 1)
      .css("pointer-events", "auto")
  }
}
