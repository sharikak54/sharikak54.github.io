---
title: "Case: Left Axe / Right Spill"
name: Left Axe / Right Spill
short_name: laxe_rspill
top: Axe
top_short_name: axe
top_lr: Left
bot: Spill
bot_short_name: spill
bot_lr: Right

optimal: 4

recognition: Bad axe/spill; tent from axe can exactly swap with tent from spill.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,1/-4,-1/-3,0/0,1"
  description: Put spill fully in DR, pair with tent on top to make scottie/shell.
other_algs:
  -
    alg: "0,-1/1,1/-1,2/3,0/0,1"
  -
    alg: "0,-1/1,1/0,3/2,-1/0,1"
  -
    alg: "1,0/-1,-1/-3,0/-3,0/0,1"
    alg: "0,-1/1,1/0,3/2,-1/0,1"
  -
    alg: "1,0/-1,-1/-3,0/-3,0/0,1"

# RELATED CASES
parents:
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
  -
    name: "Left Pinwheel / Left Kite"
    short_name: "lpinwheel_lkite"
  -
    name: "Gem / Left Axe"
    short_name: "gem_laxe"
  -
    name: "Right Whale / Left Tent"
    short_name: "rwhale_ltent"
  -
    name: "Left Pinwheel / Left Kite"
    short_name: "lpinwheel_lkite"
  -
    name: "Gem / Left Axe"
    short_name: "gem_laxe"
  -
    name: "Right Whale / Left Tent"
    short_name: "rwhale_ltent"
mirrors:
  top_bot:
    -
      name: Right Spill / Left Axe
      short_name: rspill_laxe
  lr:
    -
      name: Right Axe / Left Spill
      short_name: raxe_lspill
  pseudo:
    -
      name: Right Axe / Right Spill
      short_name: raxe_rspill
    -
      name: Left Axe / Left Spill
      short_name: laxe_lspill


---

