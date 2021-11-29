---
title: "Case: Moth / Plane"
name: Moth / Plane
short_name: moth_plane
top: Moth
top_short_name: moth
bot: Plane
bot_short_name: plane

optimal: 3

recognition: Good moth/plane - color of moth and plane are swapped.

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/2,5/0,1"
  description: Swap isolated corner on top with isolated edge on bottom.
color_mirror_algs:
  -
    alg: "0,-1/-2,1/-4,-1/0,1"
  -
    alg: "-2,0/2,-1/4,1/-1,0"
other_algs:
  -
    alg: "-2,0/2,-1/-2,-5/-1,0"
  -
    alg: "6,5/1,-2/-4,-1/0,1"
  -
    alg: "4,6/-2,1/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Dish / Right Dish"
    short_name: "rdish_rdish"
  -
    name: "Left Dish / Left Dish"
    short_name: "ldish_ldish"
mirrors:
  top_bot:
    -
      name: Plane / Moth
      short_name: plane_moth


---

