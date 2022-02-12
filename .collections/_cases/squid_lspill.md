---
title: "Case: Squid / Left Spill"
name: Squid / Left Spill
short_name: squid_lspill
top: Squid
top_short_name: squid
bot: Spill
bot_short_name: spill
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/-4,-1/4,1/-1,0"
  description: Preserve full kite on bottom in DL, swap remaining corner on bottom with whale on top.
other_algs:
  -
    alg: "-5,6/3,0/-4,-1/1,4/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Whale / Left Tent"
    short_name: "rwhale_ltent"
mirrors:
  top_bot:
    -
      name: Left Spill / Squid
      short_name: lspill_squid
  lr:
    -
      name: Squid / Right Spill
      short_name: squid_rspill


---

