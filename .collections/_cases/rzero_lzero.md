---
title: "Case: Right Zero / Left Zero"
name: Right Zero / Left Zero
short_name: rzero_lzero
top: Zero
top_short_name: zero
top_lr: Right
bot: Zero
bot_short_name: zero
bot_lr: Left

optimal: 6

recognition: Bad zero/zero; aligning birds breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/4,-2/3,0/-4,-1/-2,1/-3,0/-1,0"
  description: Preserve bird on bottom, send whale from top to form matching snoopy/snoopy; doing CO into 3E/3E is also decent.
other_algs:
  -
    alg: "3,-1/0,-3/1,4/-1,-4/-3,0/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Snoopy / Right Snoopy"
    short_name: "rsnoopy_rsnoopy"
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
    name: "Left Scottie / Left Scottie"
    short_name: "lscottie_lscottie"
mirrors:
  lr:
    -
      name: Left Zero / Right Zero
      short_name: lzero_rzero
  pseudo:
    -
      name: Left Zero / Left Zero
      short_name: lzero_lzero
    -
      name: Right Zero / Right Zero
      short_name: rzero_rzero


---

