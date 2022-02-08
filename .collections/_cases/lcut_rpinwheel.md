---
title: "Case: Left Cut / Right Pinwheel"
name: Left Cut / Right Pinwheel
short_name: lcut_rpinwheel
top: Cut
top_short_name: cut
top_lr: Left
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Right

optimal: 5

recognition: Bad cut/pinwheel - aligning blocks to slice breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,4/3,0/2,-1/4,1/-1,0"
  description: Preserve bird on top and hold any angle on bottom to go to squid/axe.
color_mirror_algs:
  -
    alg: "samecase"
  -
    alg: "0,2/-2,4/0,3/-1,2/1,4/-1,0"
# RELATED CASES
parents:
  -
    name: "Squid / Right Axe"
    short_name: "squid_raxe"
mirrors:
  top_bot:
    -
      name: Right Pinwheel / Left Cut
      short_name: rpinwheel_lcut
  lr:
    -
      name: Right Cut / Left Pinwheel
      short_name: rcut_lpinwheel
  pseudo:
    -
      name: Right Cut / Right Pinwheel
      short_name: rcut_rpinwheel
    -
      name: Left Cut / Left Pinwheel
      short_name: lcut_lpinwheel


---

