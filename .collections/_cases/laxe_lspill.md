---
title: "Case: Left Axe / Left Spill"
name: Left Axe / Left Spill
short_name: laxe_lspill
top: Axe
top_short_name: axe
top_lr: Left
bot: Spill
bot_short_name: spill
bot_lr: Left

optimal: 3

recognition: Good axe/spill; tent from axe can't exactly swap with tent from spill.

# ALGORITHMS
default_alg:
  alg: "0,-1/0,-3/1,4/-1,0"
  description: Swap tent on top with only corner from spill on bottom to make good thumbs.

# RELATED CASES
parents:
  -
    name: "Right Thumb / Right Thumb"
    short_name: "rthumb_rthumb"
mirrors:
  top_bot:
    -
      name: Left Spill / Left Axe
      short_name: lspill_laxe
  lr:
    -
      name: Right Axe / Right Spill
      short_name: raxe_rspill
  pseudo:
    -
      name: Right Axe / Left Spill
      short_name: raxe_lspill
    -
      name: Left Axe / Right Spill
      short_name: laxe_rspill


---

