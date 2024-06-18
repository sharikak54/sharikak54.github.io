---
title: "Case: Left Spill / Left Axe"
name: Left Spill / Left Axe
short_name: lspill_laxe
top: Spill
top_short_name: spill
top_lr: Left
bot: Axe
bot_short_name: axe
bot_lr: Left

optimal: 3

recognition: Good spill/axe; tent from spill can't exactly swap with tent from axe.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/4,1/-1,0"
  description: Swap only corner from spill on top with tent on bottom to make good thumbs.
color_mirror_algs:
  -
    alg: "0,-1/0,-3/4,1/-1,0"
  -
    alg: "6,5/-3,0/-2,-5/-1,0"
other_algs:
  -
    alg: "6,5/0,-3/-2,-5/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Thumb / Right Thumb"
    short_name: "rthumb_rthumb"
mirrors:
  top_bot:
    -
      name: Left Axe / Left Spill
      short_name: laxe_lspill
  lr:
    -
      name: Right Spill / Right Axe
      short_name: rspill_raxe
  pseudo:
    -
      name: Right Spill / Left Axe
      short_name: rspill_laxe
    -
      name: Left Spill / Right Axe
      short_name: lspill_raxe


---

