---
title: "Case: Shell / Right Scottie"
name: Shell / Right Scottie
short_name: shell_rscottie
top: Shell
top_short_name: shell
bot: Scottie
bot_short_name: scottie
bot_lr: Right

optimal: 3

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/0,-3/-1,0"
  description: Pair shell on top with gem on bottom, such that slice goes between gem and neighboring isolated corner, to get tent/tent.
color_mirror_algs:
  -
    alg: "0,-1/1,-2/0,-3/-1,0"
  -
    alg: "0,-1/0,-3/1,-2/-1,0"
    alg: "0,-1/0,-3/1,-2/-1,0"
other_algs:
  -
    alg: "6,5/1,-2/6,3/-1,0"
# RELATED CASES
parents:
  -
    name: "Right Tent / Right Tent"
    short_name: "rtent_rtent"
mirrors:
  top_bot:
    -
      name: Right Scottie / Shell
      short_name: rscottie_shell
  lr:
    -
      name: Shell / Left Scottie
      short_name: shell_lscottie


---

