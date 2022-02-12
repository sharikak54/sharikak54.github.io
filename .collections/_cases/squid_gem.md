---
title: "Case: Squid / Gem"
name: Squid / Gem
short_name: squid_gem
top: Squid
top_short_name: squid
bot: Gem
bot_short_name: gem

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/-3,0/-1,-1/0,1"
  description: Do CO into M2; create same trees by pairing corner on top with a tent from bottom.
other_algs:
  -
    alg: "3,2/0,-3/-3,0/1,1/-1,0"
  -
    alg: "-3,-4/-3,0/-3,0/1,1/-1,0"
  -
    alg: "-5,6/0,3/-3,0/-1,-1/0,1"

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
mirrors:
  top_bot:
    -
      name: Gem / Squid
      short_name: gem_squid


---

