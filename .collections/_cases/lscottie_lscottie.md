---
title: "Case: Left Scottie / Left Scottie"
name: Left Scottie / Left Scottie
short_name: lscottie_lscottie
top: Scottie
top_short_name: scottie
top_lr: Left
bot: Scottie
bot_short_name: scottie
bot_lr: Left

optimal: 5

recognition: Matching scotties; tents can connect to form kites.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,-2/-4,-1/3,0/-2,1/-1,0"
  description: Create a D-color shell on bottom by pairing isolated D-color corner on top with D-color tent on bottom.
color_mirror_algs:
  -
    alg: "0,-1/0,3/4,1/-3,0/2,-1/0,1"
# RELATED CASES
parents:
  -
    name: "Shell / Shell"
    short_name: "shell_shell"
mirrors:
  lr:
    -
      name: Right Scottie / Right Scottie
      short_name: rscottie_rscottie
  pseudo:
    -
      name: Right Scottie / Left Scottie
      short_name: rscottie_lscottie
    -
      name: Left Scottie / Right Scottie
      short_name: lscottie_rscottie


---

