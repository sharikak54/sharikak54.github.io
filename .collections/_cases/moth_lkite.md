---
title: "Case: Moth / Left Kite"
name: Moth / Left Kite
short_name: moth_lkite
top: Moth
top_short_name: moth
bot: Kite
bot_short_name: kite
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/2,-1/0,3/0,1"
  description: Preserve gem on top and pair tent from bottom to form shell/scottie.
color_mirror_algs:
  -
    alg: "0,-1/-2,1/2,-1/6,-3/0,1"
  -
    alg: "0,-1/-2,1/3,0/5,-4/0,1"
  -
    alg: "6,5/1,-2/3,0/-4,5/0,1"
  -
    alg: "6,5/1,-2/2,-1/-3,6/0,1"
  -
    alg: "-5,0/3,0/-3,0/-1,-4/0,1"
  -
    alg: "1,6/0,3/-3,0/-4,-1/0,1"
other_algs:
  -
    alg: "0,-1/-2,1/3,0/-1,2/0,1"
  -
    alg: "6,5/1,-2/3,0/2,-1/0,1"
  -
    alg: "6,5/1,-2/2,-1/3,0/0,1"
  -
    alg: "-5,0/3,0/-3,0/5,2/0,1"
  -
    alg: "1,6/0,3/-3,0/2,5/0,1"

# RELATED CASES
parents:
  -
    name: "Shell / Left Scottie"
    short_name: "shell_lscottie"
  -
    name: "Right Scottie / Left Bird"
    short_name: "rscottie_lbird"
mirrors:
  top_bot:
    -
      name: Left Kite / Moth
      short_name: lkite_moth
  lr:
    -
      name: Moth / Right Kite
      short_name: moth_rkite


---

