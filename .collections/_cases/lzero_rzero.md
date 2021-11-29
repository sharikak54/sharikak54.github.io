---
title: "Case: Left Zero / Right Zero"
name: Left Zero / Right Zero
short_name: lzero_rzero
top: Zero
top_short_name: zero
top_lr: Left
bot: Zero
bot_short_name: zero
bot_lr: Right

optimal: 6

recognition: Bad zero/zero; aligning birds breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-4,2/-3,0/4,1/3,0/2,-1/0,1"
  description: Preserve bird on bottom, send whale from top to form matching snoopy/snoopy; doing CO into 3E/3E is also decent.
other_algs:
  -
    alg: "-2,0/0,3/-1,-4/1,4/3,0/-4,-1/0,1"
  -
    alg: "-2,0/0,3/3,0/..."

# RELATED CASES
parents:
  -
    name: "Left Snoopy / Left Snoopy"
    short_name: "lsnoopy_lsnoopy"
  -
    name: "3E / 3E"
    short_name: "3e_3e"
  -
    name: "3C / 3C"
    short_name: "3c_3c"
  -
    name: "Angel / Angel"
    short_name: "angel_angel"
  -
    name: "Hazard / Hazard"
    short_name: "hazard_hazard"
  -
    name: "Right Scottie / Right Scottie"
    short_name: "rscottie_rscottie"
mirrors:
  lr:
    -
      name: Right Zero / Left Zero
      short_name: rzero_lzero
  pseudo:
    -
      name: Right Zero / Right Zero
      short_name: rzero_rzero
    -
      name: Left Zero / Left Zero
      short_name: lzero_lzero


---

