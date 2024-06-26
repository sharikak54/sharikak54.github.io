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

recognition: Good bird/scottie; the clean slice between the tent and corner on bottom breaks squareshape when preserving the kite on top.

# ALGORITHMS
default_alg:
  alg: "1,0/0,-3/-1,-4/0,1"
  description: Preserve shell of U kite in UL, and position isolated corner on bottom next to the slice; first move trades two edges on top with isolated corner on bottom to make good thumbs.
color_mirror_algs:
  -
    alg: "1,0/-3,0/-1,-4/0,1"
  -
    alg: "-5,6/0,-3/5,2/0,1"

# RELATED CASES
parents:
  -
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
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

