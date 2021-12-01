---
title: "Case: Left Spill / Angel"
name: Left Spill / Angel
short_name: lspill_angel
top: Spill
top_short_name: spill
top_lr: Left
bot: Angel
bot_short_name: angel

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/-1,-4/1,4/-1,0"
  description: Preserve full kite on top in UL, swap remaining corner with whale on bottom.

# RELATED CASES
parents:
  -
    name: "Left Tent / Right Whale"
    short_name: "ltent_rwhale"
mirrors:
  top_bot:
    -
      name: Angel / Left Spill
      short_name: angel_lspill
  lr:
    -
      name: Right Spill / Angel
      short_name: rspill_angel


---

