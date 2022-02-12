---
title: "Case: Left Cut / Tie"
name: Left Cut / Tie
short_name: lcut_tie
top: Cut
top_short_name: cut
top_lr: Left
bot: Tie
bot_short_name: tie

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/1,4/0,-3/-4,-1/0,1"
  description: Pair isolated corner on top with tent on bottom (breaking gem) to form good scottie/bird.
color_mirror_algs:
  -
    alg: "0,-1/-5,-2/-3,0/-4,-1/0,1"
  -
    alg: "0,-1/1,4/0,-3/2,5/0,1"
  -
    alg: "6,5/4,1/0,-3/5,2/0,1"
  -
    alg: "3,-4/-2,4/-3,0/3,0/2,-1/0,1"
  -
    alg: "3,-4/-3,3/3,0/1,-2/-3,0/-1,0"
other_algs:
  -
    alg: "6,5/4,1/0,-3/-1,-4/0,1"
  -
    alg: "3,-4/-2,4/-3,0/3,0/-4,5/0,1"
  -
    alg: "-3,2/3,-3/3,0/-2,1/-3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Scottie / Left Bird"
    short_name: "rscottie_lbird"
mirrors:
  top_bot:
    -
      name: Tie / Left Cut
      short_name: tie_lcut
  lr:
    -
      name: Right Cut / Tie
      short_name: rcut_tie


---

