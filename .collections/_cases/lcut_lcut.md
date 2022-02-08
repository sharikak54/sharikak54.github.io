---
title: "Case: Left Cut / Left Cut"
name: Left Cut / Left Cut
short_name: lcut_lcut
top: Cut
top_short_name: cut
top_lr: Left
bot: Cut
bot_short_name: cut
bot_lr: Left

optimal: 3

recognition: Good cut/cut; aligning birds preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,4/-1,-1/0,1"
  description: Solve CO into M2.
color_mirror_algs:
  -
    alg: "samecase"
  -
    alg: "0,-1/-3,3/1,1/-1,0"
# RELATED CASES
parents:
  -
    name: "Eopp / Eopp"
    short_name: "eopp_eopp"
  -
    name: "Copp / Copp"
    short_name: "copp_copp"
  -
    name: "Left Pinwheel / Left Pinwheel"
    short_name: "lpinwheel_lpinwheel"
  -
    name: "Copp / Copp"
    short_name: "copp_copp"
  -
    name: "Left Pinwheel / Left Pinwheel"
    short_name: "lpinwheel_lpinwheel"
mirrors:
  lr:
    -
      name: Right Cut / Right Cut
      short_name: rcut_rcut
  pseudo:
    -
      name: Right Cut / Left Cut
      short_name: rcut_lcut
    -
      name: Left Cut / Right Cut
      short_name: lcut_rcut


---

