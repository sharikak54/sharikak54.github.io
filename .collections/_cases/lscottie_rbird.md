---
title: "Case: Left Scottie / Right Bird"
name: Left Scottie / Right Bird
short_name: lscottie_rbird
top: Scottie
top_short_name: scottie
top_lr: Left
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
      name: Right Bird / Left Scottie
      short_name: rbird_lscottie
  lr:
    -
      name: Right Scottie / Left Bird
      short_name: rscottie_lbird
  pseudo:
    -
      name: Right Scottie / Right Bird
      short_name: rscottie_rbird
    -
      name: Left Scottie / Left Bird
      short_name: lscottie_lbird


---

