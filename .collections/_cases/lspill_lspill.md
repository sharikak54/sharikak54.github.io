---
title: "Case: Left Spill / Left Spill"
name: Left Spill / Left Spill
short_name: lspill_lspill
top: Spill
top_short_name: spill
top_lr: Left
bot: Spill
bot_short_name: spill
bot_lr: Left

optimal: 5

recognition: Bad spill/spill; swapping spills preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/2,2/-2,1/3,0/-1,0"
  description: Preserve full kite on bottom in DL, swap isolated edge on top with isolated corner on bottom to make scottie/bird.
color_mirror_algs:
  -
    alg: "1,0/0,3/2,2/1,-2/3,0/-1,0"
  -
    alg: "1,0/-4,-1/-2,1/0,3/0,3/-1,0"
other_algs:
  -
    alg: "-5,0/5,-1/4,1/-3,0/-4,-1/0,1"
  -
    alg: "-5,0/2,-1/1,4/0,3/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Right Scottie / Right Bird"
    short_name: "rscottie_rbird"
  -
    name: "Right Whale / Right Tent"
    short_name: "rwhale_rtent"
  -
    name: "Left Bunny / Right Thumb"
    short_name: "lbunny_rthumb"
mirrors:
  lr:
    -
      name: Right Spill / Right Spill
      short_name: rspill_rspill
  pseudo:
    -
      name: Right Spill / Left Spill
      short_name: rspill_lspill
    -
      name: Left Spill / Right Spill
      short_name: lspill_rspill


---

