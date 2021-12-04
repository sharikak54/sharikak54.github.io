---
title: "Case: Right Zero / Right Kite"
name: Right Zero / Right Kite
short_name: rzero_rkite
top: Zero
top_short_name: zero
top_lr: Right
bot: Kite
bot_short_name: kite
bot_lr: Right

optimal: 6

recognition: Bad zero/kite; aligning bird with kite preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/3,0/2,2/-2,1/3,0/-1,0"
  description: Preserve kite on bottom, send isolated corner to form bad spill/spill.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "4,0/-3,3/3,0/-4,-1/4,1/-3,0/-1,0"

# RELATED CASES
parents:
  -
    name: "Left Spill / Left Spill"
    short_name: "lspill_lspill"
  -
    name: "Right Bird / Right Bird"
    short_name: "rbird_rbird"
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
    name: "Right Snoopy / Right Snoopy"
    short_name: "rsnoopy_rsnoopy"
  -
    name: "Right Scottie / Right Scottie"
    short_name: "rscottie_rscottie"
mirrors:
  top_bot:
    -
      name: Right Kite / Right Zero
      short_name: rkite_rzero
  lr:
    -
      name: Left Zero / Left Kite
      short_name: lzero_lkite
  pseudo:
    -
      name: Left Zero / Right Kite
      short_name: lzero_rkite
    -
      name: Right Zero / Left Kite
      short_name: rzero_lkite


---

