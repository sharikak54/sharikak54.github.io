---
title: "Case: Right Cut / Tie"
name: Right Cut / Tie
short_name: rcut_tie
top: Cut
top_short_name: cut
top_lr: Right
bot: Tie
bot_short_name: tie

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-4/0,3/4,1/-1,0"
  description: Pair isolated corner on top with tent on bottom (breaking gem) to form good scottie/bird.
color_mirror_algs:
  -
    alg: "1,0/5,2/3,0/4,1/-1,0"
  -
    alg: "1,0/-1,-4/0,3/-2,-5/-1,0"
  -
    alg: "-5,6/-4,-1/0,3/-5,-2/-1,0"
  -
    alg: "-2,3/-3,3/0,-3/-1,2/0,3/0,1"
  -
    alg: "-2,3/2,-4/3,0/-2,1/-3,0/-1,0"
  -
    alg: "-2,3/3,-3/-3,0/-4,-1/-3,0/0,1"
    alg: "1,0/-1,-4/0,3/-2,-5/-1,0"
  -
    alg: "-5,6/-4,-1/0,3/-5,-2/-1,0"
  -
    alg: "-2,3/-3,3/0,-3/-1,2/0,3/0,1"
  -
    alg: "-2,3/2,-4/3,0/-2,1/-3,0/-1,0"
  -
    alg: "-2,3/3,-3/-3,0/-4,-1/-3,0/0,1"
other_algs:
  -
    alg: "-5,6/-4,-1/0,3/1,4/-1,0"
  -
    alg: "-2,3/-3,3/0,-3/-1,2/6,-3/0,1"
  -
    alg: "4,-3/-3,3/-3,0/2,-1/3,0/0,1"
    alg: "-2,3/-3,3/0,-3/-1,2/6,-3/0,1"
  -
    alg: "4,-3/-3,3/-3,0/2,-1/3,0/0,1"

# RELATED CASES
parents:
  -
    name: "Left Scottie / Right Bird"
    short_name: "lscottie_rbird"
mirrors:
  top_bot:
    -
      name: Tie / Right Cut
      short_name: tie_rcut
  lr:
    -
      name: Left Cut / Tie
      short_name: lcut_tie


---

