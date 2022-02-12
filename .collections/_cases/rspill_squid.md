---
title: "Case: Right Spill / Squid"
name: Right Spill / Squid
short_name: rspill_squid
top: Spill
top_short_name: spill
top_lr: Right
bot: Squid
bot_short_name: squid

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/1,4/-1,-4/0,1"
  description: Preserve full kite on top in UL, swap remaining corner with whale on bottom.
other_algs:
  -
    alg: "6,5/0,-3/1,4/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Right Tent / Left Whale"
    short_name: "rtent_lwhale"
mirrors:
  top_bot:
    -
      name: Squid / Right Spill
      short_name: squid_rspill
  lr:
    -
      name: Left Spill / Squid
      short_name: lspill_squid


---

