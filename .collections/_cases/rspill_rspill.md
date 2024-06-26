---
title: "Case: Right Spill / Right Spill"
name: Right Spill / Right Spill
short_name: rspill_rspill
top: Spill
top_short_name: spill
top_lr: Right
bot: Spill
bot_short_name: spill
bot_lr: Right

optimal: 5

recognition: Bad spill/spill; swapping spills preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/-2,-2/2,-1/-3,0/0,1"
  description: Preserve full kite on bottom in DL, swap isolated edge on top with isolated corner on bottom to make scottie/bird.
other_algs:
  -
    alg: "1,0/-4,-1/-2,-2/2,-1/-3,0/0,1"
  -
    alg: "6,-1/-5,1/-4,-1/3,0/4,1/-1,0"
  -
    alg: "6,-1/-2,1/-1,-4/0,-3/1,4/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Scottie / Left Bird"
    short_name: "lscottie_lbird"
  -
    name: "Left Whale / Left Tent"
    short_name: "lwhale_ltent"
  -
    name: "Right Bunny / Left Thumb"
    short_name: "rbunny_lthumb"
mirrors:
  lr:
    -
      name: Left Spill / Left Spill
      short_name: lspill_lspill
  pseudo:
    -
      name: Left Spill / Right Spill
      short_name: lspill_rspill
    -
      name: Right Spill / Left Spill
      short_name: rspill_lspill


---

