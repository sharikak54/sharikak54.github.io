---
title: "Case: Angel / Left Snoopy"
name: Angel / Left Snoopy
short_name: angel_lsnoopy
top: Angel
top_short_name: angel
bot: Snoopy
bot_short_name: snoopy
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/-2,1/-4,-1/0,1"
  description: Put shell on bottom in DL, pair tent on bottom with whale on top to form good moth/plane.
color_mirror_algs:
  -
    alg: ""

# RELATED CASES
parents:
  -
    name: "Moth / Plane"
    short_name: "moth_plane"
  -
    name: "Left Snoopy / Left Spill"
    short_name: "lsnoopy_lspill"
  -
    name: "Left Baron / Left Baron"
    short_name: "lbaron_lbaron"
mirrors:
  top_bot:
    -
      name: Left Snoopy / Angel
      short_name: lsnoopy_angel
  lr:
    -
      name: Angel / Right Snoopy
      short_name: angel_rsnoopy


---

