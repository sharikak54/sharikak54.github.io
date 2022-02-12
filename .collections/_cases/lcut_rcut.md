---
title: "Case: Left Cut / Right Cut"
name: Left Cut / Right Cut
short_name: lcut_rcut
top: Cut
top_short_name: cut
top_lr: Left
bot: Cut
bot_short_name: cut
bot_lr: Right

optimal: 6

recognition: Bad cuts; aligning birds breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-4,2/-3,0/4,1/3,0/2,-1/0,1"
  description: Preserve bird on bottom, send whale from top to form matching axe/axe; doing CO into 3E/3E is also decent.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "-2,0/0,3/-1,-4/1,4/3,0/-4,-1/0,1"
  -
    alg: "-2,0/0,3/3,0/3,0/-1,-1/-3,0/-3,0/0,1"

# RELATED CASES
parents:
  -
    name: "Left Axe / Left Axe"
    short_name: "laxe_laxe"
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
    name: "Right Scottie / Right Scottie"
    short_name: "rscottie_rscottie"
mirrors:
  lr:
    -
      name: Right Cut / Left Cut
      short_name: rcut_lcut
  pseudo:
    -
      name: Right Cut / Right Cut
      short_name: rcut_rcut
    -
      name: Left Cut / Left Cut
      short_name: lcut_lcut


---

