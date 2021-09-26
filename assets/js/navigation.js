$(document).ready(() => {
  $("#hamburger").click(onClickHamburger);
});

function onClickHamburger(e) {
  $(this).parent().find("ul.mobileMenu").toggle();
}
