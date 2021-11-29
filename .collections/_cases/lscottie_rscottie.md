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

recognition: mirrored scotties; tents can't connect to form kites

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/0,3/2,-1/-3,0/0,1"
  description: create a yellow (D-color) shell on bottom (as part of a plane) by pairing isolated yellow corner on top with yellow tent on bottom
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
    name: "Left Kite / Plane"
    short_name: "lkite_plane"
  -
    name: "Left Bird / Hazard"
    short_name: "lbird_hazard"
  -
    name: "Left Bird / Shell"
    short_name: "lbird_shell"
  -
    name: "Left Zero / Plane"
    short_name: "lzero_plane"
  -
    name: "Moth / Moth"
    short_name: "moth_moth"
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

