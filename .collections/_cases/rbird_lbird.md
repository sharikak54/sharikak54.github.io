---
name: Right Bird / Left Bird
short_name: rbird_lbird
top: Bird
top_short_name: bird
top_lr: Right
bot: Bird
bot_short_name: bird
bot_lr: Left

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "1,0/5,5/0,1"
  description: TODO
color_mirror_algs:
  -
    alg: "0,0/"
    description: TODO
other_algs:
  -
    alg: "0,0/"
    description: TODO

# RELATED CASES
parents:
  -
    name: TODO
    short_name: TODO
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

Description TODO

