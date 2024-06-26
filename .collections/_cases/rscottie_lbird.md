---
title: "Case: Right Scottie / Left Bird"
name: Right Scottie / Left Bird
short_name: rscottie_lbird
top: Scottie
top_short_name: scottie
top_lr: Right
bot: Bird
bot_short_name: bird
bot_lr: Left

optimal: 3

recognition: Good scottie/bird; the clean slice between the tent and corner on top breaks squareshape when preserving the kite on bottom.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/-4,-1/0,1"
  description: Position isolated corner on top next to the slice, and hold D kite in DL; first move trades isolated corner on top with two edges on bottom to make good thumbs.
color_mirror_algs:
  -
    alg: "1,0/0,-3/-4,-1/0,1"
  -
    alg: "-5,6/-3,0/2,5/0,1"

# RELATED CASES
parents:
  -
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
mirrors:
  top_bot:
    -
      name: Left Bird / Right Scottie
      short_name: lbird_rscottie
  lr:
    -
      name: Left Scottie / Right Bird
      short_name: lscottie_rbird
  pseudo:
    -
      name: Left Scottie / Left Bird
      short_name: lscottie_lbird
    -
      name: Right Scottie / Right Bird
      short_name: rscottie_rbird


---

