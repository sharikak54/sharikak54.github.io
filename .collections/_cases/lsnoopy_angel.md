---
title: "Case: Left Snoopy / Angel"
name: Left Snoopy / Angel
short_name: lsnoopy_angel
top: Snoopy
top_short_name: snoopy
top_lr: Left
bot: Angel
bot_short_name: angel

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/0,-3/1,-2/-1,-4/0,1"
  description: Put shell on top in UL, pair tent on top with whale on bottom to form good plane/moth.
color_mirror_algs:
  -
    alg: ""
other_algs:
  -
    alg: "6,5/-3,0/1,-2/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Plane / Moth"
    short_name: "plane_moth"
  -
    name: "Left Spill / Left Snoopy"
    short_name: "lspill_lsnoopy"
  -
    name: "Left Baron / Left Baron"
    short_name: "lbaron_lbaron"
mirrors:
  top_bot:
    -
      name: Angel / Left Snoopy
      short_name: angel_lsnoopy
  lr:
    -
      name: Right Snoopy / Angel
      short_name: rsnoopy_angel


---

