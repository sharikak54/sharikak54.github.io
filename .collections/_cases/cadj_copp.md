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
    alg: "1,0/3,0/0,-3/2,-1/3,0/0,1"
# RELATED CASES
parents:
  -
    name: "Right Kite / Tie"
    short_name: "rkite_tie"
  -
    name: "Right Cut / Tie"
    short_name: "rcut_tie"
  -
    name: "Gem / Left Spill"
    short_name: "gem_lspill"
  -
    name: "Left Spill / Squid"
    short_name: "lspill_squid"
  -
    name: "Right Cut / Tie"
    short_name: "rcut_tie"
  -
    name: "Gem / Left Spill"
    short_name: "gem_lspill"
  -
    name: "Left Spill / Squid"
    short_name: "lspill_squid"
mirrors:
  top_bot:
    -
      name: Copp / Cadj
      short_name: copp_cadj


---

