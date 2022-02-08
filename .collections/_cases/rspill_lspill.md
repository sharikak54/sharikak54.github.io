---
title: "Case: Right Spill / Left Spill"
name: Right Spill / Left Spill
short_name: rspill_lspill
top: Spill
top_short_name: spill
top_lr: Right
bot: Spill
bot_short_name: spill
bot_lr: Left

optimal: 4

recognition: Good spill/spill; swapping spills breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/3,0/-3,0/1,1/-1,0"
  description: Do CO into M2, make same trees with tent on top connecting with whale from bottom.
other_algs:
  -
    alg: "4,3/0,-3/0,3/-1,-1/0,1"
# RELATED CASES
parents:
  -
    name: "Same Tree / Tree"
    short_name: "tree_tree_same"
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
mirrors:
  lr:
    -
      name: Left Spill / Right Spill
      short_name: lspill_rspill
  pseudo:
    -
      name: Left Spill / Left Spill
      short_name: lspill_lspill
    -
      name: Right Spill / Right Spill
      short_name: rspill_rspill


---

