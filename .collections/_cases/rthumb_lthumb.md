---
title: "Case: Right Thumb / Left Thumb"
name: Right Thumb / Left Thumb
short_name: rthumb_lthumb
top: Thumb
top_short_name: thumb
top_lr: Right
bot: Thumb
bot_short_name: thumb
bot_lr: Left

optimal: 5

recognition: Bad thumbs; thumbs are mirrors of each other, or making a kite on one face forms tree on the other

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-1/-2,1/2,-1/-3,0/0,1"
  description: Keep bottom shell in DL, swap 2 edges on top with isolated corner on bottom to form good birds.
other_algs:
  -
    alg: "0,-1/1,1/-3,0/2,-1/-3,0/0,1"

# RELATED CASES
parents:
  -
    name: "Left Bird / Right Bird"
    short_name: "lbird_rbird"
  -
    name: "Left Kite / Tree"
    short_name: "lkite_tree"
  -
    name: "Tie / Right Kite"
    short_name: "tie_rkite"
  -
    name: "Squid / Left Axe"
    short_name: "squid_laxe"
  -
    name: "Left Whale / Left Tent"
    short_name: "lwhale_ltent"
  -
    name: "Right Whale / Right Tent"
    short_name: "rwhale_rtent"
  -
    name: "Left Scottie / Hazard"
    short_name: "lscottie_hazard"
  -
    name: "Left Spill / Right Spill"
    short_name: "lspill_rspill"
  -
    name: "Right Axe / Squid"
    short_name: "raxe_squid"
mirrors:
  lr:
    -
      name: Left Thumb / Right Thumb
      short_name: lthumb_rthumb
  pseudo:
    -
      name: Left Thumb / Left Thumb
      short_name: lthumb_lthumb
    -
      name: Right Thumb / Right Thumb
      short_name: rthumb_rthumb


---

