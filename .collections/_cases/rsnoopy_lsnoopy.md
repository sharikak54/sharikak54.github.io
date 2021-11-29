---
title: "Case: Right Snoopy / Left Snoopy"
name: Right Snoopy / Left Snoopy
short_name: rsnoopy_lsnoopy
top: Snoopy
top_short_name: snoopy
top_lr: Right
bot: Snoopy
bot_short_name: snoopy
bot_lr: Left

optimal: 5

recognition: Mirrored snoopies; tents can't connect to form kites.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/-2,1/-1,-1/-3,0/0,1"
  description: Swap isolated edge on top with tent on bottom, forming opposite plane/plane.
color_mirror_algs:
  -
    alg: ""
other_algs:
  -
    alg: "1,0/-4,-1/-2,1/-1,-1/-3,0/0,1"
  -
    alg: "3,-1/4,1/2,-1/4,1/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Plane / Plane"
    short_name: "plane_plane"
  -
    name: "Gem / Left Spill"
    short_name: "gem_lspill"
  -
    name: "Moth / Right Kite"
    short_name: "moth_rkite"
  -
    name: "Angel / Left Spill"
    short_name: "angel_lspill"
  -
    name: "Moth / Left Zero"
    short_name: "moth_lzero"
mirrors:
  lr:
    -
      name: Left Snoopy / Right Snoopy
      short_name: lsnoopy_rsnoopy
  pseudo:
    -
      name: Left Snoopy / Left Snoopy
      short_name: lsnoopy_lsnoopy
    -
      name: Right Snoopy / Right Snoopy
      short_name: rsnoopy_rsnoopy


---

