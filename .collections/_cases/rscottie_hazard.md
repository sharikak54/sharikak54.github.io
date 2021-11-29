---
title: "Case: Right Scottie / Hazard"
name: Right Scottie / Hazard
short_name: rscottie_hazard
top: Scottie
top_short_name: scottie
top_lr: Right
bot: Hazard
bot_short_name: hazard

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/-3,3/2,5/0,1"
  description: Switch isolated corner on top with hazard corners on bottom; slice should be next to edge from tent on top without splitting it.
color_mirror_algs:
  -
    alg: "1,0/0,3/-3,3/-4,-1/0,1"
  -
    alg: "1,0/0,3/3,-3/-1,-4/0,1"
  -
    alg: "-5,6/3,0/-3,3/-1,-4/0,1"
  -
    alg: "-5,6/3,0/3,-3/-4,-1/0,1"
other_algs:
  -
    alg: "1,0/0,3/3,-3/5,2/0,1"
  -
    alg: "-5,6/3,0/-3,3/5,2/0,1"
  -
    alg: "-5,6/3,0/3,-3/2,5/0,1"

# RELATED CASES
parents:
  -
    name: "Right Baron / Right Baron"
    short_name: "rbaron_rbaron"
  -
    name: "Left Scottie / Right Bird"
    short_name: "lscottie_rbird"
  -
    name: "Moth / Plane"
    short_name: "moth_plane"
mirrors:
  top_bot:
    -
      name: Hazard / Right Scottie
      short_name: hazard_rscottie
  lr:
    -
      name: Left Scottie / Hazard
      short_name: lscottie_hazard


---

