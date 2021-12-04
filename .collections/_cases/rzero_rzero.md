---
title: "Case: Right Zero / Right Zero"
name: Right Zero / Right Zero
short_name: rzero_rzero
top: Zero
top_short_name: zero
top_lr: Right
bot: Zero
bot_short_name: zero
bot_lr: Right

optimal: 3

recognition: Good zero/zero; aligning birds preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,3/-1,-1/0,1"
  description: Solve CO into M2.
color_mirror_algs:
  -
    alg: "samecase"

# RELATED CASES
parents:
  -
    name: "Eopp / Eopp"
    short_name: "eopp_eopp"
  -
    name: "Copp / Copp"
    short_name: "copp_copp"
  -
    name: "Right Pinwheel / Right Pinwheel"
    short_name: "rpinwheel_rpinwheel"
mirrors:
  lr:
    -
      name: Left Zero / Left Zero
      short_name: lzero_lzero
  pseudo:
    -
      name: Left Zero / Right Zero
      short_name: lzero_rzero
    -
      name: Right Zero / Left Zero
      short_name: rzero_lzero


---

