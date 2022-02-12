---
title: "Case: Right Tent / Right Whale"
name: Right Tent / Right Whale
short_name: rtent_rwhale
top: Tent
top_short_name: tent
top_lr: Right
bot: Whale
bot_short_name: whale
bot_lr: Right

optimal: 4

recognition: Bad tent/whale; splitting tent on top and sandwiched tent on bottom breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/4,1/3,0/-4,-1/0,1"
  description: Swap tent on top (so that it's not touching the slice) with same-colored spill on bottom (keeping shell on DL) to form spill/axe.

# RELATED CASES
parents:
  -
    name: "Right Spill / Right Axe"
    short_name: "rspill_raxe"
  -
    name: "Left Bird / Right Scottie"
    short_name: "lbird_rscottie"
  -
    name: "Left Bird / Right Scottie"
    short_name: "lbird_rscottie"
  -
    name: "Left Bird / Right Scottie"
    short_name: "lbird_rscottie"
mirrors:
  top_bot:
    -
      name: Right Whale / Right Tent
      short_name: rwhale_rtent
  lr:
    -
      name: Left Tent / Left Whale
      short_name: ltent_lwhale
  pseudo:
    -
      name: Left Tent / Right Whale
      short_name: ltent_rwhale
    -
      name: Right Tent / Left Whale
      short_name: rtent_lwhale


---

