---
title: "Case: Same Plane / Moth"
name: Same Plane / Moth
short_name: plane_moth_same
top: Plane
top_short_name: plane
bot: Moth
bot_short_name: moth

optimal: 4

recognition: Bad plane/moth - color of plane and moth match.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,-3/-2,1/0,3/-1,0"
  description: Pair shell on top with a tent on bottom to form gem/snoopy.
color_mirror_algs:
  -
    alg: "0,-1/3,3/4,1/-3,0/-1,0"
  -
    alg: "0,-1/3,3/1,-2/0,3/-1,0"
  -
    alg: "1,3/-3,-3/-3,0/2,-1/0,1"
  -
    alg: "-2,0/3,3/-1,2/0,3/0,1"
  -
    alg: "-3,-4/-3,-3/4,1/3,0/-1,0"
  -
    alg: "-3,-4/-3,-3/1,-2/-3,0/-1,0"
other_algs:
  -
    alg: "1,3/3,3/2,-1/0,-3/0,1"
  -
    alg: "-2,0/-3,-3/2,-1/0,3/0,1"
  -
    alg: "-3,-4/3,3/-2,1/-3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Gem / Right Snoopy"
    short_name: "gem_rsnoopy"
  -
    name: "Gem / Left Snoopy"
    short_name: "gem_lsnoopy"
  -
    name: "Right Spill / Right Snoopy"
    short_name: "rspill_rsnoopy"
  -
    name: "Left Spill / Left Snoopy"
    short_name: "lspill_lsnoopy"
  -
    name: "Right Scottie / Left Bird"
    short_name: "rscottie_lbird"
  -
    name: "Left Scottie / Right Bird"
    short_name: "lscottie_rbird"
  -
    name: "Right Whale / Right Whale"
    short_name: "rwhale_rwhale"
  -
    name: "Left Whale / Left Whale"
    short_name: "lwhale_lwhale"
mirrors:
  top_bot:
    -
      name: Moth / Plane
      short_name: moth_plane


---

A Plane and a Moth that are the same color.  Be careful not to mistake this for [Plane / Moth](plane_moth).

