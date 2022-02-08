---
title: "Case: Left Pinwheel / Right Pinwheel"
name: Left Pinwheel / Right Pinwheel
short_name: lpinwheel_rpinwheel
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Right

optimal: 4

recognition: Bad pinwheel/pinwheel; tents can't connect to form kites.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,-3/0,3/-1,-1/0,1"
  description: Do good pinwheel/pinwheel into M2; all alignments will form matching trees.
color_mirror_algs:
  -
    alg: "samecase"
  -
    alg: "0,-1/-2,-2/0,3/-1,-1/0,1"
  -
    alg: "-2,3/2,2/-2,1/-1,-1/0,1"
  -
    alg: "-3,2/3,3/-2,1/-1,-1/0,1"
  -
    alg: "-3,2/3,3/-3,0/1,1/-1,0"
    alg: "-2,3/2,2/-2,1/-1,-1/0,1"
  -
    alg: "-3,2/3,3/-2,1/-1,-1/0,1"
  -
    alg: "-3,2/3,3/-3,0/1,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Same Tree / Tree"
    short_name: "tree_tree_same"
  -
    name: "Same Tie / Tie"
    short_name: "tie_tie_same"
  -
    name: "Same Tie / Tie"
    short_name: "tie_tie_same"
mirrors:
  lr:
    -
      name: Right Pinwheel / Left Pinwheel
      short_name: rpinwheel_lpinwheel
  pseudo:
    -
      name: Right Pinwheel / Right Pinwheel
      short_name: rpinwheel_rpinwheel
    -
      name: Left Pinwheel / Left Pinwheel
      short_name: lpinwheel_lpinwheel


---

