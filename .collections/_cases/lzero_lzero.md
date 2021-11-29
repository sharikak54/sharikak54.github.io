---
title: "Case: Left Zero / Left Zero"
name: Left Zero / Left Zero
short_name: lzero_lzero
top: Zero
top_short_name: zero
top_lr: Left
bot: Zero
bot_short_name: zero
bot_lr: Left

optimal: 3

recognition: Good zero/zero; aligning birds preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,4/-1,-1/0,1"
  description: Solve CO into M2.
other_algs:
  -
    alg: "0,-1/-3,3/1,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Eopp / Eopp"
    short_name: "eopp_eopp"
  -
    name: "Copp / Copp"
    short_name: "copp_copp"
  -
    name: "Left Pinwheel / Left Pinwheel"
    short_name: "lpinwheel_lpinwheel"
mirrors:
  lr:
    -
      name: Right Zero / Right Zero
      short_name: rzero_rzero
  pseudo:
    -
      name: Right Zero / Left Zero
      short_name: rzero_lzero
    -
      name: Left Zero / Right Zero
      short_name: lzero_rzero


---

