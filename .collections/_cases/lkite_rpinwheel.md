---
title: "Case: Left Kite / Right Pinwheel"
name: Left Kite / Right Pinwheel
short_name: lkite_rpinwheel
top: Kite
top_short_name: kite
top_lr: Left
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Right

optimal: 4

recognition: Bad kite/pinwheel - aligning blocks to slice breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-1,5/-2,1/3,0/-1,0"
  description: Pair edge on top with tent on bottom to form axe/gem.
color_mirror_algs:
  -
    alg: "samecase"

# RELATED CASES
parents:
  -
    name: "Gem / Right Axe"
    short_name: "gem_raxe"
  -
    name: "Right Scottie / Shell"
    short_name: "rscottie_shell"
  -
    name: "Left Whale / Right Tent"
    short_name: "lwhale_rtent"
  -
    name: "Tree / Tie"
    short_name: "tree_tie"
mirrors:
  top_bot:
    -
      name: Right Pinwheel / Left Kite
      short_name: rpinwheel_lkite
  lr:
    -
      name: Right Kite / Left Pinwheel
      short_name: rkite_lpinwheel
  pseudo:
    -
      name: Right Kite / Right Pinwheel
      short_name: rkite_rpinwheel
    -
      name: Left Kite / Left Pinwheel
      short_name: lkite_lpinwheel


---

