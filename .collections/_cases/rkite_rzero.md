---
title: "Case: Right Kite / Right Zero"
name: Right Kite / Right Zero
short_name: rkite_rzero
top: Kite
top_short_name: kite
top_lr: Right
bot: Zero
bot_short_name: zero
bot_lr: Right

optimal: 6

recognition: Bad kite/zero; aligning kite with bird preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/0,-3/-3,0/2,-1/-2,1/3,0/-1,0"
  description: Solve CO into 1e/1e.

# RELATED CASES
parents:
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
    name: "Left Spill / Left Spill"
    short_name: "lspill_lspill"
  -
    name: "Right Bird / Right Bird"
    short_name: "rbird_rbird"
  -
    name: "Right Scottie / Right Scottie"
    short_name: "rscottie_rscottie"
mirrors:
  top_bot:
    -
      name: Right Zero / Right Kite
      short_name: rzero_rkite
  lr:
    -
      name: Left Kite / Left Zero
      short_name: lkite_lzero
  pseudo:
    -
      name: Left Kite / Right Zero
      short_name: lkite_rzero
    -
      name: Right Kite / Left Zero
      short_name: rkite_lzero


---

