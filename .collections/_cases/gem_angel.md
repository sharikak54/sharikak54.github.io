---
title: "Case: Gem / Angel"
name: Gem / Angel
short_name: gem_angel
top: Gem
top_short_name: gem
bot: Angel
bot_short_name: angel

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/0,3/1,1/-1,0"
  description: Do CO into M2; create same plane/plane by pairing U-color corner from bottom with tent on top.
other_algs:
  -
    alg: "-2,-3/0,3/0,3/-1,-1/0,1"
  -
    alg: "4,3/3,0/0,3/-1,-1/0,1"
  -
    alg: "6,5/0,-3/0,3/1,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Same Plane / Plane"
    short_name: "plane_plane_same"
  -
    name: "Right Scottie / Left Bird"
    short_name: "rscottie_lbird"
  -
    name: "Left Scottie / Right Bird"
    short_name: "lscottie_rbird"
mirrors:
  top_bot:
    -
      name: Angel / Gem
      short_name: angel_gem


---

