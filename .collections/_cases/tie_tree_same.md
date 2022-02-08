---
title: "Case: Same Tie / Tree"
name: Same Tie / Tree
short_name: tie_tree_same
top: Tie
top_short_name: tie
bot: Tree
bot_short_name: tree

optimal: 4

recognition: Bad tie/tree - color of tie and tree match.

# ALGORITHMS
default_alg:
  alg: "0,-1/3,3/-2,1/3,0/-1,0"
  description: Send tent on top with shell on bottom to form axe/gem.
color_mirror_algs:
  -
    alg: "0,-1/-3,-3/1,-2/3,0/-1,0"
  -
    alg: "0,-1/-3,-3/4,1/0,-3/-1,0"
  -
    alg: "4,0/3,3/-1,2/-3,0/0,1"
  -
    alg: "1,-3/-3,-3/-4,-1/-3,0/0,1"
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
    alg: "1,-3/3,3/3,0/2,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Right Axe / Gem"
    short_name: "raxe_gem"
  -
    name: "Left Axe / Gem"
    short_name: "laxe_gem"
  -
    name: "Right Axe / Right Spill"
    short_name: "raxe_rspill"
  -
    name: "Left Axe / Left Spill"
    short_name: "laxe_lspill"
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
  -
    name: "Left Axe / Gem"
    short_name: "laxe_gem"
  -
    name: "Right Axe / Right Spill"
    short_name: "raxe_rspill"
  -
    name: "Left Axe / Left Spill"
    short_name: "laxe_lspill"
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
      name: Tree / Tie
      short_name: tree_tie


---

A Tie and a Tree that are the same color.  Be careful not to mistake this for [Tie / Tree](tie_tree).

