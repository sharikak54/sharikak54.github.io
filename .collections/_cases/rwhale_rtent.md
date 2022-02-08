---
title: "Case: Right Whale / Right Tent"
name: Right Whale / Right Tent
short_name: rwhale_rtent
top: Whale
top_short_name: whale
top_lr: Right
bot: Tent
bot_short_name: tent
bot_lr: Right

optimal: 4

recognition: Bad whale/tent; splitting sandwiched tent on top and tent on bottom breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,4/0,3/-1,-4/0,1"
  description: Keep only isolated corner on top, swapping isolated edge for same-color whale to form scottie/bird.
other_algs:
  -
    alg: "3,-1/4,1/-3,0/-4,-1/0,1"
# RELATED CASES
parents:
  -
    name: "Right Scottie / Left Bird"
    short_name: "rscottie_lbird"
  -
    name: "Right Axe / Right Spill"
    short_name: "raxe_rspill"
  -
    name: "Right Axe / Right Spill"
    short_name: "raxe_rspill"
mirrors:
  top_bot:
    -
      name: Right Tent / Right Whale
      short_name: rtent_rwhale
  lr:
    -
      name: Left Whale / Left Tent
      short_name: lwhale_ltent
  pseudo:
    -
      name: Left Whale / Right Tent
      short_name: lwhale_rtent
    -
      name: Right Whale / Left Tent
      short_name: rwhale_ltent


---

