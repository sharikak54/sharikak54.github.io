---
title: "Case: Hazard / Left Bird"
name: Hazard / Left Bird
short_name: hazard_lbird
top: Hazard
top_short_name: hazard
bot: Bird
bot_short_name: bird
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/0,3/1,4/-4,-1/0,1"
  description: Preserve kite on bottom, swap whale on top with isolated edge on bottom to form good whale/tent.
other_algs:
  -
    alg: "6,5/3,0/1,4/-1,-4/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Whale / Right Tent"
    short_name: "lwhale_rtent"
mirrors:
  top_bot:
    -
      name: Left Bird / Hazard
      short_name: lbird_hazard
  lr:
    -
      name: Hazard / Right Bird
      short_name: hazard_rbird


---

