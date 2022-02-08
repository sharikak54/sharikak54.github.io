---
title: "Case: Gem / Squid"
name: Gem / Squid
short_name: gem_squid
top: Gem
top_short_name: gem
bot: Squid
bot_short_name: squid

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/0,3/1,1/-1,0"
  description: Do CO into M2; create same trees by pairing U-color corner from bottom with tent on top.
other_algs:
  -
    alg: "-2,-3/0,3/0,3/-1,-1/0,1"
  -
    alg: "4,3/3,0/0,3/-1,-1/0,1"
  -
    alg: "6,5/0,-3/0,3/1,1/-1,0"
    alg: "4,3/3,0/0,3/-1,-1/0,1"
  -
    alg: "6,5/0,-3/0,3/1,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Same Tree / Tree"
    short_name: "tree_tree_same"
  -
    name: "Right Scottie / Left Bird"
    short_name: "rscottie_lbird"
  -
    name: "Left Scottie / Right Bird"
    short_name: "lscottie_rbird"
  -
    name: "Right Scottie / Left Bird"
    short_name: "rscottie_lbird"
  -
    name: "Left Scottie / Right Bird"
    short_name: "lscottie_rbird"
mirrors:
  top_bot:
    -
      name: Squid / Gem
      short_name: squid_gem


---

