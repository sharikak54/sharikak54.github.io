---
title: "Case: Left Spill / Right Axe"
name: Left Spill / Right Axe
short_name: lspill_raxe
top: Spill
top_short_name: spill
top_lr: Left
bot: Axe
bot_short_name: axe
bot_lr: Right

optimal: 4

recognition: Bad spill/axe; tent from spill can exactly swap with tent from axe.

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-1/-3,0/-2,1/-1,0"
  description: Keep spill fully in UL, pair edge from spill with tent to make scottie/shell.
other_algs:
  -
    alg: "1,0/-1,-1/-2,1/-3,0/-1,0"
  -
    alg: "0,-1/1,1/-3,0/-3,0/-1,0"
    alg: "0,-1/1,1/-3,0/-3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Scottie / Shell"
    short_name: "rscottie_shell"
  -
    name: "Right Pinwheel / Right Kite"
    short_name: "rpinwheel_rkite"
  -
    name: "Right Axe / Gem"
    short_name: "raxe_gem"
  -
    name: "Right Tent / Left Whale"
    short_name: "rtent_lwhale"
  -
    name: "Right Pinwheel / Right Kite"
    short_name: "rpinwheel_rkite"
  -
    name: "Right Axe / Gem"
    short_name: "raxe_gem"
  -
    name: "Right Tent / Left Whale"
    short_name: "rtent_lwhale"
mirrors:
  top_bot:
    -
      name: Right Axe / Left Spill
      short_name: raxe_lspill
  lr:
    -
      name: Right Spill / Left Axe
      short_name: rspill_laxe
  pseudo:
    -
      name: Right Spill / Right Axe
      short_name: rspill_raxe
    -
      name: Left Spill / Left Axe
      short_name: lspill_laxe


---

