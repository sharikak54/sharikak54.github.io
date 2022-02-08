---
title: "Case: Right Cut / Right Pinwheel"
name: Right Cut / Right Pinwheel
short_name: rcut_rpinwheel
top: Cut
top_short_name: cut
top_lr: Right
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Right

optimal: 4

recognition: Good cut/pinwheel - aligning blocks to slice preserves cubeshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,4/-3,3/-1,-4/0,1"
  description: Intentionally align both faces' blocks to go to good bunnies.
color_mirror_algs:
  -
    alg: "samecase"
  -
    alg: "0,-1/1,4/3,-3/-4,-1/0,1"
  -
    alg: "0,2/4,1/-3,3/2,5/0,1"
  -
    alg: "1,0/-3,3/-1,-1/-2,1/-3,0/-1,0"
  -
    alg: "1,3/-3,3/-1,-1/1,-2/0,-3/-1,0"
    alg: "0,2/4,1/-3,3/2,5/0,1"
  -
    alg: "1,0/-3,3/-1,-1/-2,1/-3,0/-1,0"
  -
    alg: "1,3/-3,3/-1,-1/1,-2/0,-3/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Bunny / Left Bunny"
    short_name: "lbunny_lbunny"
mirrors:
  top_bot:
    -
      name: Right Pinwheel / Right Cut
      short_name: rpinwheel_rcut
  lr:
    -
      name: Left Cut / Left Pinwheel
      short_name: lcut_lpinwheel
  pseudo:
    -
      name: Left Cut / Right Pinwheel
      short_name: lcut_rpinwheel
    -
      name: Right Cut / Left Pinwheel
      short_name: rcut_lpinwheel


---

