---
title: "Case: Right Scottie / Left Bird"
name: Right Scottie / Left Bird
short_name: rscottie_lbird
top: Scottie
top_short_name: scottie
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
  top_bot:
    -
      name: Left Bird / Right Scottie
      short_name: lbird_rscottie
  lr:
    -
      name: Left Scottie / Right Bird
      short_name: lscottie_rbird
  pseudo:
    -
      name: Left Scottie / Left Bird
      short_name: lscottie_lbird
    -
      name: Right Scottie / Right Bird
      short_name: rscottie_rbird


---

