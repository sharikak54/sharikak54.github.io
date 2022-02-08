---
title: "Case: Right Cut / Right Cut"
name: Right Cut / Right Cut
short_name: rcut_rcut
top: Cut
top_short_name: cut
top_lr: Right
bot: Cut
bot_short_name: cut
bot_lr: Right

optimal: 3

recognition: Good cut/cut; aligning birds preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,3/-1,-1/0,1"
  description: Solve CO into M2.
color_mirror_algs:
  -
    alg: "samecase"
# RELATED CASES
parents:
  -
    name: "Eopp / Eopp"
    short_name: "eopp_eopp"
  -
    name: "Copp / Copp"
    short_name: "copp_copp"
  -
    name: "Right Pinwheel / Right Pinwheel"
    short_name: "rpinwheel_rpinwheel"
  -
    name: "Copp / Copp"
    short_name: "copp_copp"
  -
    name: "Right Pinwheel / Right Pinwheel"
    short_name: "rpinwheel_rpinwheel"
mirrors:
  lr:
    -
      name: Left Cut / Left Cut
      short_name: lcut_lcut
  pseudo:
    -
      name: Left Cut / Right Cut
      short_name: lcut_rcut
    -
      name: Right Cut / Left Cut
      short_name: rcut_lcut


---

