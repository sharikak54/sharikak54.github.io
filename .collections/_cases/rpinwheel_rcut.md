---
title: "Case: Right Pinwheel / Right Cut"
name: Right Pinwheel / Right Cut
short_name: rpinwheel_rcut
top: Pinwheel
top_short_name: pinwheel
top_lr: Right
bot: Cut
bot_short_name: cut
bot_lr: Right

optimal: 4

recognition: Good pinwheel/cut - aligning blocks to slice preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/4,1/-3,3/-1,-4/0,1"
  description: Intentionally misalign both faces' blocks to go to good bunnies.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "3,-1/1,4/-3,3/2,5/0,1"
  -
    alg: "1,0/-3,3/-1,-1/4,1/3,0/-1,0"
  -
    alg: "-2,0/-3,3/-1,-1/-2,1/0,-3/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Bunny / Left Bunny"
    short_name: "lbunny_lbunny"
mirrors:
  top_bot:
    -
      name: Right Cut / Right Pinwheel
      short_name: rcut_rpinwheel
  lr:
    -
      name: Left Pinwheel / Left Cut
      short_name: lpinwheel_lcut
  pseudo:
    -
      name: Left Pinwheel / Right Cut
      short_name: lpinwheel_rcut
    -
      name: Right Pinwheel / Left Cut
      short_name: rpinwheel_lcut


---

