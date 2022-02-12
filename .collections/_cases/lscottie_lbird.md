---
title: "Case: Left Scottie / Left Bird"
name: Left Scottie / Left Bird
short_name: lscottie_lbird
top: Scottie
top_short_name: scottie
top_lr: Left
bot: Bird
bot_short_name: bird
bot_lr: Left

optimal: 4

recognition: Bad scottie/bird; the clean slice between the tent and corner on top preserves squareshape when preserving the  kite on bottom.

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,-2/2,-1/-3,0/0,1"
  description: Position isolated corner on top next to the slice, and preserve D kite in DL; first move trades isolated corner on top with isolated edge on bottom to make axe/gem.
color_mirror_algs:
  -
    alg: "0,-1/4,4/-1,2/-3,0/0,1"
  -
    alg: "0,-1/4,4/-3,0/-1,2/0,1"
other_algs:
  -
    alg: "0,-1/-2,-2/0,-3/-1,2/0,1"

# RELATED CASES
parents:
  -
    name: "Left Axe / Gem"
    short_name: "laxe_gem"
  -
    name: "Right Whale / Left Tent"
    short_name: "rwhale_ltent"
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
  -
    name: "Left Pinwheel / Left Kite"
    short_name: "lpinwheel_lkite"
mirrors:
  top_bot:
    -
      name: Left Bird / Left Scottie
      short_name: lbird_lscottie
  lr:
    -
      name: Right Scottie / Right Bird
      short_name: rscottie_rbird
  pseudo:
    -
      name: Right Scottie / Left Bird
      short_name: rscottie_lbird
    -
      name: Left Scottie / Right Bird
      short_name: lscottie_rbird


---

