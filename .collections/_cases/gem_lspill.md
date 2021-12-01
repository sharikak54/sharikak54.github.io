---
title: "Case: Gem / Left Spill"
name: Gem / Left Spill
short_name: gem_lspill
top: Gem
top_short_name: gem
bot: Spill
bot_short_name: spill
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/2,-1/4,1/-4,-1/0,1"
  description: Preserve full kite on bottom in DL, put gem directly above isolated corner on bottom (in this case, in UFR/DFR).

# RELATED CASES
parents:
  -
    name: "Left Whale / Right Tent"
    short_name: "lwhale_rtent"
mirrors:
  top_bot:
    -
      name: Left Spill / Gem
      short_name: lspill_gem
  lr:
    -
      name: Gem / Right Spill
      short_name: gem_rspill


---

