---
title: "Case: Right Bird / Right Scottie"
name: Right Bird / Right Scottie
short_name: rbird_rscottie
top: Bird
top_short_name: bird
top_lr: Right
bot: Scottie
bot_short_name: scottie
bot_lr: Right

optimal: 4

recognition: Bad bird/scottie; the clean slice between the tent and corner on bottom preserves squareshape when preserving the kite on top.

# ALGORITHMS
default_alg:
  alg: "1,0/2,2/3,0/-2,1/-1,0"
  description: Fully preserve U kite in UL, and position isolated corner on bottom next to the slice; first move trades isolated edge on top with isolated corner on bottom to make gem/axe.
color_mirror_algs:
  -
    alg: "1,0/-4,-4/-2,1/0,3/-1,0"
  -
    alg: "1,0/-4,-4/0,3/-2,1/-1,0"
other_algs:
  -
    alg: "1,0/2,2/4,1/-3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Gem / Right Axe"
    short_name: "gem_raxe"
  -
    name: "Right Tent / Left Whale"
    short_name: "rtent_lwhale"
  -
    name: "Shell / Right Scottie"
    short_name: "shell_rscottie"
  -
    name: "Right Kite / Right Pinwheel"
    short_name: "rkite_rpinwheel"
mirrors:
  top_bot:
    -
      name: Right Scottie / Right Bird
      short_name: rscottie_rbird
  lr:
    -
      name: Left Bird / Left Scottie
      short_name: lbird_lscottie
  pseudo:
    -
      name: Left Bird / Right Scottie
      short_name: lbird_rscottie
    -
      name: Right Bird / Left Scottie
      short_name: rbird_lscottie


---

