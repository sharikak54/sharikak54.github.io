---
title: "Case: Same Moth / Plane"
name: Same Moth / Plane
short_name: moth_plane_same
top: Moth
top_short_name: moth
bot: Plane
bot_short_name: plane

optimal: 4

recognition: Bad moth/plane - color of moth and plane match.

# ALGORITHMS
default_alg:
  alg: "0,-1/3,3/-2,1/3,0/-1,0"
  description: Send tent on top with shell on bottom to form snoopy/gem.
color_mirror_algs:
  -
    alg: "0,-1/-3,-3/1,-2/3,0/-1,0"
  -
    alg: "0,-1/-3,-3/4,1/0,-3/-1,0"
  -
    alg: "4,0/3,3/-1,2/-3,0/0,1"
  -
    alg: "1,-3/-3,-3/-4,-1/-3,0/0,1"
other_algs:
  -
    alg: "4,0/-3,-3/2,-1/-3,0/0,1"
  -
    alg: "1,-3/3,3/3,0/2,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Right Snoopy / Gem"
    short_name: "rsnoopy_gem"
  -
    name: "Left Snoopy / Gem"
    short_name: "lsnoopy_gem"
  -
    name: "Right Snoopy / Right Spill"
    short_name: "rsnoopy_rspill"
  -
    name: "Left Snoopy / Left Spill"
    short_name: "lsnoopy_lspill"
  -
    name: "Right Bird / Left Scottie"
    short_name: "rbird_lscottie"
  -
    name: "Left Bird / Right Scottie"
    short_name: "lbird_rscottie"
  -
    name: "Right Whale / Right Whale"
    short_name: "rwhale_rwhale"
  -
    name: "Left Whale / Left Whale"
    short_name: "lwhale_lwhale"
mirrors:
  top_bot:
    -
      name: Plane / Moth
      short_name: plane_moth


---

A Moth and a Plane that are the same color.  Be careful not to mistake this for [Moth / Plane](moth_plane).

