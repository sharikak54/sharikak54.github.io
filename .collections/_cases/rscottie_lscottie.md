---
title: "Case: Right Scottie / Left Scottie"
name: Right Scottie / Left Scottie
short_name: rscottie_lscottie
top: Scottie
top_short_name: scottie
top_lr: Right
bot: Scottie
bot_short_name: scottie
bot_lr: Left

optimal: 5

recognition: Mirrored scotties; tents can't connect to form kites.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/0,-3/-2,1/3,0/-1,0"
  description: Create a D-color shell on bottom (as part of a tree) by pairing isolated D-color corner on top with D-color tent on bottom.
color_mirror_algs:
  -
    alg: "1,0/-1,-4/-2,1/2,-1/-3,0/0,1"
  -
    alg: "-3,-4/0,-3/0,-3/1,-2/3,0/-1,0"
other_algs:
  -
    alg: "4,3/0,3/3,0/-3,0/2,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Right Kite / Tree"
    short_name: "rkite_tree"
  -
    name: "Right Bird / Hazard"
    short_name: "rbird_hazard"
  -
    name: "Right Bird / Shell"
    short_name: "rbird_shell"
  -
    name: "Right Cut / Tree"
    short_name: "rcut_tree"
  -
    name: "Tie / Tie"
    short_name: "tie_tie"
mirrors:
  lr:
    -
      name: Left Scottie / Right Scottie
      short_name: lscottie_rscottie
  pseudo:
    -
      name: Left Scottie / Left Scottie
      short_name: lscottie_lscottie
    -
      name: Right Scottie / Right Scottie
      short_name: rscottie_rscottie


---

