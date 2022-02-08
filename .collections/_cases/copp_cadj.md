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
    name: "Tie / Left Kite"
    short_name: "tie_lkite"
  -
    name: "Tie / Left Cut"
    short_name: "tie_lcut"
  -
    name: "Right Spill / Gem"
    short_name: "rspill_gem"
  -
    name: "Squid / Right Spill"
    short_name: "squid_rspill"
  -
    name: "Tie / Left Cut"
    short_name: "tie_lcut"
  -
    name: "Right Spill / Gem"
    short_name: "rspill_gem"
  -
    name: "Squid / Right Spill"
    short_name: "squid_rspill"
mirrors:
  top_bot:
    -
      name: Cadj / Copp
      short_name: cadj_copp


---

