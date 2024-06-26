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

recognition: Good birds; preserving both kites breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/2,-1/-3,0/0,1"
  description: Preserve kite on bottom, send isolated corner (aligned next to slice) to form axe/gem.
other_algs:
  -
    alg: "-5,6/0,-3/2,-1/0,-3/0,1"

# RELATED CASES
parents:
  -
    name: "Left Axe / Gem"
    short_name: "laxe_gem"
  -
    name: "Same Tie / Tie"
    short_name: "tie_tie_same"
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

