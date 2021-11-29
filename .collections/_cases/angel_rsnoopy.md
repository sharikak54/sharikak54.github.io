---
title: "Case: Angel / Right Snoopy"
name: Angel / Right Snoopy
short_name: angel_rsnoopy
top: Angel
top_short_name: angel
bot: Snoopy
bot_short_name: snoopy
bot_lr: Right

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/2,-1/4,1/-1,0"
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
    name: "Right Snoopy / Right Spill"
    short_name: "rsnoopy_rspill"
  -
    name: "Right Baron / Right Baron"
    short_name: "rbaron_rbaron"
mirrors:
  top_bot:
    -
      name: Right Snoopy / Angel
      short_name: rsnoopy_angel
  lr:
    -
      name: Angel / Left Snoopy
      short_name: angel_lsnoopy


---

