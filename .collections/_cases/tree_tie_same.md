---
title: "Case: Same Tree / Tie"
name: Same Tree / Tie
short_name: tree_tie_same
top: Tree
top_short_name: tree
bot: Tie
bot_short_name: tie

optimal: 4

recognition: Bad tree/tie - color of tree and tie match.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,-3/-3,0/2,-1/0,1"
  description: Pair shell on top with a tent on bottom to form gem/axe.
color_mirror_algs:
  -
    alg: "0,-4/-3,-3/-2,1/0,3/-1,0"
  -
    alg: "1,0/3,3/2,-1/0,-3/0,1"
  -
    alg: "-2,-3/-3,-3/2,-1/0,3/0,1"
  -
    alg: "-5,-3/2,-1/4,-2/6,3/-1,0"
other_algs:
  -
    alg: "0,-4/3,3/4,1/-3,0/-1,0"
  -
    alg: "0,-4/3,3/1,-2/0,3/-1,0"
  -
    alg: "-2,-3/3,3/-1,2/0,3/0,1"
  -
    alg: "-5,-3/2,-1/-2,4/-3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Gem / Right Axe"
    short_name: "gem_raxe"
  -
    name: "Gem / Left Axe"
    short_name: "gem_laxe"
  -
    name: "Right Spill / Right Axe"
    short_name: "rspill_raxe"
  -
    name: "Left Spill / Left Axe"
    short_name: "lspill_laxe"
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
      name: Tie / Tree
      short_name: tie_tree


---

A Tree and a Tie that are the same color.  Be careful not to mistake this for [Tree / Tie](tree_tie).

