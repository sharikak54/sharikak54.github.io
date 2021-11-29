---
title: "Case: Plane / Plane"
name: Plane / Plane
short_name: plane_plane
top: Plane
top_short_name: plane
bot: Plane
bot_short_name: plane

optimal: 4

recognition: opposite plane/plane; planes are of different colors

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/-1,-1/3,6/0,1"
  description: hold D-layer shell in DL, and hold same-color corners in UL ("anti-CO") to go to good zero/kite; I prefer misaligning D-layer
color_mirror_algs:
  -
    alg: "0,-1/-2,1/-1,-1/-3,0/0,1"
  -
    alg: "1,0/2,-1/1,1/3,0/-1,0"
  -
    alg: "-5,6/-1,2/1,1/0,3/-1,0"
other_algs:
  -
    alg: "1,0/2,-1/1,1/-3,6/-1,0"
  -
    alg: "-5,6/-1,2/1,1/6,-3/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Zero / Right Kite"
    short_name: "lzero_rkite"
  -
    name: "Right Zero / Left Kite"
    short_name: "rzero_lkite"
---

