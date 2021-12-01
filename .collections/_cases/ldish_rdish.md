---
title: "Case: Left Dish / Right Dish"
name: Left Dish / Right Dish
short_name: ldish_rdish
top: Dish
top_short_name: dish
top_lr: Left
bot: Dish
bot_short_name: dish
bot_lr: Right

optimal: 5

recognition: Bad dish/dish; thumbs are mirrors of each other, or making a kite on one face forms plane on the other

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-1/-2,1/2,-1/-3,0/0,1"
  description: Keep bottom shell in DL, swap 2 edges on top with isolated corner on bottom to form bird/bird.
other_algs:
  -
    alg: "0,-1/1,1/-3,0/2,-1/-3,0/0,1"

# RELATED CASES
parents:
  -
    name: "Left Bird / Right Bird"
    short_name: "lbird_rbird"
  -
    name: "Left Kite / Plane"
    short_name: "lkite_plane"
  -
    name: "Moth / Right Kite"
    short_name: "moth_rkite"
  -
    name: "Angel / Left Snoopy"
    short_name: "angel_lsnoopy"
  -
    name: "Left Whale / Left Tent"
    short_name: "lwhale_ltent"
  -
    name: "Right Whale / Right Tent"
    short_name: "rwhale_rtent"
  -
    name: "Left Scottie / Hazard"
    short_name: "lscottie_hazard"
  -
    name: "Left Spill / Right Spill"
    short_name: "lspill_rspill"
  -
    name: "Right Snoopy / Angel"
    short_name: "rsnoopy_angel"
mirrors:
  lr:
    -
      name: Right Dish / Left Dish
      short_name: rdish_ldish
  pseudo:
    -
      name: Right Dish / Right Dish
      short_name: rdish_rdish
    -
      name: Left Dish / Left Dish
      short_name: ldish_ldish


---

