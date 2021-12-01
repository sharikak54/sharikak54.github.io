---
title: "Case: Right Spill / Left Snoopy"
name: Right Spill / Left Snoopy
short_name: rspill_lsnoopy
top: Spill
top_short_name: spill
top_lr: Right
bot: Snoopy
bot_short_name: snoopy
bot_lr: Left

optimal: 4

recognition: Bad spill/snoopy; tent from spill can exactly swap with tent from snoopy.

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

# RELATED CASES
parents:
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
  -
    name: "Left Pinwheel / Left Kite"
    short_name: "lpinwheel_lkite"
  -
    name: "Left Snoopy / Gem"
    short_name: "lsnoopy_gem"
  -
    name: "Left Tent / Right Whale"
    short_name: "ltent_rwhale"
mirrors:
  top_bot:
    -
      name: Left Snoopy / Right Spill
      short_name: lsnoopy_rspill
  lr:
    -
      name: Left Spill / Right Snoopy
      short_name: lspill_rsnoopy
  pseudo:
    -
      name: Left Spill / Left Snoopy
      short_name: lspill_lsnoopy
    -
      name: Right Spill / Right Snoopy
      short_name: rspill_rsnoopy


---

