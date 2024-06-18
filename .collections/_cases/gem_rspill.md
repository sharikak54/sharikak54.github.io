---
title: "Case: Gem / Right Spill"
name: Gem / Right Spill
short_name: gem_rspill
top: Gem
top_short_name: gem
bot: Spill
bot_short_name: spill
bot_lr: Right

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/-4,-1/4,1/-1,0"
  description: Preserve full kite on bottom in DL, put gem directly above isolated corner on bottom (in this case, in UBR/DBR).
other_algs:
  -
    alg: "1,0/-3,0/-4,-1/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Whale / Left Tent"
    short_name: "rwhale_ltent"
mirrors:
  top_bot:
    -
      name: Right Spill / Gem
      short_name: rspill_gem
  lr:
    -
      name: Gem / Left Spill
      short_name: gem_lspill


---

