---
title: "Case: Left Whale / Right Whale"
name: Left Whale / Right Whale
short_name: lwhale_rwhale
top: Whale
top_short_name: whale
top_lr: Left
bot: Whale
bot_short_name: whale
bot_lr: Right

optimal: 4

recognition: Bad whales; whales are mirrors of each other.

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/2,-1/-3,0/0,1"
  description: Swap top whale head, held against slice with tail in UL, with full bottom whale in DR.
other_algs:
  -
    alg: "4,0/-3,0/-1,2/3,0/0,1"
  -
    alg: "3,-1/3,0/-2,1/-3,0/-1,0"
  -
    alg: "3,-1/3,0/-3,0/-2,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Axe / Gem"
    short_name: "laxe_gem"
  -
    name: "Gem / Right Axe"
    short_name: "gem_raxe"
  -
    name: "Right Scottie / Shell"
    short_name: "rscottie_shell"
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
mirrors:
  lr:
    -
      name: Right Whale / Left Whale
      short_name: rwhale_lwhale
  pseudo:
    -
      name: Right Whale / Right Whale
      short_name: rwhale_rwhale
    -
      name: Left Whale / Left Whale
      short_name: lwhale_lwhale


---

