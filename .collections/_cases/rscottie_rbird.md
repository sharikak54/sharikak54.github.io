---
title: "Case: Right Scottie / Right Bird"
name: Right Scottie / Right Bird
short_name: rscottie_rbird
top: Scottie
top_short_name: scottie
top_lr: Right
bot: Bird
bot_short_name: bird
bot_lr: Right

optimal: 4

recognition: bad scottie/bird; the clean slice between the tent and corner on top preserves squareshape when preserving the half on bottom

# ALGORITHMS
default_alg:
  alg: "1,0/2,2/-2,1/3,0/-1,0"
  description: position isolated corner on top next to the slice, and preserve D half in DL; first move trades isolated corner on top with isolated edge on bottom to make snoopy/gem
color_mirror_algs:
  -
    alg: "1,0/-4,-4/3,0/1,-2/-1,0"
  -
    alg: "1,0/-4,-4/1-2/3,0/-1,0"
other_algs:
  -
    alg: "1,0/2,2/0,3/1,-2/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Snoopy / Gem"
    short_name: "rsnoopy_gem"
  -
    name: "Left Whale / Right Tent"
    short_name: "lwhale_rtent"
  -
    name: "Right Scottie / Shell"
    short_name: "rscottie_shell"
  -
    name: "Right Pinwheel / Right Kite"
    short_name: "rpinwheel_rkite"
mirrors:
  top_bot:
    -
      name: Right Bird / Right Scottie
      short_name: rbird_rscottie
  lr:
    -
      name: Left Scottie / Left Bird
      short_name: lscottie_lbird
  pseudo:
    -
      name: Left Scottie / Right Bird
      short_name: lscottie_rbird
    -
      name: Right Scottie / Left Bird
      short_name: rscottie_lbird


---

