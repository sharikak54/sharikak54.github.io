---
title: "Case: Tie / Right Kite"
name: Tie / Right Kite
short_name: tie_rkite
top: Tie
top_short_name: tie
bot: Kite
bot_short_name: kite
bot_lr: Right

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/2,-1/-2,1/0,-3/-1,0"
  description: Preserve gem on top and pair tent from bottom to form shell/scottie.
color_mirror_algs:
  -
    alg: "1,0/2,-1/-2,1/6,3/-1,0"
  -
    alg: "1,0/2,-1/-3,0/-5,4/-1,0"
  -
    alg: "-5,6/-1,2/-2,1/3,6/-1,0"
  -
    alg: "-5,6/-1,2/-3,0/4,-5/-1,0"
  -
    alg: "6,-1/-3,0/3,0/1,4/-1,0"
  -
    alg: "0,5/0,-3/3,0/4,1/-1,0"
other_algs:
  -
    alg: "1,0/2,-1/-3,0/1,-2/-1,0"
  -
    alg: "-5,6/-1,2/-2,1/-3,0/-1,0"
  -
    alg: "-5,6/-1,2/-3,0/-2,1/-1,0"
  -
    alg: "6,-1/-3,0/3,0/-2,-5/-1,0"
  -
    alg: "0,5/0,-3/3,0/-5,-2/-1,0"

# RELATED CASES
parents:
  -
    name: "Shell / Right Scottie"
    short_name: "shell_rscottie"
  -
    name: "Left Scottie / Right Bird"
    short_name: "lscottie_rbird"
mirrors:
  top_bot:
    -
      name: Right Kite / Tie
      short_name: rkite_tie
  lr:
    -
      name: Tie / Left Kite
      short_name: tie_lkite


---

