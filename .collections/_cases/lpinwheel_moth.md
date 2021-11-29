---
title: "Case: Left Pinwheel / Moth"
name: Left Pinwheel / Moth
short_name: lpinwheel_moth
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
bot: Moth
bot_short_name: moth

optimal: 5

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/0,-3/1,-2/0,-3/2,-1/0,1"
  description: Create a yellow (D-color) shell on bottom (as part of a plane) by pairing isolated yellow corner on bottom with yellow tent on top.
color_mirror_algs:
  -
    alg: "0,-1/-3,0/1,-2/-3,0/2,-1/0,1"
  -
    alg: "1,0/-1,2/0,3/1,4/-4,-1/0,1"
  -
    alg: "-2,3/2,-1/1,4/3,0/-4,-1/0,1"
  -
    alg: "-3,2/-3,0/-2,1/-4,-1/1,4/-1,0"
  -
    alg: "6,5/0,-3/1,-2/0,-3/-4,5/0,1"
other_algs:
  -
    alg: "1,0/2,-1/0,3/4,1/-4,-1/0,1"
  -
    alg: "-2,3/-1,2/1,4/0,3/-4,-1/0,1"
  -
    alg: "-3,2/0,-3/-2,1/-1,-4/1,4/-1,0"
  -
    alg: "6,5/-3,0/1,-2/-3,0/-4,5/0,1"

# RELATED CASES
parents:
  -
    name: "Left Kite / Plane"
    short_name: "lkite_plane"
  -
    name: "Left Bird / Hazard"
    short_name: "lbird_hazard"
  -
    name: "Left Bird / Shell"
    short_name: "lbird_shell"
  -
    name: "Left Zero / Plane"
    short_name: "lzero_plane"
mirrors:
  top_bot:
    -
      name: Moth / Left Pinwheel
      short_name: moth_lpinwheel
  lr:
    -
      name: Right Pinwheel / Moth
      short_name: rpinwheel_moth


---

