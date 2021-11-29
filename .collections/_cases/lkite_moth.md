---
title: "Case: Left Kite / Moth"
name: Left Kite / Moth
short_name: lkite_moth
top: Kite
top_short_name: kite
top_lr: Left
bot: Moth
bot_short_name: moth

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/1,-2/-1,2/3,0/0,1"
  description: preserve gem on bottom and pair tent from top to form scottie/shell
color_mirror_algs:
  -
    alg: "0,-1/1,-2/-1,2/-3,6/0,1"
  -
    alg: "0,-1/1,-2/0,3/-4,5/0,1"
  -
    alg: "6,5/-2,1/-1,2/6,-3/0,1"
  -
    alg: "6,5/-2,1/0,3/5,-4/0,1"
  -
    alg: "-5,0/3,0/0,-3/-1,-4/0,1"
  -
    alg: "1,6/0,3/0,-3/-4,-1/0,1"
other_algs:
  -
    alg: "0,-1/1,-2/0,3/2,-1/0,1"
  -
    alg: "6,5/-2,1/-1,2/0,3/0,1"
  -
    alg: "6,5/-2,1/0,3/-1,2/0,1"
  -
    alg: "-5,0/3,0/0,-3/5,2/0,1"
  -
    alg: "1,6/0,3/0,-3/2,5/0,1"

# RELATED CASES
parents:
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
  -
    name: "Left Bird / Right Scottie"
    short_name: "lbird_rscottie"
mirrors:
  top_bot:
    -
      name: Moth / Left Kite
      short_name: moth_lkite
  lr:
    -
      name: Right Kite / Moth
      short_name: rkite_moth


---

