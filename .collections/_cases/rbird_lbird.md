---
title: "Case: Right Bird / Left Bird"
name: Right Bird / Left Bird
short_name: rbird_lbird
top: Bird
top_short_name: bird
top_lr: Right
bot: Bird
bot_short_name: bird
bot_lr: Left

optimal: 4

recognition: Good birds; preserving both kites breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/3,0/-2,1/3,0/-1,0"
  description: Preserve kite on bottom, send isolated corner (aligned next to slice) to form axe/gem.
other_algs:
  -
    alg: "6,5/0,3/-2,1/0,3/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Axe / Gem"
    short_name: "raxe_gem"
  -
    name: "Same Tie / Tie"
    short_name: "tie_tie_same"
mirrors:
  lr:
    -
      name: Left Bird / Right Bird
      short_name: lbird_rbird
  pseudo:
    -
      name: Left Bird / Left Bird
      short_name: lbird_lbird
    -
      name: Right Bird / Right Bird
      short_name: rbird_rbird


---

