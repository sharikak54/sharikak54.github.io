---
title: "Case: Hazard / Right Scottie"
name: Hazard / Right Scottie
short_name: hazard_rscottie
top: Hazard
top_short_name: hazard
bot: Scottie
bot_short_name: scottie
bot_lr: Right

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/-3,3/2,5/0,1"
  description: Switch hazard corners on top with isolated corner on bottom; slice should be next to edge from tent on bottom without splitting it.
color_mirror_algs:
  -
    alg: "1,0/3,0/-3,3/-4,-1/0,1"
  -
    alg: "1,0/3,0/3,-3/-1,-4/0,1"
other_algs:
  -
    alg: "1,0/3,0/3,-3/5,2/0,1"

# RELATED CASES
parents:
  -
    name: "Left Bunny / Left Bunny"
    short_name: "lbunny_lbunny"
  -
    name: "Left Scottie / Right Bird"
    short_name: "lscottie_rbird"
  -
    name: "Tie / Tree"
    short_name: "tie_tree"
mirrors:
  top_bot:
    -
      name: Right Scottie / Hazard
      short_name: rscottie_hazard
  lr:
    -
      name: Hazard / Left Scottie
      short_name: hazard_lscottie


---

