---
name: Right Bird / Hazard
short_name: rbird_hazard
top: Bird
top_short_name: bird
top_lr: Right
bot: Hazard
bot_short_name: hazard

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
      name: Hazard / Right Bird
      short_name: hazard_rbird
  lr:
    -
      name: Left Bird / Hazard
      short_name: lbird_hazard


---

Description TODO

