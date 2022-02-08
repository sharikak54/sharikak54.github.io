---
title: "Case: Left Cut / Left Pinwheel"
name: Left Cut / Left Pinwheel
short_name: lcut_lpinwheel
top: Cut
top_short_name: cut
top_lr: Left
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Left

optimal: 4

recognition: Good cut/pinwheel - aligning blocks to slice preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-4/-3,3/4,1/-1,0"
  description: Intentionally misalign both faces' blocks to go to good bunnies.
color_mirror_algs:
  -
    alg: "samecase"
  -
    alg: "1,3/-4,-1/-3,3/-5,-2/-1,0"
  -
    alg: "0,-1/-3,3/1,1/2,-1/0,3/0,1"
  -
    alg: "0,2/-3,3/1,1/-4,-1/-3,0/0,1"
    alg: "0,-1/-3,3/1,1/2,-1/0,3/0,1"
  -
    alg: "0,2/-3,3/1,1/-4,-1/-3,0/0,1"

# RELATED CASES
parents:
  -
    name: "Right Bunny / Right Bunny"
    short_name: "rbunny_rbunny"
mirrors:
  top_bot:
    -
      name: Left Pinwheel / Left Cut
      short_name: lpinwheel_lcut
  lr:
    -
      name: Right Cut / Right Pinwheel
      short_name: rcut_rpinwheel
  pseudo:
    -
      name: Right Cut / Left Pinwheel
      short_name: rcut_lpinwheel
    -
      name: Left Cut / Right Pinwheel
      short_name: lcut_rpinwheel


---

