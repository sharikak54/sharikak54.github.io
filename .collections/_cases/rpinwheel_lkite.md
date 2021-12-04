---
title: "Case: Right Pinwheel / Left Kite"
name: Right Pinwheel / Left Kite
short_name: rpinwheel_lkite
top: Pinwheel
top_short_name: pinwheel
top_lr: Right
bot: Kite
bot_short_name: kite
bot_lr: Left

optimal: 4

recognition: Bad pinwheel/kite - aligning blocks to slice breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/5,-1/3,0/-2,1/-1,0"
  description: Pair tent on top with edge on bottom to form gem/snoopy.
color_mirror_algs:
  -
    alg: "samecase"

# RELATED CASES
parents:
  -
    name: "Left Snoopy / Gem"
    short_name: "lsnoopy_gem"
  -
    name: "Shell / Left Scottie"
    short_name: "shell_lscottie"
  -
    name: "Left Tent / Right Whale"
    short_name: "ltent_rwhale"
  -
    name: "Moth / Plane"
    short_name: "moth_plane"
mirrors:
  top_bot:
    -
      name: Left Kite / Right Pinwheel
      short_name: lkite_rpinwheel
  lr:
    -
      name: Left Pinwheel / Right Kite
      short_name: lpinwheel_rkite
  pseudo:
    -
      name: Left Pinwheel / Left Kite
      short_name: lpinwheel_lkite
    -
      name: Right Pinwheel / Right Kite
      short_name: rpinwheel_rkite


---

