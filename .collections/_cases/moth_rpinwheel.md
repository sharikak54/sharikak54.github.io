---
title: "Case: Moth / Right Pinwheel"
name: Moth / Right Pinwheel
short_name: moth_rpinwheel
top: Moth
top_short_name: moth
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Right

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/2,-1/1,-2/3,0/-1,0"
  description: Create a shell on top (as part of a plane) with the isolated corner on top and a tent on bottom.
color_mirror_algs:
  -
    alg: "1,0/0,3/2,-1/-2,1/3,0/-1,0"
  -
    alg: "0,-1/-2,1/-3,0/-4,-1/1,4/-1,0"
  -
    alg: "-2,3/0,3/-1,2/1,4/-4,-1/0,1"
  -
    alg: "-3,2/1,-2/-4,-1/0,-3/1,4/-1,0"
  -
    alg: "-5,6/3,0/2,-1/1,-2/-3,6/-1,0"
other_algs:
  -
    alg: "0,-1/1,-2/-3,0/-1,-4/1,4/-1,0"
  -
    alg: "-2,3/3,0/-1,2/4,1/-4,-1/0,1"
  -
    alg: "-3,2/-2,1/-4,-1/-3,0/1,4/-1,0"
  -
    alg: "-5,6/0,3/2,-1/-2,1/-3,6/-1,0"

# RELATED CASES
parents:
  -
    name: "Plane / Right Kite"
    short_name: "plane_rkite"
  -
    name: "Hazard / Right Bird"
    short_name: "hazard_rbird"
  -
    name: "Shell / Right Bird"
    short_name: "shell_rbird"
  -
    name: "Plane / Right Zero"
    short_name: "plane_rzero"
mirrors:
  top_bot:
    -
      name: Right Pinwheel / Moth
      short_name: rpinwheel_moth
  lr:
    -
      name: Moth / Left Pinwheel
      short_name: moth_lpinwheel


---

