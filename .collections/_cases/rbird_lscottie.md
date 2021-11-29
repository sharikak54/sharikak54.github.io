---
title: "Case: Right Bird / Left Scottie"
name: Right Bird / Left Scottie
short_name: rbird_lscottie
top: Bird
top_short_name: bird
top_lr: Right
bot: Scottie
bot_short_name: scottie
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
      name: Left Scottie / Right Bird
      short_name: lscottie_rbird
  lr:
    -
      name: Left Bird / Right Scottie
      short_name: lbird_rscottie
  pseudo:
    -
      name: Left Bird / Left Scottie
      short_name: lbird_lscottie
    -
      name: Right Bird / Right Scottie
      short_name: rbird_rscottie


---

