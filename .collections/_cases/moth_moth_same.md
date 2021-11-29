---
title: "Case: Same Moth / Moth"
name: Same Moth / Moth
short_name: moth_moth_same
top: Moth
top_short_name: moth
bot: Moth
bot_short_name: moth

optimal: 3

recognition: Matching moth moth; moths are of same colors.

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/2,2/0,1"
  description: Swap isolated corner with gem to go to m2.
color_mirror_algs:
  -
    alg: "1,0/-3,0/2,2/0,1"
  -
    alg: "3,2/-3,0/-2,-2/-1,0"
  -
    alg: "-3,-4/0,3/4,4/-1,0"
  -
    alg: "-5,6/0,3/-4,-4/0,1"
other_algs:
  -
    alg: "3,2/0,3/-2,-2/-1,0"
  -
    alg: "-3,-4/-3,0/4,4/-1,0"
  -
    alg: "-5,6/-3,0/-4,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Copp / Copp"
    short_name: "copp_copp"
---

Two Moths that are the same color.  Be careful not to mistake this for [Moth / Moth](moth_moth).

