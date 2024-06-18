---
title: "Case: Right Bird / Left Scottie"
name: Right Bird / Left Scottie
short_name: rbird_lscottie
top: Bird
top_short_name: bird
top_lr: Right
bot: Scottie
bot_short_name: scottie
bot_lr: Left

optimal: 3

recognition: Good bird/scottie; the clean slice between the tent and corner on bottom breaks squareshape when preserving the kite on top.

# ALGORITHMS
default_alg:
  alg: "0,-1/0,3/1,4/-1,0"
  description: Hold U kite in UL, and position isolated corner on bottom next to the slice; first move trades two edges on top with isolated corner on bottom to make good thumbs.
color_mirror_algs:
  -
    alg: "0,-1/3,0/1,4/-1,0"
  -
    alg: "6,5/0,3/-5,-2/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Thumb / Right Thumb"
    short_name: "rthumb_rthumb"
mirrors:
  top_bot:
    -
      name: Left Scottie / Right Bird
      short_name: lscottie_rbird
  lr:
    -
      name: Left Bird / Right Scottie
      short_name: lbird_rscottie
  pseudo:
    -
      name: Left Bird / Left Scottie
      short_name: lbird_lscottie
    -
      name: Right Bird / Right Scottie
      short_name: rbird_rscottie


---

