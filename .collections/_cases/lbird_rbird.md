---
title: "Case: Left Bird / Right Bird"
name: Left Bird / Right Bird
short_name: lbird_rbird
top: Bird
top_short_name: bird
top_lr: Left
bot: Bird
bot_short_name: bird
bot_lr: Right

optimal: 4

recognition: Good bird/bird; preserving both kites breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/2,-1/-3,0/0,1"
  description: Preserve kite on bottom, send isolated corner (aligned next to slice) to form snoopy/gem.
color_mirror_algs:
  -
    alg: "1,0/-3,0/2,-1/3,6/0,1"
  -
    alg: "-5,6/0,-3/2,-1/6,3/0,1"
other_algs:
  -
    alg: "-5,6/0,-3/2,-1/0,-3/0,1"

# RELATED CASES
parents:
  -
    name: "Left Snoopy / Gem"
    short_name: "lsnoopy_gem"
  -
    name: "Same Moth / Moth"
    short_name: "moth_moth_same"
mirrors:
  lr:
    -
      name: Right Bird / Left Bird
      short_name: rbird_lbird
  pseudo:
    -
      name: Right Bird / Right Bird
      short_name: rbird_rbird
    -
      name: Left Bird / Left Bird
      short_name: lbird_lbird


---

