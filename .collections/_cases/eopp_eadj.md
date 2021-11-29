---
title: "Case: Eopp / Eadj"
name: Eopp / Eadj
short_name: eopp_eadj
top: Eopp
top_short_name: eopp
bot: Eadj
bot_short_name: eadj

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/3,0/-3,0/1,-2/0,3/-1,0"
  description: Hold edges in U FB, and D FR; split the adjacent edges on bottom.
color_mirror_algs:
  -
    alg: "1,0/0,-3/3,0/2,-1/0,-3/0,1"
other_algs:
  -
    alg: "0,-1/3,0/-3,0/1,1/3,0/-3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Plane / Right Kite"
    short_name: "plane_rkite"
  -
    name: "Left Bird / Shell"
    short_name: "lbird_shell"
  -
    name: "Left Zero / Plane"
    short_name: "lzero_plane"
  -
    name: "Hazard / Right Bird"
    short_name: "hazard_rbird"
mirrors:
  top_bot:
    -
      name: Eadj / Eopp
      short_name: eadj_eopp


---

