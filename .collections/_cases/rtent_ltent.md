---
title: "Case: Right Tent / Left Tent"
name: Right Tent / Left Tent
short_name: rtent_ltent
top: Tent
top_short_name: tent
top_lr: Right
bot: Tent
bot_short_name: tent
bot_lr: Left

optimal: 4

recognition: Bad tent/tent; aligning tents next to slice breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/2,-1/-2,1/-3,0/-1,0"
  description: Keep top tent on left with edge next to slice, send gem from bottom to form scottie/shell.
other_algs:
  -
    alg: "1,0/2,-1/-3,0/-2,1/-1,0"
  -
    alg: "-2,0/2,-1/1,-2/0,3/-1,0"
  -
    alg: "-2,0/2,-1/3,0/-2,1/-1,0"
    alg: "-2,0/2,-1/1,-2/0,3/-1,0"
  -
    alg: "-2,0/2,-1/3,0/-2,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Scottie / Shell"
    short_name: "rscottie_shell"
  -
    name: "Gem / Right Axe"
    short_name: "gem_raxe"
  -
    name: "Gem / Right Axe"
    short_name: "gem_raxe"
mirrors:
  lr:
    -
      name: Left Tent / Right Tent
      short_name: ltent_rtent
  pseudo:
    -
      name: Left Tent / Left Tent
      short_name: ltent_ltent
    -
      name: Right Tent / Right Tent
      short_name: rtent_rtent


---

