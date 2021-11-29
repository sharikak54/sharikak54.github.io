---
title: "Case: Right Dish / Left Baron"
name: Right Dish / Left Baron
short_name: rdish_lbaron
top: Dish
top_short_name: dish
top_lr: Right
bot: Baron
bot_short_name: baron
bot_lr: Left

optimal: 4

recognition: breaking dish/baron; putting slice between shell and gem on top and preserving tents on bottom breaks squareshape

# ALGORITHMS
default_alg:
  alg: "0,-1/0,-3/0,3/1,4/-1,0"
  description: put shell of dish in UL and align so slice breaks gem, preserve both tents in DL (goes to good bird/scottie)
color_mirror_algs:
  -
    alg: ""
other_algs:
  -
    alg: "6,5/-3,0/0,3/4,1/-1,0"
  -
    alg: "3,5/3,0/0,-3/1,4/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Bird / Left Scottie"
    short_name: "rbird_lscottie"
  -
    name: "Left Snoopy / Left Spill"
    short_name: "lsnoopy_lspill"
mirrors:
  top_bot:
    -
      name: Left Baron / Right Dish
      short_name: lbaron_rdish
  lr:
    -
      name: Left Dish / Right Baron
      short_name: ldish_rbaron
  pseudo:
    -
      name: Left Dish / Left Baron
      short_name: ldish_lbaron
    -
      name: Right Dish / Right Baron
      short_name: rdish_rbaron


---

