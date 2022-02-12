---
title: "Case: Left Spill / Squid"
name: Left Spill / Squid
short_name: lspill_squid
top: Spill
top_short_name: spill
top_lr: Left
bot: Squid
bot_short_name: squid

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/-1,-4/1,4/-1,0"
  description: Preserve full kite on top in UL, swap remaining corner with whale on bottom.
other_algs:
  -
    alg: "-5,6/0,3/-1,-4/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Tent / Right Whale"
    short_name: "ltent_rwhale"
mirrors:
  top_bot:
    -
      name: Squid / Left Spill
      short_name: squid_lspill
  lr:
    -
      name: Right Spill / Squid
      short_name: rspill_squid


---

