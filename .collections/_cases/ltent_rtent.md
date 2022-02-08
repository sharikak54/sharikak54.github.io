---
title: "Case: Left Tent / Right Tent"
name: Left Tent / Right Tent
short_name: ltent_rtent
top: Tent
top_short_name: tent
top_lr: Left
bot: Tent
bot_short_name: tent
bot_lr: Right

optimal: 4

recognition: Bad tent/tent; aligning tents next to slice breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/2,-1/3,0/0,1"
  description: Keep top tent on left with edge next to slice, send gem from bottom to form scottie/shell.
other_algs:
  -
    alg: "3,-1/-2,1/-3,0/2,-1/0,1"
  -
    alg: "3,-1/-2,1/-1,2/0,-3/0,1"
    alg: "3,-1/-2,1/-1,2/0,-3/0,1"

# RELATED CASES
parents:
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
  -
    name: "Gem / Left Axe"
    short_name: "gem_laxe"
  -
    name: "Gem / Left Axe"
    short_name: "gem_laxe"
mirrors:
  lr:
    -
      name: Right Tent / Left Tent
      short_name: rtent_ltent
  pseudo:
    -
      name: Right Tent / Right Tent
      short_name: rtent_rtent
    -
      name: Left Tent / Left Tent
      short_name: ltent_ltent


---

