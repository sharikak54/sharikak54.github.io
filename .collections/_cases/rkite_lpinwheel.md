---
title: "Case: Right Kite / Left Pinwheel"
name: Right Kite / Left Pinwheel
short_name: rkite_lpinwheel
top: Kite
top_short_name: kite
top_lr: Right
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Left

optimal: 4

recognition: Bad kite/pinwheel - aligning blocks to slice breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,-5/2,-1/-3,0/0,1"
  description: Pair edge on top with tent on bottom to form axe/gem.
color_mirror_algs:
  -
    alg: "samecase"

# RELATED CASES
parents:
  -
    name: "Gem / Left Axe"
    short_name: "gem_laxe"
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
  -
    name: "Right Whale / Left Tent"
    short_name: "rwhale_ltent"
  -
    name: "Tree / Tie"
    short_name: "tree_tie"
mirrors:
  top_bot:
    -
      name: Left Pinwheel / Right Kite
      short_name: lpinwheel_rkite
  lr:
    -
      name: Left Kite / Right Pinwheel
      short_name: lkite_rpinwheel
  pseudo:
    -
      name: Left Kite / Left Pinwheel
      short_name: lkite_lpinwheel
    -
      name: Right Kite / Right Pinwheel
      short_name: rkite_rpinwheel


---

