---
title: "Case: Hazard / Left Scottie"
name: Hazard / Left Scottie
short_name: hazard_lscottie
top: Hazard
top_short_name: hazard
bot: Scottie
bot_short_name: scottie
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/-3,3/-5,-2/-1,0"
  description: Switch hazard corners on top with isolated corner on bottom; slice should be next to edge from tent on bottom without splitting it.
color_mirror_algs:
  -
    alg: "0,-1/-3,0/-3,3/1,4/-1,0"
  -
    alg: "0,-1/-3,0/3,3/4,1/-1,0"
other_algs:
  -
    alg: "0,-1/-3,0/3,-3/-2,-5/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Baron / Left Baron"
    short_name: "lbaron_lbaron"
  -
    name: "Right Scottie / Left Bird"
    short_name: "rscottie_lbird"
  -
    name: "Moth / Plane"
    short_name: "moth_plane"
mirrors:
  top_bot:
    -
      name: Left Scottie / Hazard
      short_name: lscottie_hazard
  lr:
    -
      name: Hazard / Right Scottie
      short_name: hazard_rscottie


---

