---
title: "Case: Squid / Squid"
name: Squid / Squid
short_name: squid_squid
top: Squid
top_short_name: squid
bot: Squid
bot_short_name: squid

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/-3,0/-3,3/4,1/-1,0"
  description: Put isolated corners in UBL and DFR; either alignment will make scottie/hazard.
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

# RELATED CASES
parents:
  -
    name: "Left Scottie / Hazard"
    short_name: "lscottie_hazard"
  -
    name: "Right Scottie / Hazard"
    short_name: "rscottie_hazard"
---

