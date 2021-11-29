---
title: "Case: Left Snoopy / Right Spill"
name: Left Snoopy / Right Spill
short_name: lsnoopy_rspill
top: Snoopy
top_short_name: snoopy
top_lr: Left
bot: Spill
bot_short_name: spill
bot_lr: Right

optimal: 4

recognition: Bad snoopy/spill; tent from snoopy can exactly swap with tent from spill.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,1/-4,-1/-3,0/0,1"
  description: Put spill fully in DR, pair with tent on top to make scottie/shell.
color_mirror_algs:
  -
    alg: ""
other_algs:
  -
    alg: "0,-1/1,1/-1,2/3,0/0,1"
  -
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
    name: "Gem / Left Snoopy"
    short_name: "gem_lsnoopy"
  -
    name: "Right Whale / Left Tent"
    short_name: "rwhale_ltent"
mirrors:
  top_bot:
    -
      name: Right Spill / Left Snoopy
      short_name: rspill_lsnoopy
  lr:
    -
      name: Right Snoopy / Left Spill
      short_name: rsnoopy_lspill
  pseudo:
    -
      name: Right Snoopy / Right Spill
      short_name: rsnoopy_rspill
    -
      name: Left Snoopy / Left Spill
      short_name: lsnoopy_lspill


---

