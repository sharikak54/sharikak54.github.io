---
title: "Case: Right Pinwheel / Left Cut"
name: Right Pinwheel / Left Cut
short_name: rpinwheel_lcut
top: Pinwheel
top_short_name: pinwheel
top_lr: Right
bot: Cut
bot_short_name: cut
bot_lr: Left

optimal: 5

recognition: Bad pinwheel/cut - aligning blocks to slice breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "3,-1/-2,4/0,3/2,-1/1,4/-1,0"
  description: Hold any angle on top and preserve bird on bottom to go to axe/squid.
color_mirror_algs:
  -
    alg: "samecase"
  -
    alg: "0,-1/-2,4/3,0/-1,2/4,1/-1,0"
# RELATED CASES
parents:
  -
    name: "Right Axe / Squid"
    short_name: "raxe_squid"
mirrors:
  top_bot:
    -
      name: Left Cut / Right Pinwheel
      short_name: lcut_rpinwheel
  lr:
    -
      name: Left Pinwheel / Right Cut
      short_name: lpinwheel_rcut
  pseudo:
    -
      name: Left Pinwheel / Left Cut
      short_name: lpinwheel_lcut
    -
      name: Right Pinwheel / Right Cut
      short_name: rpinwheel_rcut


---

