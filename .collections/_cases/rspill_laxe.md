---
title: "Case: Right Spill / Left Axe"
name: Right Spill / Left Axe
short_name: rspill_laxe
top: Spill
top_short_name: spill
top_lr: Right
bot: Axe
bot_short_name: axe
bot_lr: Left

optimal: 4

recognition: Bad spill/axe; tent from spill can exactly swap with tent from axe.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,1/3,0/2,-1/0,1"
  description: Keep spill fully in UL, pair edge from spill with tent to make scottie/shell.
other_algs:
  -
    alg: "0,-1/1,1/2,-1/3,0/0,1"
  -
    alg: "1,0/-1,-1/3,0/3,0/0,1"
  -
    alg: "1,0/-4,-1/-3,0/-3,0/0,1"
    alg: "1,0/-1,-1/3,0/3,0/0,1"
  -
    alg: "1,0/-4,-1/-3,0/-3,0/0,1"

# RELATED CASES
parents:
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
  -
    name: "Left Pinwheel / Left Kite"
    short_name: "lpinwheel_lkite"
  -
    name: "Left Axe / Gem"
    short_name: "laxe_gem"
  -
    name: "Left Tent / Right Whale"
    short_name: "ltent_rwhale"
  -
    name: "Left Pinwheel / Left Kite"
    short_name: "lpinwheel_lkite"
  -
    name: "Left Axe / Gem"
    short_name: "laxe_gem"
  -
    name: "Left Tent / Right Whale"
    short_name: "ltent_rwhale"
mirrors:
  top_bot:
    -
      name: Left Axe / Right Spill
      short_name: laxe_rspill
  lr:
    -
      name: Left Spill / Right Axe
      short_name: lspill_raxe
  pseudo:
    -
      name: Left Spill / Left Axe
      short_name: lspill_laxe
    -
      name: Right Spill / Right Axe
      short_name: rspill_raxe


---

