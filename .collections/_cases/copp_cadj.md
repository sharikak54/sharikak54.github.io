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
  alg: "1,0/3,0/-3,0/2,-1/0,3/0,1"
  description: Put isolated corner against slice in UFR, and D corners in DF.
color_mirror_algs:
  -
    alg: "0,-1/0,-3/3,0/1,-2/0,-3/-1,0"

# RELATED CASES
parents:
  -
    name: "Moth / Left Kite"
    short_name: "moth_lkite"
  -
    name: "Moth / Left Zero"
    short_name: "moth_lzero"
  -
    name: "Right Spill / Gem"
    short_name: "rspill_gem"
  -
    name: "Angel / Right Spill"
    short_name: "angel_rspill"
mirrors:
  top_bot:
    -
      name: Cadj / Copp
      short_name: cadj_copp


---

