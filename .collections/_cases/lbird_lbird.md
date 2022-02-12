---
title: "Case: Left Bird / Left Bird"
name: Left Bird / Left Bird
short_name: lbird_lbird
top: Bird
top_short_name: bird
top_lr: Left
bot: Bird
bot_short_name: bird
bot_lr: Left

optimal: 5

recognition: Bad birds; preserving both kites preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/3,0/1,1/-4,-1/-3,0/0,1"
  description: Preserve kite on bottom, send isolated corner (aligned away from slice) to form axe/spill.
color_mirror_algs:
  -
    alg: "0,-1/0,3/1,1/3,0/2,-1/0,1"
  -
    alg: "6,5/3,0/1,1/-4,-1/3,6/0,1"
  -
    alg: "-5,0/0,-3/-1,-1/-3,0/-3,0/0,1"
other_algs:
  -
    alg: "0,-1/4,1/-1,-1/-3,0/-3,0/0,1"
  -
    alg: "-5,0/-3,0/-1,-1/3,0/3,0/0,1"
  -
    alg: "-5,0/-3,0/2,-1/-3,0/-3,0/0,1"
  -
    alg: "-5,0/-4,-1/1,1/2,-1/3,0/0,1"
  -
    alg: "-5,0/-4,-1/1,1/3,0/2,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Left Axe / Right Spill"
    short_name: "laxe_rspill"
  -
    name: "Left Whale / Left Tent"
    short_name: "lwhale_ltent"
  -
    name: "Right Bunny / Left Thumb"
    short_name: "rbunny_lthumb"
mirrors:
  lr:
    -
      name: Right Bird / Right Bird
      short_name: rbird_rbird
  pseudo:
    -
      name: Right Bird / Left Bird
      short_name: rbird_lbird
    -
      name: Left Bird / Right Bird
      short_name: lbird_rbird


---

