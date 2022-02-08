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

recognition: Bad whale/whale; whales are mirrors of each other.

# ALGORITHMS
default_alg:
  alg: "0,-1/3,0/-2,1/-3,0/-1,0"
  description: Put top whale in UL and bottom whale in DR; either slice alignment will create scottie/shell.
other_algs:
  -
    alg: "0,-1/3,0/-3,0/-2,1/-1,0"
  -
    alg: "1,0/-3,0/-4,-1/-3,0/0,1"
    alg: "1,0/-3,0/-4,-1/-3,0/0,1"

# RELATED CASES
parents:
  -
    name: "Right Scottie / Shell"
    short_name: "rscottie_shell"
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
  -
    name: "Left Axe / Gem"
    short_name: "laxe_gem"
  -
    name: "Gem / Right Axe"
    short_name: "gem_raxe"
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
  -
    name: "Left Axe / Gem"
    short_name: "laxe_gem"
  -
    name: "Gem / Right Axe"
    short_name: "gem_raxe"
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

