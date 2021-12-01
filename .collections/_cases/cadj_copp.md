---
title: "Case: Cadj / Copp"
name: Cadj / Copp
short_name: cadj_copp
top: Cadj
top_short_name: cadj
bot: Copp
bot_short_name: copp

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/0,-3/0,3/1,-2/-3,0/-1,0"
  description: Put U corners in UF, and put an isolated corner against slice in DFR.
color_mirror_algs:
  -
    alg: "0,-1/0,-3/3,0/1,-2/0,-3/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Kite / Moth"
    short_name: "rkite_moth"
  -
    name: "Right Zero / Moth"
    short_name: "rzero_moth"
  -
    name: "Gem / Left Spill"
    short_name: "gem_lspill"
  -
    name: "Left Spill / Angel"
    short_name: "lspill_angel"
mirrors:
  top_bot:
    -
      name: Copp / Cadj
      short_name: copp_cadj


---

