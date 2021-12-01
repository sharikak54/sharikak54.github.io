---
title: "Case: Right Spill / Angel"
name: Right Spill / Angel
short_name: rspill_angel
top: Spill
top_short_name: spill
top_lr: Right
bot: Angel
bot_short_name: angel

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/1,4/-1,-4/0,1"
  description: Preserve full kite on top in UL, swap remaining corner with whale on bottom.

# RELATED CASES
parents:
  -
    name: "Right Tent / Left Whale"
    short_name: "rtent_lwhale"
mirrors:
  top_bot:
    -
      name: Angel / Right Spill
      short_name: angel_rspill
  lr:
    -
      name: Left Spill / Angel
      short_name: lspill_angel


---

