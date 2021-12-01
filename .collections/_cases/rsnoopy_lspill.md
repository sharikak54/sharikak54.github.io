---
title: "Case: Right Snoopy / Left Spill"
name: Right Snoopy / Left Spill
short_name: rsnoopy_lspill
top: Snoopy
top_short_name: snoopy
top_lr: Right
bot: Spill
bot_short_name: spill
bot_lr: Left

optimal: 4

recognition: Bad snoopy/spill; tent from snoopy can exactly swap with tent from spill.

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

# RELATED CASES
parents:
  -
    name: "Right Scottie / Shell"
    short_name: "rscottie_shell"
  -
    name: "Right Pinwheel / Right Kite"
    short_name: "rpinwheel_rkite"
  -
    name: "Gem / Right Snoopy"
    short_name: "gem_rsnoopy"
  -
    name: "Left Whale / Right Tent"
    short_name: "lwhale_rtent"
mirrors:
  top_bot:
    -
      name: Left Spill / Right Snoopy
      short_name: lspill_rsnoopy
  lr:
    -
      name: Left Snoopy / Right Spill
      short_name: lsnoopy_rspill
  pseudo:
    -
      name: Left Snoopy / Left Spill
      short_name: lsnoopy_lspill
    -
      name: Right Snoopy / Right Spill
      short_name: rsnoopy_rspill


---

