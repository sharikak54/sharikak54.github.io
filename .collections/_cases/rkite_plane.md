---
title: "Case: Right Kite / Plane"
name: Right Kite / Plane
short_name: rkite_plane
top: Kite
top_short_name: kite
top_lr: Right
bot: Plane
bot_short_name: plane

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/2,-1/-2,1/-3,6/-1,0"
  description: send tent on top to pair with shell on bottom to form snoopy/gem
color_mirror_algs:
  -
    alg: "1,0/2,-1/-2,1/3,0/-1,0"
other_algs:
  -
    alg: "-5,6/-1,2/-2,1/6,-3/-1,0"
  -
    alg: "-5,6/5,-4/1,-2/0,3/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Snoopy / Gem"
    short_name: "rsnoopy_gem"
  -
    name: "Left Spill / Left Snoopy"
    short_name: "lspill_lsnoopy"
mirrors:
  top_bot:
    -
      name: Plane / Right Kite
      short_name: plane_rkite
  lr:
    -
      name: Left Kite / Plane
      short_name: lkite_plane


---

