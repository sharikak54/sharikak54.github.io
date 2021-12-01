---
title: "Case: Left Spill / Right Spill"
name: Left Spill / Right Spill
short_name: lspill_rspill
top: Spill
top_short_name: spill
top_lr: Left
bot: Spill
bot_short_name: spill
bot_lr: Right

optimal: 4

recognition: Good spill/spill; swapping spills breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/-3,0/-1,-1/0,1"
  description: Do CO into M2, make plane/plane with tent on top connecting with whale from bottom.
other_algs:
  -
    alg: "-3,-4/0,3/0,3/1,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Same Plane / Plane"
    short_name: "plane_plane_same"
  -
    name: "Right Scottie / Shell"
    short_name: "rscottie_shell"
mirrors:
  lr:
    -
      name: Right Spill / Left Spill
      short_name: rspill_lspill
  pseudo:
    -
      name: Right Spill / Right Spill
      short_name: rspill_rspill
    -
      name: Left Spill / Left Spill
      short_name: lspill_lspill


---

