---
title: "Case: Right Spill / Gem"
name: Right Spill / Gem
short_name: rspill_gem
top: Spill
top_short_name: spill
top_lr: Right
bot: Gem
bot_short_name: gem

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/1,-2/-1,-4/1,4/-1,0"
  description: Preserve full kite on top in UL, put gem directly below isolated corner on top (in this case, UFR/DFR).
color_mirror_algs:
  -
    alg: ""

# RELATED CASES
parents:
  -
    name: "Left Tent / Right Whale"
    short_name: "ltent_rwhale"
mirrors:
  top_bot:
    -
      name: Gem / Right Spill
      short_name: gem_rspill
  lr:
    -
      name: Left Spill / Gem
      short_name: lspill_gem


---

