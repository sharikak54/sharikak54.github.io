---
title: "Case: Eadj / Eopp"
name: Eadj / Eopp
short_name: eadj_eopp
top: Eadj
top_short_name: eadj
bot: Eopp
bot_short_name: eopp

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/2,-1/-2,1/2,-1/-3,0/0,1"
  description: hold edges in U FR, and D FB; split the adjacent edges on top
color_mirror_algs:
  -
    alg: "0,-1/3,0/0,-3/1,-2/3,0/-1,0"
other_algs:
  -
    alg: "1,0/0,-3/0,3/2,-1/-3,0/0,1"
  -
    alg: "-5,0/3,0/3,0/-1,-1/-2,1/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Left Kite / Plane"
    short_name: "lkite_plane"
  -
    name: "Shell / Right Bird"
    short_name: "shell_rbird"
  -
    name: "Plane / Right Zero"
    short_name: "plane_rzero"
  -
    name: "Left Bird / Hazard"
    short_name: "lbird_hazard"
mirrors:
  top_bot:
    -
      name: Eopp / Eadj
      short_name: eopp_eadj


---

