---
title: "Case: Right Dish / Left Dish"
name: Right Dish / Left Dish
short_name: rdish_ldish
top: Dish
top_short_name: dish
top_lr: Right
bot: Dish
bot_short_name: dish
bot_lr: Left

optimal: 5

recognition: bad dish/dish; thumbs are mirrors of each other, or making a half on one face forms plane on the other

# ALGORITHMS
default_alg:
  alg: "0,-1/1,1/2,-1/-2,1/3,0/-1,0"
  description: keep bottom shell in DL, swap 2 edges on top with isolated corner on bottom to form bird/bird
color_mirror_algs:
  -
    alg: ""
other_algs:
  -
    alg: "1,0/-1,-1/3,0/-2,1/3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Bird / Left Bird"
    short_name: "rbird_lbird"
  -
    name: "Right Kite / Plane"
    short_name: "rkite_plane"
  -
    name: "Moth / Left Kite"
    short_name: "moth_lkite"
  -
    name: "Angel / Right Snoopy"
    short_name: "angel_rsnoopy"
  -
    name: "Right Whale / Right Tent"
    short_name: "rwhale_rtent"
  -
    name: "Left Whale / Left Tent"
    short_name: "lwhale_ltent"
  -
    name: "Right Scottie / Hazard"
    short_name: "rscottie_hazard"
  -
    name: "Right Spill / Left Spill"
    short_name: "rspill_lspill"
  -
    name: "Left Snoopy / Angel"
    short_name: "lsnoopy_angel"
mirrors:
  lr:
    -
      name: Left Dish / Right Dish
      short_name: ldish_rdish
  pseudo:
    -
      name: Left Dish / Left Dish
      short_name: ldish_ldish
    -
      name: Right Dish / Right Dish
      short_name: rdish_rdish


---

