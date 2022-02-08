---
title: "Case: Right Spill / Right Axe"
name: Right Spill / Right Axe
short_name: rspill_raxe
top: Spill
top_short_name: spill
top_lr: Right
bot: Axe
bot_short_name: axe
bot_lr: Right

optimal: 3

recognition: Good spill/axe; tent from spill can't exactly swap with tent from axe.

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/-4,-1/0,1"
  description: Swap only corner from spill on top with tent on bottom to make good thumbs.

# RELATED CASES
parents:
  -
    name: "Left Thumb / Left Thumb"
    short_name: "lthumb_lthumb"
mirrors:
  top_bot:
    -
      name: Right Axe / Right Spill
      short_name: raxe_rspill
  lr:
    -
      name: Left Spill / Left Axe
      short_name: lspill_laxe
  pseudo:
    -
      name: Left Spill / Right Axe
      short_name: lspill_raxe
    -
      name: Right Spill / Left Axe
      short_name: rspill_laxe


---

