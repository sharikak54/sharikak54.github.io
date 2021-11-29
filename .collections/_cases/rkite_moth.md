---
title: "Case: Right Kite / Moth"
name: Right Kite / Moth
short_name: rkite_moth
top: Kite
top_short_name: kite
top_lr: Right
bot: Moth
bot_short_name: moth

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-1,2/1,-2/-3,0/-1,0"
  description: Preserve gem on bottom and pair tent from top to form scottie/shell.
color_mirror_algs:
  -
    alg: "1,0/-1,2/1,-2/3,6/-1,0"
  -
    alg: "1,0/-1,2/4,1/-3,6/-1,0"
  -
    alg: "-5,6/2,-1/1,-2/6,3/-1,0"
  -
    alg: "-5,6/2,-1/4,1/6,-3/-1,0"
  -
    alg: "6,-1/-3,0/0,3/1,4/-1,0"
  -
    alg: "0,5/0,-3/0,3/4,1/-1,0"
other_algs:
  -
    alg: "1,0/-1,2/4,1/3,0/-1,0"
  -
    alg: "-5,6/2,-1/1,-2/0,-3/-1,0"
  -
    alg: "-5,6/2,-1/4,1/0,3/-1,0"
  -
    alg: "6,-1/-3,0/0,3/-5,-2/-1,0"
  -
    alg: "0,5/0,-3/0,3/-2,-5/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Scottie / Shell"
    short_name: "rscottie_shell"
  -
    name: "Left Bird / Left Scottie"
    short_name: "lbird_lscottie"
mirrors:
  top_bot:
    -
      name: Moth / Right Kite
      short_name: moth_rkite
  lr:
    -
      name: Left Kite / Moth
      short_name: lkite_moth


---

