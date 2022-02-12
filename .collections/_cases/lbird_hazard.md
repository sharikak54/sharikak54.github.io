---
title: "Case: Left Bird / Hazard"
name: Left Bird / Hazard
short_name: lbird_hazard
top: Bird
top_short_name: bird
top_lr: Left
bot: Hazard
bot_short_name: hazard

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/3,0/4,1/-1,-4/0,1"
  description: Preserve kite on top, swap isolated edge with whale on bottom to form good tent/whale.
other_algs:
  -
    alg: "6,5/0,3/4,1/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Right Tent / Left Whale"
    short_name: "rtent_lwhale"
mirrors:
  top_bot:
    -
      name: Hazard / Left Bird
      short_name: hazard_lbird
  lr:
    -
      name: Right Bird / Hazard
      short_name: rbird_hazard


---

