---
title: "Case: Left Bird / Left Scottie"
name: Left Bird / Left Scottie
short_name: lbird_lscottie
top: Bird
top_short_name: bird
top_lr: Left
bot: Scottie
bot_short_name: scottie
bot_lr: Left

optimal: 4

recognition: bad bird/scottie; the clean slice between the tent and corner on bottom preserves squareshape when preserving the half on top

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,-2/-3,0/2,-1/0,1"
  description: fully preserve U half in UL, and position isolated corner on bottom next to the slice; first move trades isolated edge on top with isolated corner on bottom to make gem/snoopy
color_mirror_algs:
  -
    alg: "0,-1/4,4/2,-1/0,-3/0,1"
  -
    alg: "0,-1/4,4/0,-3/2,-1/0,1"
other_algs:
  -
    alg: "0,-1/-2,-2/-4,-1/3,0/0,1"

# RELATED CASES
parents:
  -
    name: "Gem / Left Snoopy"
    short_name: "gem_lsnoopy"
  -
    name: "Left Tent / Right Whale"
    short_name: "ltent_rwhale"
  -
    name: "Shell / Left Scottie"
    short_name: "shell_lscottie"
  -
    name: "Left Kite / Left Pinwheel"
    short_name: "lkite_lpinwheel"
mirrors:
  top_bot:
    -
      name: Left Scottie / Left Bird
      short_name: lscottie_lbird
  lr:
    -
      name: Right Bird / Right Scottie
      short_name: rbird_rscottie
  pseudo:
    -
      name: Right Bird / Left Scottie
      short_name: rbird_lscottie
    -
      name: Left Bird / Right Scottie
      short_name: lbird_rscottie


---

