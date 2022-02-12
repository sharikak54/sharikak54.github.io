---
title: "Case: Right Bird / Right Bird"
name: Right Bird / Right Bird
short_name: rbird_rbird
top: Bird
top_short_name: bird
top_lr: Right
bot: Bird
bot_short_name: bird
bot_lr: Right

optimal: 5

recognition: Bad birds; preserving both kites preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/-1,-1/4,1/3,0/-1,0"
  description: Preserve kite on bottom, send isolated corner (aligned away from slice) to form axe/spill.
color_mirror_algs:
  -
    alg: "1,0/0,-3/-1,-1/-2,1/-3,0/-1,0"
  -
    alg: "-5,6/-3,0/-1,-1/4,1/-3,6/-1,0"
  -
    alg: "0,-1/1,4/-1,-1/4,1/3,0/-1,0"
  -
    alg: "0,-1/1,4/-1,-1/1,-2/-3,0/-1,0"
other_algs:
  -
    alg: "1,0/-4,-1/1,1/3,0/3,0/-1,0"
  -
    alg: "1,0/-4,-1/-2,1/-3,0/-3,0/-1,0"
  -
    alg: "6,-1/3,0/1,1/-3,0/-3,0/-1,0"
  -
    alg: "6,-1/4,1/-1,-1/-2,1/-3,0/-1,0"
  -
    alg: "6,-1/4,1/-1,-1/-3,0/-2,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Axe / Left Spill"
    short_name: "raxe_lspill"
  -
    name: "Right Whale / Right Tent"
    short_name: "rwhale_rtent"
  -
    name: "Left Bunny / Right Thumb"
    short_name: "lbunny_rthumb"
mirrors:
  lr:
    -
      name: Left Bird / Left Bird
      short_name: lbird_lbird
  pseudo:
    -
      name: Left Bird / Right Bird
      short_name: lbird_rbird
    -
      name: Right Bird / Left Bird
      short_name: rbird_lbird


---

