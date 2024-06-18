---
title: "Case: Left Pinwheel / Left Cut"
name: Left Pinwheel / Left Cut
short_name: lpinwheel_lcut
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Cut
bot_short_name: cut
bot_lr: Left

optimal: 4

recognition: Good pinwheel/cut - aligning blocks to slice preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/-3,3/4,1/-1,0"
  description: Intentionally misalign both faces' blocks to go to good bunnies.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "-2,0/-1,-4/-3,3/-5,-2/-1,0"
  -
    alg: "0,-1/-3,3/1,1/-1,2/0,3/0,1"
  -
    alg: "0,-1/3,-3/1,1/-4,-1/-3,0/0,1"
  -
    alg: "3,-1/-3,3/1,1/3,0/2,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Right Bunny / Right Bunny"
    short_name: "rbunny_rbunny"
mirrors:
  top_bot:
    -
      name: Left Cut / Left Pinwheel
      short_name: lcut_lpinwheel
  lr:
    -
      name: Right Pinwheel / Right Cut
      short_name: rpinwheel_rcut
  pseudo:
    -
      name: Right Pinwheel / Left Cut
      short_name: rpinwheel_lcut
    -
      name: Left Pinwheel / Right Cut
      short_name: lpinwheel_rcut


---

