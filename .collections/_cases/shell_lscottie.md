---
title: "Case: Shell / Left Scottie"
name: Shell / Left Scottie
short_name: shell_lscottie
top: Shell
top_short_name: shell
bot: Scottie
bot_short_name: scottie
bot_lr: Left

optimal: 3

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/2,-1/0,3/0,1"
  description: Pair shell on top with gem on bottom, such that slice goes between gem and neighboring isolated corner, to get tent/tent.
color_mirror_algs:
  -
    alg: "1,0/-1,2/0,3/0,1"
  -
    alg: "1,0/0,3/-1,2/0,1"
other_algs:
  -
    alg: "-5,6/-1,2/6,-3/0,1"

# RELATED CASES
parents:
  -
    name: "Left Tent / Left Tent"
    short_name: "ltent_ltent"
mirrors:
  top_bot:
    -
      name: Left Scottie / Shell
      short_name: lscottie_shell
  lr:
    -
      name: Shell / Right Scottie
      short_name: shell_rscottie


---

