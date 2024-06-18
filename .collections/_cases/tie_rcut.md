---
title: "Case: Tie / Right Cut"
name: Tie / Right Cut
short_name: tie_rcut
top: Tie
top_short_name: tie
bot: Cut
bot_short_name: cut
bot_lr: Right

optimal: 4

recognition: 0,-1/-2,1/-4,-1/0,1 -2,0/2,-1/4,1/-1,0

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/3,0/1,4/-1,0"
  description: Pair isolated corner on bottom with tent on top (breaking gem) to form good bird/scottie.
color_mirror_algs:
  -
    alg: "1,0/-4,-1/3,0/-5,-2/-1,0"
  -
    alg: "-5,6/-1,-4/3,0/-2,-5/-1,0"
  -
    alg: "-5,6/5,2/0,3/4,1/-1,0"
  -
    alg: "4,-3/3,-3/-3,0/3,0/2,-1/0,1"
  -
    alg: "4,-3/-3,3/0,-3/2,-1/0,3/0,1"
other_algs:
  -
    alg: "-5,6/-1,-4/3,0/4,1/-1,0"
  -
    alg: "4,-3/3,-3/-3,0/2,-1/-3,6/0,1"
  -
    alg: "-2,3/-3,3/-3,0/-4,-1/-3,0/0,1"
  -
    alg: "-2,3/-3,3/-3,0/0,3/2,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Right Bird / Left Scottie"
    short_name: "rbird_lscottie"
mirrors:
  top_bot:
    -
      name: Right Cut / Tie
      short_name: rcut_tie
  lr:
    -
      name: Tie / Left Cut
      short_name: tie_lcut


---

