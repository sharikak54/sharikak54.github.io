---
title: "Case: Copp / Cadj"
name: Copp / Cadj
short_name: copp_cadj
top: Copp
top_short_name: copp
bot: Cadj
bot_short_name: cadj

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/0,-3/0,3/1,-2/-3,0/-1,0"
  description: corner mirror; put U corners in UF, and put an isolated corner against slice in DFR
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
      name: Cadj / Copp
      short_name: cadj_copp


---

