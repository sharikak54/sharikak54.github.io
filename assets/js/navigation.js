let hamburgerMenuIsOpen = false;

$(document).ready(() => {
  $("body").click(onClickBody);
  $("#hamburger").click(onClickHamburger);
  $("#mobileMenu").click(onClickMobileMenu);
  $(".mobileSubheader").click(onClickSubheader);
});

function onClickBody(e) {
  if (hamburgerMenuIsOpen) {
    const $target = $(e.target);
    const targetIsHamburger = $target.attr("id") === "hamburger" 
      || $target.parents("#hamburger").length;
    const targetIsMobileMenu = $target.parents(".mobileNavigation").length;

    if (!(targetIsHamburger || targetIsMobileMenu)) {
      hamburgerMenuIsOpen = false
      toggleMobileMenu($("#mobileMenu"), false);
      onClickMobileMenu();
    }
  }
}

function onClickHamburger(e) {
  hamburgerMenuIsOpen = true;
  toggleMobileMenu($(this).parent().find("#mobileMenu"), true);
}

function onClickMobileMenu(e) {
  // Toggle all submenus closed.
  $("ul.submenu").each((i) => {
    $submenu = $($("ul.submenu")[i]);
    toggleMobileMenu($submenu, false);
  });
}

/** Toggle visibility of corresponding submenu. */
function onClickSubheader(e) {
  e.preventDefault();
  e.stopPropagation();

  const id = $(this).attr("id");
  const $thisSubmenu = $(this).parent().find(`#submenu${id}`);
  const wasVisible = parseInt($thisSubmenu.css("opacity"));

  // Toggle all other submenus closed too.
  $("ul.submenu").each((i) => {
    const $submenu = $($("ul.submenu")[i]);
    if ($submenu.attr("id") === `submenu${id}`) {
      toggleMobileMenu($submenu, !wasVisible);
    } else {
      toggleMobileMenu($submenu, false);
    }
  });
}

function toggleMobileMenu($menu, display = true) {
  $menu
    .css("opacity", display ? 1 : 0)
    .css("pointer-events", display ? "auto" : "none");
}
