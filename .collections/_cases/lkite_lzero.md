---
title: "Case: Left Kite / Left Zero"
name: Left Kite / Left Zero
short_name: lkite_lzero
top: Kite
top_short_name: kite
top_lr: Left
bot: Zero
bot_short_name: zero
bot_lr: Left

optimal: 6

recognition: bad kite/zero; aligning kite with bird preserves squareshape

# ALGORITHMS
default_alg:
  alg: "0,-1/1,-2/-3,0/2,-1/-2,1/3,0/-1,0"
  description: just solve CO -> 1e1e

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
    name: "Left Snoopy / Left Snoopy"
    short_name: "lsnoopy_lsnoopy"
  -
    name: "Right Spill / Right Spill"
    short_name: "rspill_rspill"
  -
    name: "Left Bird / Left Bird"
    short_name: "lbird_lbird"
  -
    name: "Left Scottie / Left Scottie"
    short_name: "lscottie_lscottie"
mirrors:
  top_bot:
    -
      name: Left Zero / Left Kite
      short_name: lzero_lkite
  lr:
    -
      name: Right Kite / Right Zero
      short_name: rkite_rzero
  pseudo:
    -
      name: Right Kite / Left Zero
      short_name: rkite_lzero
    -
      name: Left Kite / Right Zero
      short_name: lkite_rzero


---

