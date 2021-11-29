---
title: "Case: Left Snoopy / Right Snoopy"
name: Left Snoopy / Right Snoopy
short_name: lsnoopy_rsnoopy
top: Snoopy
top_short_name: snoopy
top_lr: Left
bot: Snoopy
bot_short_name: snoopy
bot_lr: Right

optimal: 5

recognition: Mirrored snoopies; tents can't connect to form kites.

# ALGORITHMS
default_alg:
  alg: "1,0/2,-1/-2,1/-1,-1/-3,0/0,1"
  description: Swap isolated edge on top with tent on bottom, forming opposite plane/plane.
color_mirror_algs:
  -
    alg: ""
other_algs:
  -
    alg: "0,-1/3,0/-2,1/-1,-1/-3,0/0,1"
  -
    alg: "-2,0/-4,-1/-2,1/-4,-1/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Plane / Plane"
    short_name: "plane_plane"
  -
    name: "Gem / Right Spill"
    short_name: "gem_rspill"
  -
    name: "Moth / Left Kite"
    short_name: "moth_lkite"
  -
    name: "Angel / Right Spill"
    short_name: "angel_rspill"
  -
    name: "Moth / Right Zero"
    short_name: "moth_rzero"
mirrors:
  lr:
    -
      name: Right Snoopy / Left Snoopy
      short_name: rsnoopy_lsnoopy
  pseudo:
    -
      name: Right Snoopy / Right Snoopy
      short_name: rsnoopy_rsnoopy
    -
      name: Left Snoopy / Left Snoopy
      short_name: lsnoopy_lsnoopy


---

