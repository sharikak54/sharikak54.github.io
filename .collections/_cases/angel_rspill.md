---
title: "Case: Angel / Right Spill"
name: Angel / Right Spill
short_name: angel_rspill
top: Angel
top_short_name: angel
bot: Spill
bot_short_name: spill
bot_lr: Right

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/0,-3/4,1/-4,-1/0,1"
  description: preserve full kite on bottom in DL, swap remaining corner on bottom with whale on top
color_mirror_algs:
  -
    alg: ""

# RELATED CASES
parents:
  -
    name: "Left Whale / Right Tent"
    short_name: "lwhale_rtent"
mirrors:
  top_bot:
    -
      name: Right Spill / Angel
      short_name: rspill_angel
  lr:
    -
      name: Angel / Left Spill
      short_name: angel_lspill


---

