---
title: "Case: Right Cut / Left Pinwheel"
name: Right Cut / Left Pinwheel
short_name: rcut_lpinwheel
top: Cut
top_short_name: cut
top_lr: Right
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Left

optimal: 5

recognition: Bad cut/pinwheel - aligning blocks to slice breaks cubeshape.

# ALGORITHMS
default_alg:
  alg: "1,0/2,-4/-3,0/-2,1/-4,-1/0,1"
  description: Preserve bird on tap and hold any angle on bottom to go to squid/axe or axe/squid.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "1,0/-4,2/0,-3/-2,1/-1,-4/0,1"
  -
    alg: "1,3/-4,2/-3,0/1,-2/-4,-1/0,1"
  -
    alg: "1,3/2,-4/0,-3/1,-2/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Squid / Left Axe"
    short_name: "squid_laxe"
mirrors:
  top_bot:
    -
      name: Left Pinwheel / Right Cut
      short_name: lpinwheel_rcut
  lr:
    -
      name: Left Cut / Right Pinwheel
      short_name: lcut_rpinwheel
  pseudo:
    -
      name: Left Cut / Left Pinwheel
      short_name: lcut_lpinwheel
    -
      name: Right Cut / Right Pinwheel
      short_name: rcut_rpinwheel


---

