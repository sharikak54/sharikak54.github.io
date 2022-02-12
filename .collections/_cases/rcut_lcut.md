---
title: "Case: Right Cut / Left Cut"
name: Right Cut / Left Cut
short_name: rcut_lcut
top: Cut
top_short_name: cut
top_lr: Right
bot: Cut
bot_short_name: cut
bot_lr: Left

optimal: 6

recognition: Bad cuts; aligning birds breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/4,-2/3,0/-4,-1/-2,1/-3,0/-1,0"
  description: Preserve bird on bottom, send whale from top to form matching axe/axe; doing CO into 3E/3E is also decent.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "3,-1/0,-3/1,4/-1,-4/-3,0/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Axe / Right Axe"
    short_name: "raxe_raxe"
  -
    name: "3E / 3E"
    short_name: "3e_3e"
  -
    name: "3C / 3C"
    short_name: "3c_3c"
  -
    name: "Squid / Squid"
    short_name: "squid_squid"
  -
    name: "Hazard / Hazard"
    short_name: "hazard_hazard"
  -
    name: "Left Scottie / Left Scottie"
    short_name: "lscottie_lscottie"
mirrors:
  lr:
    -
      name: Left Cut / Right Cut
      short_name: lcut_rcut
  pseudo:
    -
      name: Left Cut / Left Cut
      short_name: lcut_lcut
    -
      name: Right Cut / Right Cut
      short_name: rcut_rcut


---

