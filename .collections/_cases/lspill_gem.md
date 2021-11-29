---
title: "Case: Left Spill / Gem"
name: Left Spill / Gem
short_name: lspill_gem
top: Spill
top_short_name: spill
top_lr: Left
bot: Gem
bot_short_name: gem

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-1,2/1,4/-1,-4/0,1"
  description: preserve full kite on top in UL, put gem directly below isolated corner on bottom (in this case, UBR/DBR)
color_mirror_algs:
  -
    alg: ""

# RELATED CASES
parents:
  -
    name: "Right Tent / Left Whale"
    short_name: "rtent_lwhale"
mirrors:
  top_bot:
    -
      name: Gem / Left Spill
      short_name: gem_lspill
  lr:
    -
      name: Right Spill / Gem
      short_name: rspill_gem


---

