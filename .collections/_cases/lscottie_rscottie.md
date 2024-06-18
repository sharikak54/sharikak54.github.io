---
title: "Case: Left Scottie / Right Scottie"
name: Left Scottie / Right Scottie
short_name: lscottie_rscottie
top: Scottie
top_short_name: scottie
top_lr: Left
bot: Scottie
bot_short_name: scottie
bot_lr: Right

optimal: 5

recognition: Mirrored scotties; tents can't connect to form kites.

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/0,3/2,-1/-3,0/0,1"
  description: Create a D-color shell on bottom (as part of a tree) by pairing isolated D-color corner on top with D-color tent on bottom.
color_mirror_algs:
  -
    alg: "0,-1/1,4/2,-1/-2,1/3,0/-1,0"
  -
    alg: "4,-3/0,3/0,3/-1,2/-3,0/0,1"
other_algs:
  -
    alg: "-3,-4/0,-3/-3,0/3,0/-2,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Kite / Tree"
    short_name: "lkite_tree"
  -
    name: "Left Bird / Hazard"
    short_name: "lbird_hazard"
  -
    name: "Left Bird / Shell"
    short_name: "lbird_shell"
  -
    name: "Left Cut / Tree"
    short_name: "lcut_tree"
  -
    name: "Tie / Tie"
    short_name: "tie_tie"
mirrors:
  lr:
    -
      name: Right Scottie / Left Scottie
      short_name: rscottie_lscottie
  pseudo:
    -
      name: Right Scottie / Right Scottie
      short_name: rscottie_rscottie
    -
      name: Left Scottie / Left Scottie
      short_name: lscottie_lscottie


---

