---
title: "Case: Same Plane / Plane"
name: Same Plane / Plane
short_name: plane_plane_same
top: Plane
top_short_name: plane
bot: Plane
bot_short_name: plane

optimal: 3

recognition: Matching plane/plane; planes are the same color.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/-1,-1/0,1"
  description: Solve CO into M2.
color_mirror_algs:
  -
    alg: "1,0/0,3/-1,-1/0,1"
  -
    alg: "0,-1/0,3/1,1/-1,0"
other_algs:
  -
    alg: "0,-1/-3,0/1,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Eopp / Eopp"
    short_name: "eopp_eopp"
---

Two Planes that are the same color.  Be careful not to mistake this for [Plane / Plane](plane_plane).

