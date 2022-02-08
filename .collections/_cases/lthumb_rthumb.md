---
title: "Case: Left Thumb / Right Thumb"
name: Left Thumb / Right Thumb
short_name: lthumb_rthumb
top: Thumb
top_short_name: thumb
top_lr: Left
bot: Thumb
bot_short_name: thumb
bot_lr: Right

optimal: 5

recognition: Bad thumbs; thumbs are mirrors of each other, or making a kite on one face forms tree on the other.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,1/2,-1/-2,1/3,0/-1,0"
  description: Keep bottom shell in DL, swap 2 edges on top with isolated corner on bottom to form bird/bird.
other_algs:
  -
    alg: "1,0/-1,-1/3,0/-2,1/3,0/-1,0"
# RELATED CASES
parents:
  -
    name: "Right Bird / Left Bird"
    short_name: "rbird_lbird"
  -
    name: "Right Kite / Tree"
    short_name: "rkite_tree"
  -
    name: "Tie / Left Kite"
    short_name: "tie_lkite"
  -
    name: "Squid / Right Axe"
    short_name: "squid_raxe"
  -
    name: "Right Whale / Right Tent"
    short_name: "rwhale_rtent"
  -
    name: "Left Whale / Left Tent"
    short_name: "lwhale_ltent"
  -
    name: "Right Scottie / Hazard"
    short_name: "rscottie_hazard"
  -
    name: "Right Spill / Left Spill"
    short_name: "rspill_lspill"
  -
    name: "Left Axe / Squid"
    short_name: "laxe_squid"
  -
    name: "Right Kite / Tree"
    short_name: "rkite_tree"
  -
    name: "Tie / Left Kite"
    short_name: "tie_lkite"
  -
    name: "Squid / Right Axe"
    short_name: "squid_raxe"
  -
    name: "Right Whale / Right Tent"
    short_name: "rwhale_rtent"
  -
    name: "Left Whale / Left Tent"
    short_name: "lwhale_ltent"
  -
    name: "Right Scottie / Hazard"
    short_name: "rscottie_hazard"
  -
    name: "Right Spill / Left Spill"
    short_name: "rspill_lspill"
  -
    name: "Left Axe / Squid"
    short_name: "laxe_squid"
mirrors:
  lr:
    -
      name: Right Thumb / Left Thumb
      short_name: rthumb_lthumb
  pseudo:
    -
      name: Right Thumb / Right Thumb
      short_name: rthumb_rthumb
    -
      name: Left Thumb / Left Thumb
      short_name: lthumb_lthumb


---

