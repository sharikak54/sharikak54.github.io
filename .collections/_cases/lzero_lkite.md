---
title: "Case: Left Zero / Left Kite"
name: Left Zero / Left Kite
short_name: lzero_lkite
top: Zero
top_short_name: zero
top_lr: Left
bot: Kite
bot_short_name: kite
bot_lr: Left

optimal: 6

recognition: Bad zero/kite; aligning bird with kite preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/3,0/-3,0/-2,-2/2,-1/-3,0/0,1"
  description: Preserve kite on bottom, send isolated corner to form bad spill/spill.
other_algs:
  -
    alg: "-3,-1/-2,4/3,0/-4,-1/4,1/-3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Spill / Right Spill"
    short_name: "rspill_rspill"
  -
    name: "Left Bird / Left Bird"
    short_name: "lbird_lbird"
  -
    name: "1E / 1E"
    short_name: "1e_1e"
  -
    name: "3E / 3E"
    short_name: "3e_3e"
  -
    name: "1C / 1C"
    short_name: "1c_1c"
  -
    name: "3C / 3C"
    short_name: "3c_3c"
  -
    name: "Left Snoopy / Left Snoopy"
    short_name: "lsnoopy_lsnoopy"
  -
    name: "Left Scottie / Left Scottie"
    short_name: "lscottie_lscottie"
mirrors:
  top_bot:
    -
      name: Left Kite / Left Zero
      short_name: lkite_lzero
  lr:
    -
      name: Right Zero / Right Kite
      short_name: rzero_rkite
  pseudo:
    -
      name: Right Zero / Left Kite
      short_name: rzero_lkite
    -
      name: Left Zero / Right Kite
      short_name: lzero_rkite


---

