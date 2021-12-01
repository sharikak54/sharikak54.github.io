---
title: "Case: Left Whale / Left Tent"
name: Left Whale / Left Tent
short_name: lwhale_ltent
top: Whale
top_short_name: whale
top_lr: Left
bot: Tent
bot_short_name: tent
bot_lr: Left

optimal: 4

recognition: Bad whale/tent; splitting sandwiched tent on top and tent on bottom breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/3,0/4,1/-1,0"
  description: Keep only isolated corner on top, swapping isolated edge for same-color whale to form scottie/bird.
other_algs:
  -
    alg: "4,0/-1,-4/0,-3/1,4/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Scottie / Right Bird"
    short_name: "lscottie_rbird"
  -
    name: "Left Snoopy / Left Spill"
    short_name: "lsnoopy_lspill"
mirrors:
  top_bot:
    -
      name: Left Tent / Left Whale
      short_name: ltent_lwhale
  lr:
    -
      name: Right Whale / Right Tent
      short_name: rwhale_rtent
  pseudo:
    -
      name: Right Whale / Left Tent
      short_name: rwhale_ltent
    -
      name: Left Whale / Right Tent
      short_name: lwhale_rtent


---

