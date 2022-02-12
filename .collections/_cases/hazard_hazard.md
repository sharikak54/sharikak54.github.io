---
title: "Case: Hazard / Hazard"
name: Hazard / Hazard
short_name: hazard_hazard
top: Hazard
top_short_name: hazard
bot: Hazard
bot_short_name: hazard

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-1,2/-3,0/-2,1/-4,-1/0,1"
  description: Keep non-hazard corners in DL, swap whale on top with hazard corners on bottom to get squid/axe.
color_mirror_algs:
  -
    alg: "1,0/-1,2/-3,0/-2,1/2,5/0,1"
  -
    alg: "0,5/-2,1/3,0/-1,2/4,1/-1,0"
  -
    alg: "-5,6/2,-1/-3,0/1,-2/-4,-1/0,1"
  -
    alg: "6,-1/1,-2/3,0/2,-1/-2,-5/-1,0"
  -
    alg: "6,-1/1,-2/5,-1/-2,1/2,5/0,1"
other_algs:
  -
    alg: "6,-1/1,-2/3,0/2,-1/4,1/-1,0"
  -
    alg: "6,-1/1,-2/5,-1/-2,1/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Squid / Left Axe"
    short_name: "squid_laxe"
  -
    name: "Squid / Right Axe"
    short_name: "squid_raxe"
---

