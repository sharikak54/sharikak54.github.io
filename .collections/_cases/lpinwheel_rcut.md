---
title: "Case: Left Pinwheel / Right Cut"
name: Left Pinwheel / Right Cut
short_name: lpinwheel_rcut
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Cut
bot_short_name: cut
bot_lr: Right

optimal: 5

recognition: Bad pinwheel/cut - aligning blocks to slice breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-4,2/-3,0/-2,1/-4,-1/0,1"
  description: Hold any angle on top and preserve bird on bottom to go to axe/squid.
color_mirror_algs:
  -
    alg: "samecase"
  -
    alg: "-2,0/-4,2/0,-3/1,-2/-1,-4/0,1"
# RELATED CASES
parents:
  -
    name: "Left Axe / Squid"
    short_name: "laxe_squid"
mirrors:
  top_bot:
    -
      name: Right Cut / Left Pinwheel
      short_name: rcut_lpinwheel
  lr:
    -
      name: Right Pinwheel / Left Cut
      short_name: rpinwheel_lcut
  pseudo:
    -
      name: Right Pinwheel / Right Cut
      short_name: rpinwheel_rcut
    -
      name: Left Pinwheel / Left Cut
      short_name: lpinwheel_lcut


---

