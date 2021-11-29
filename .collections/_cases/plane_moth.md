---
title: "Case: Plane / Moth"
name: Plane / Moth
short_name: plane_moth
top: Plane
top_short_name: plane
bot: Moth
bot_short_name: moth

optimal: 3

recognition: Good plane/moth - color of plane and moth are swapped.

# ALGORITHMS
default_alg:
  alg: "1,0/-1,2/-5,-2/-1,0"
  description: Swap isolated edge on top with isolated corner on bottom.
color_mirror_algs:
  -
    alg: "1,0/-1,2/1,4/-1,0"
  -
    alg: "0,2/1,-2/-1,-4/0,1"
other_algs:
  -
    alg: "0,2/1,-2/5,2/0,1"
  -
    alg: "-5,6/2,-1/1,4/-1,0"
  -
    alg: "6,-4/-2,1/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Left Dish / Left Dish"
    short_name: "ldish_ldish"
  -
    name: "Right Dish / Right Dish"
    short_name: "rdish_rdish"
mirrors:
  top_bot:
    -
      name: Moth / Plane
      short_name: moth_plane


---

