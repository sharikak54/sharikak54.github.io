---
title: "Case: Left Pinwheel / Right Kite"
name: Left Pinwheel / Right Kite
short_name: lpinwheel_rkite
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Kite
bot_short_name: kite
bot_lr: Right

optimal: 4

recognition: Bad pinwheel/kite - aligning blocks to slice breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/-5,1/-3,0/2,-1/0,1"
  description: Pair tent on top with edge on bottom to form gem/snoopy.
color_mirror_algs:
  -
    alg: "samecase"

# RELATED CASES
parents:
  -
    name: "Right Snoopy / Gem"
    short_name: "rsnoopy_gem"
  -
    name: "Shell / Right Scottie"
    short_name: "shell_rscottie"
  -
    name: "Right Tent / Left Whale"
    short_name: "rtent_lwhale"
  -
    name: "Moth / Plane"
    short_name: "moth_plane"
mirrors:
  top_bot:
    -
      name: Right Kite / Left Pinwheel
      short_name: rkite_lpinwheel
  lr:
    -
      name: Right Pinwheel / Left Kite
      short_name: rpinwheel_lkite
  pseudo:
    -
      name: Right Pinwheel / Right Kite
      short_name: rpinwheel_rkite
    -
      name: Left Pinwheel / Left Kite
      short_name: lpinwheel_lkite


---

