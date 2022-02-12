---
title: "Case: Tie / Tie"
name: Tie / Tie
short_name: tie_tie
top: Tie
top_short_name: tie
bot: Tie
bot_short_name: tie

optimal: 4

recognition: Opposite ties; ties are of different colors.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,-2/-1,-1/-3,0/0,1"
  description: Make kite on bottom from pairing gem on top with matching isolated corner.
color_mirror_algs:
  -
    alg: "0,-1/1,-2/-1,-1/3,6/0,1"
  -
    alg: "1,0/0,-3/-1,-1/3,6/0,1"
  -
    alg: "-2,-3/-1,2/1,1/-3,6/-1,0"
  -
    alg: "-3,-4/0,3/1,1/-3,6/-1,0"
other_algs:
  -
    alg: "1,0/0,-3/-1,-1/-3,0/0,1"
  -
    alg: "-2,-3/-1,2/1,1/3,0/-1,0"
  -
    alg: "-3,-4/0,3/1,1/3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Cut / Right Kite"
    short_name: "lcut_rkite"
  -
    name: "Right Cut / Left Kite"
    short_name: "rcut_lkite"
---

