---
name: Right Bird / Right Bird
short_name: rbird_rbird
top: Bird
top_short_name: bird
top_lr: Right
bot: Bird
bot_short_name: bird
bot_lr: Right

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "0,0/"
  description: TODO
mirror_algs:
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
  -
    type: lr
    values: 
      -
        name: Left Bird / Left Bird
        short_name: lbird_lbird
  -
    type: pseudo
    values: 
      -
        name: Left Bird / Right Bird
        short_name: lbird_rbird
      -
        name: Right Bird / Left Bird
        short_name: rbird_lbird


---

Description TODO

