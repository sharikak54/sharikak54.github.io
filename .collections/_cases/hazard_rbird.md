---
name: Hazard / Right Bird
short_name: hazard_rbird
top: Hazard
top_short_name: hazard
bot: Bird
bot_short_name: bird
bot_lr: Right

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
  top_bot:
    -
      name: Right Bird / Hazard
      short_name: rbird_hazard
  lr:
    -
      name: Hazard / Left Bird
      short_name: hazard_lbird


---

Description TODO
