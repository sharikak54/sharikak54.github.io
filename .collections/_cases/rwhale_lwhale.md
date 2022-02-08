---
title: "Case: Right Whale / Left Whale"
name: Right Whale / Left Whale
short_name: rwhale_lwhale
top: Whale
top_short_name: whale
top_lr: Right
bot: Whale
bot_short_name: whale
bot_lr: Left

optimal: 4

recognition: Bad whale/whale; whales are mirrors of each other.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/3,0/2,-1/0,1"
  description: Put top whale in UL and bottom whale in DR; either slice alignment will create scottie/shell.
other_algs:
  -
    alg: "1,0/-3,0/2,-1/3,0/0,1"
  -
    alg: "0,-1/3,0/4,1/3,0/-1,0"
    alg: "0,-1/3,0/4,1/3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
  -
    name: "Right Scottie / Shell"
    short_name: "rscottie_shell"
  -
    name: "Right Axe / Gem"
    short_name: "raxe_gem"
  -
    name: "Gem / Left Axe"
    short_name: "gem_laxe"
  -
    name: "Right Scottie / Shell"
    short_name: "rscottie_shell"
  -
    name: "Right Axe / Gem"
    short_name: "raxe_gem"
  -
    name: "Gem / Left Axe"
    short_name: "gem_laxe"
mirrors:
  lr:
    -
      name: Left Whale / Right Whale
      short_name: lwhale_rwhale
  pseudo:
    -
      name: Left Whale / Left Whale
      short_name: lwhale_lwhale
    -
      name: Right Whale / Right Whale
      short_name: rwhale_rwhale


---

