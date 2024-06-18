---
title: "Case: Right Axe / Right Spill"
name: Right Axe / Right Spill
short_name: raxe_rspill
top: Axe
top_short_name: axe
top_lr: Right
bot: Spill
bot_short_name: spill
bot_lr: Right

optimal: 3

recognition: Good axe/spill; tent from axe can't exactly swap with tent from spill.

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/-1,-4/0,1"
  description: Swap tent on top with only corner from spill on bottom to make good thumbs.
color_mirror_algs:
  -
    alg: "1,0/3,0/-1,-4/0,1"
  -
    alg: "-5,6/0,3/5,2/0,1"
other_algs:
  -
    alg: "-5,6/3,0/5,2/0,1"

# RELATED CASES
parents:
  -
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
mirrors:
  top_bot:
    -
      name: Right Spill / Right Axe
      short_name: rspill_raxe
  lr:
    -
      name: Left Axe / Left Spill
      short_name: laxe_lspill
  pseudo:
    -
      name: Left Axe / Right Spill
      short_name: laxe_rspill
    -
      name: Right Axe / Left Spill
      short_name: raxe_lspill


---

