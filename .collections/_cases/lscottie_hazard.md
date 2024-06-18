---
title: "Case: Left Scottie / Hazard"
name: Left Scottie / Hazard
short_name: lscottie_hazard
top: Scottie
top_short_name: scottie
top_lr: Left
bot: Hazard
bot_short_name: hazard

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/0,-3/-3,3/-5,-2/-1,0"
  description: Switch isolated corner on top with hazard corners on bottom; slice should be next to edge from tent on top without splitting it.
color_mirror_algs:
  -
    alg: "0,-1/0,-3/-3,3/1,4/-1,0"
  -
    alg: "0,-1/0,-3/3,-3/4,1/-1,0"
  -
    alg: "6,5/-3,0/-3,3/4,1/-1,0"
  -
    alg: "6,5/-3,0/3,-3/1,4/-1,0"
other_algs:
  -
    alg: "0,-1/0,-3/3,-3/-2,-5/-1,0"
  -
    alg: "6,5/-3,0/-3,3/-2,-5/-1,0"
  -
    alg: "6,5/-3,0/3,-3/-5,-2/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Bunny / Right Bunny"
    short_name: "rbunny_rbunny"
  -
    name: "Right Scottie / Left Bird"
    short_name: "rscottie_lbird"
  -
    name: "Tie / Tree"
    short_name: "tie_tree"
mirrors:
  top_bot:
    -
      name: Hazard / Left Scottie
      short_name: hazard_lscottie
  lr:
    -
      name: Right Scottie / Hazard
      short_name: rscottie_hazard


---

