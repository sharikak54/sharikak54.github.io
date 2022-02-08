---
title: "Case: Left Scottie / Right Bird"
name: Left Scottie / Right Bird
short_name: lscottie_rbird
top: Scottie
top_short_name: scottie
top_lr: Left
bot: Bird
bot_short_name: bird
bot_lr: Right

optimal: 3

recognition: Good scottie/bird; the clean slice between the tent and corner on top breaks squareshape when preserving the kite on bottom.

# ALGORITHMS
default_alg:
  alg: "0,-1/3,0/4,1/-1,0"
  description: Position isolated corner on top next to the slice, and hold D kite in DL; first move trades isolated corner on top with two edges on bottom to make good thumbs.
color_mirror_algs:
  -
    alg: "0,-1/0,3/4,1/-1,0"
  -
    alg: "6,5/3,0/-2,-5/-1,0"
    alg: "6,5/3,0/-2,-5/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Thumb / Right Thumb"
    short_name: "rthumb_rthumb"
mirrors:
  top_bot:
    -
      name: Right Bird / Left Scottie
      short_name: rbird_lscottie
  lr:
    -
      name: Right Scottie / Left Bird
      short_name: rscottie_lbird
  pseudo:
    -
      name: Right Scottie / Right Bird
      short_name: rscottie_rbird
    -
      name: Left Scottie / Left Bird
      short_name: lscottie_lbird


---

