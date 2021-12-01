---
title: "Case: Left Tent / Left Whale"
name: Left Tent / Left Whale
short_name: ltent_lwhale
top: Tent
top_short_name: tent
top_lr: Left
bot: Whale
bot_short_name: whale
bot_lr: Left

optimal: 4

recognition: Bad tent/whale; splitting tent on top and sandwiched tent on bottom breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/-3,0/4,1/-1,0"
  description: Swap tent on top (so that it's not touching the slice) with same-colored spill on bottom (keeping shell on DL) to form spill/snoopy.

# RELATED CASES
parents:
  -
    name: "Left Spill / Left Snoopy"
    short_name: "lspill_lsnoopy"
  -
    name: "Right Bird / Left Scottie"
    short_name: "rbird_lscottie"
mirrors:
  top_bot:
    -
      name: Left Whale / Left Tent
      short_name: lwhale_ltent
  lr:
    -
      name: Right Tent / Right Whale
      short_name: rtent_rwhale
  pseudo:
    -
      name: Right Tent / Left Whale
      short_name: rtent_lwhale
    -
      name: Left Tent / Right Whale
      short_name: ltent_rwhale


---

