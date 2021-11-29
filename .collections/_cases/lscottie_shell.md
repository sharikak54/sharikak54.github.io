---
title: "Case: Left Scottie / Shell"
name: Left Scottie / Shell
short_name: lscottie_shell
top: Scottie
top_short_name: scottie
top_lr: Left
bot: Shell
bot_short_name: shell

optimal: 3

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/-3,0/0,1"
  description: maximal blockbuild - pair shell on bottom with gem on top to get tent/tent
color_mirror_algs:
  -
    alg: "1,0/3,0/2,-1/0,1"
  -
    alg: "1,0/2,-1/3,0/0,1"
other_algs:
  -
    alg: "1,0/-1,2/3,0/0,1"
  -
    alg: "1,0/0,3/2,-1/0,1"
  -
    alg: "-5,6/3,0/-4,5/0,1"

# RELATED CASES
parents:
  -
    name: "Left Tent / Left Tent"
    short_name: "ltent_ltent"
mirrors:
  top_bot:
    -
      name: Shell / Left Scottie
      short_name: shell_lscottie
  lr:
    -
      name: Right Scottie / Shell
      short_name: rscottie_shell


---

