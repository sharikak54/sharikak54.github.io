---
title: "Case: Right Axe / Left Spill"
name: Right Axe / Left Spill
short_name: raxe_lspill
top: Axe
top_short_name: axe
top_lr: Right
bot: Spill
bot_short_name: spill
bot_lr: Left

optimal: 4

recognition: Bad axe/spill; tent from axe can exactly swap with tent from spill.

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-1/4,1/3,0/-1,0"
  description: Put spill fully in DR, pair with tent on top to make scottie/shell.
other_algs:
  -
    alg: "1,0/-1,-1/1,-2/-3,0/-1,0"
  -
    alg: "1,0/-1,-1/0,-3/-2,1/-1,0"
  -
    alg: "0,-1/-2,1/-3,0/-3,0/-1,0"
  -
    alg: "0,-1/1,1/3,0/3,0/-1,0"
  -
    alg: "-5,6/-1,-1/4,1/0,3/-1,0"
  -
    alg: "-5,6/-1,-1/1,-2/0,-3/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Scottie / Shell"
    short_name: "rscottie_shell"
  -
    name: "Right Pinwheel / Right Kite"
    short_name: "rpinwheel_rkite"
  -
    name: "Gem / Right Axe"
    short_name: "gem_raxe"
  -
    name: "Left Whale / Right Tent"
    short_name: "lwhale_rtent"
mirrors:
  top_bot:
    -
      name: Left Spill / Right Axe
      short_name: lspill_raxe
  lr:
    -
      name: Left Axe / Right Spill
      short_name: laxe_rspill
  pseudo:
    -
      name: Left Axe / Left Spill
      short_name: laxe_lspill
    -
      name: Right Axe / Right Spill
      short_name: raxe_rspill


---

