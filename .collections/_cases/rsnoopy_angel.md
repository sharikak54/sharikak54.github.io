---
title: "Case: Right Snoopy / Angel"
name: Right Snoopy / Angel
short_name: rsnoopy_angel
top: Snoopy
top_short_name: snoopy
top_lr: Right
bot: Angel
bot_short_name: angel

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/-1,2/1,4/-1,0"
  description: put shell on top in UL, pair tent on top with whale on bottom to form good plane/moth
color_mirror_algs:
  -
    alg: ""
other_algs:
  -
    alg: "-5,6/3,0/-1,2/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Plane / Moth"
    short_name: "plane_moth"
  -
    name: "Right Spill / Right Snoopy"
    short_name: "rspill_rsnoopy"
  -
    name: "Right Baron / Right Baron"
    short_name: "rbaron_rbaron"
mirrors:
  top_bot:
    -
      name: Angel / Right Snoopy
      short_name: angel_rsnoopy
  lr:
    -
      name: Left Snoopy / Angel
      short_name: lsnoopy_angel


---

