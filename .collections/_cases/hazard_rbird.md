---
title: "Case: Hazard / Right Bird"
name: Hazard / Right Bird
short_name: hazard_rbird
top: Hazard
top_short_name: hazard
bot: Bird
bot_short_name: bird
bot_lr: Right

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/0,-3/-1,-4/4,1/-1,0"
  description: Preserve kite on bottom, swap whale on top with isolated edge on bottom to form good whale/tent.
other_algs:
  -
    alg: "-5,6/-3,0/-1,-4/1,4/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Whale / Left Tent"
    short_name: "rwhale_ltent"
mirrors:
  top_bot:
    -
      name: Right Bird / Hazard
      short_name: rbird_hazard
  lr:
    -
      name: Hazard / Left Bird
      short_name: hazard_lbird


---

