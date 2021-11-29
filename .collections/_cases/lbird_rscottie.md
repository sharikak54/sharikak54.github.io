---
title: "Case: Left Bird / Right Scottie"
name: Left Bird / Right Scottie
short_name: lbird_rscottie
top: Bird
top_short_name: bird
top_lr: Left
bot: Scottie
bot_short_name: scottie
bot_lr: Right

optimal: 3

recognition: good bird/scottie; the clean slice between the tent and corner on bottom breaks squareshape when preserving the half on top

# ALGORITHMS
default_alg:
  alg: "1,0/0,-3/-1,-4/0,1"
  description: preserve shell of U half in UL, and position isolated corner on bottom next to the slice; first move trades two edges on top with isolated corner on bottom to make dish/dish
color_mirror_algs:
  -
    alg: "1,0/-3,0/-1,-4/0,1"
  -
    alg: "-5,6/0,-3/5,2/0,1"

# RELATED CASES
parents:
  -
    name: "Right Dish / Right Dish"
    short_name: "rdish_rdish"
mirrors:
  top_bot:
    -
      name: Right Scottie / Left Bird
      short_name: rscottie_lbird
  lr:
    -
      name: Right Bird / Left Scottie
      short_name: rbird_lscottie
  pseudo:
    -
      name: Right Bird / Right Scottie
      short_name: rbird_rscottie
    -
      name: Left Bird / Left Scottie
      short_name: lbird_lscottie


---

