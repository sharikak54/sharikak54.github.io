---
title: "Case: Right Scottie / Shell"
name: Right Scottie / Shell
short_name: rscottie_shell
top: Scottie
top_short_name: scottie
top_lr: Right
bot: Shell
bot_short_name: shell

optimal: 3

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/-3,0/-1,0"
  description: Pair shell on bottom with gem on top, such that slice goes between gem and neighboring isolated corner, to get good tents.
color_mirror_algs:
  -
    alg: "0,-1/4,1/3,0/-1,0"
  -
    alg: "0,-1/1,-2/-3,0/-1,0"
  -
    alg: "0,-1/0,-3/-2,1/-1,0"
  -
    alg: "6,5/-2,1/3,6/-1,0"
other_algs:
  -
    alg: "0,-1/-3,0/-2,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Tent / Right Tent"
    short_name: "rtent_rtent"
mirrors:
  top_bot:
    -
      name: Shell / Right Scottie
      short_name: shell_rscottie
  lr:
    -
      name: Left Scottie / Shell
      short_name: lscottie_shell


---

