---
title: "Case: Angel / Angel"
name: Angel / Angel
short_name: angel_angel
top: Angel
top_short_name: angel
bot: Angel
bot_short_name: angel

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/-3,0/-3,3/4,1/-1,0"
  description: put isolated corners in UBL and DFR; either alignment will make scottie/hazard
color_mirror_algs:
  -
    alg: ""
other_algs:
  -
    alg: "0,-1/1,-2/0,-3/2,-1/-2,-5/-1,0"
  -
    alg: "0,-1/1,-2/-4,2/1,-2/-4,-1/0,1"
  -
    alg: "0,-1/4,1/0,3/-3,3/2,5/0,1"
  -
    alg: "3,-1/-2,-2/3,0/-4,-1/-2,1/-3,0/-1,0"
  -
    alg: "4,-3/2,-1/0,3/1,-2/-4,-1/0,1"
  -
    alg: "-2,3/-1,2/0,3/-2,1/2,5/0,1"
  -
    alg: "-2,3/-1,2/4,-2/-1,2/4,1/-1,0"
  -
    alg: "-2,3/-4,-1/0,-3/-3,3/-5,-2/-1,0"
  -
    alg: ""

# RELATED CASES
parents:
  -
    name: "Left Scottie / Hazard"
    short_name: "lscottie_hazard"
  -
    name: "Right Scottie / Hazard"
    short_name: "rscottie_hazard"
---

