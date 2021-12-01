---
title: "Case: Left Spill / Right Snoopy"
name: Left Spill / Right Snoopy
short_name: lspill_rsnoopy
top: Spill
top_short_name: spill
top_lr: Left
bot: Snoopy
bot_short_name: snoopy
bot_lr: Right

optimal: 4

recognition: Bad spill/snoopy; tent from spill can exactly swap with tent from snoopy.

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-1/-3,0/-2,1/-1,0"
  description: Keep spill fully in UL, pair edge from spill with tent to make scottie/shell.
other_algs:
  -
    alg: "1,0/-1,-1/-2,1/-3,0/-1,0"
  -
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
    name: "Right Snoopy / Gem"
    short_name: "rsnoopy_gem"
  -
    name: "Right Tent / Left Whale"
    short_name: "rtent_lwhale"
mirrors:
  top_bot:
    -
      name: Right Snoopy / Left Spill
      short_name: rsnoopy_lspill
  lr:
    -
      name: Right Spill / Left Snoopy
      short_name: rspill_lsnoopy
  pseudo:
    -
      name: Right Spill / Right Snoopy
      short_name: rspill_rsnoopy
    -
      name: Left Spill / Left Snoopy
      short_name: lspill_lsnoopy


---

