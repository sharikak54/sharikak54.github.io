---
title: "Case: Angel / Left Spill"
name: Angel / Left Spill
short_name: angel_lspill
top: Angel
top_short_name: angel
bot: Spill
bot_short_name: spill
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/-4,-1/4,1/-1,0"
  description: Preserve full kite on bottom in DL, swap remaining corner on bottom with whale on top.
color_mirror_algs:
  -
    alg: ""

# RELATED CASES
parents:
  -
    name: "Right Whale / Left Tent"
    short_name: "rwhale_ltent"
mirrors:
  top_bot:
    -
      name: Left Spill / Angel
      short_name: lspill_angel
  lr:
    -
      name: Angel / Right Spill
      short_name: angel_rspill


---

