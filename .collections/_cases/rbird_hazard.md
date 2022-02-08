---
title: "Case: Right Bird / Hazard"
name: Right Bird / Hazard
short_name: rbird_hazard
top: Bird
top_short_name: bird
top_lr: Right
bot: Hazard
bot_short_name: hazard

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/-4,-1/-5,-2/-1,0"
  description: Preserve kite on top, swap isolated edge with whale on bottom to form good tent/whale.
color_mirror_algs:
  -
    alg: "1,0/-3,0/-4,-1/1,4/-1,0"
  -
    alg: "-5,6/0,-3/-4,-1/4,1/-1,0"
    alg: "-5,6/0,-3/-4,-1/4,1/-1,0"
other_algs:
  -
    alg: "-5,6/0,-3/-4,-1/-2,-5/-1,0"
# RELATED CASES
parents:
  -
    name: "Left Tent / Right Whale"
    short_name: "ltent_rwhale"
mirrors:
  top_bot:
    -
      name: Hazard / Right Bird
      short_name: hazard_rbird
  lr:
    -
      name: Left Bird / Hazard
      short_name: lbird_hazard


---

