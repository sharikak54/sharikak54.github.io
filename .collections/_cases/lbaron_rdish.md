---
title: "Case: Left Baron / Right Dish"
name: Left Baron / Right Dish
short_name: lbaron_rdish
top: Baron
top_short_name: baron
top_lr: Left
bot: Dish
bot_short_name: dish
bot_lr: Right

optimal: 4

recognition: Breaking baron/dish; preserving tents on top and putting slice between shell and gem on bottom breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/3,0/4,1/-1,0"
  description: Put shell of dish in DL and align so slice breaks gem, preserve both tents in UL (goes to scottie/bird).

# RELATED CASES
parents:
  -
    name: "Left Scottie / Right Bird"
    short_name: "lscottie_rbird"
  -
    name: "Left Spill / Left Snoopy"
    short_name: "lspill_lsnoopy"
mirrors:
  top_bot:
    -
      name: Right Dish / Left Baron
      short_name: rdish_lbaron
  lr:
    -
      name: Right Baron / Left Dish
      short_name: rbaron_ldish
  pseudo:
    -
      name: Right Baron / Right Dish
      short_name: rbaron_rdish
    -
      name: Left Baron / Left Dish
      short_name: lbaron_ldish


---

