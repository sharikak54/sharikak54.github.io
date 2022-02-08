---
title: "Case: Left Kite / Left Cut"
name: Left Kite / Left Cut
short_name: lkite_lcut
top: Kite
top_short_name: kite
top_lr: Left
bot: Cut
bot_short_name: cut
bot_lr: Left

optimal: 6

recognition: Bad kite/cut; aligning kite with bird preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/1,-2/-3,0/2,-1/-2,1/3,0/-1,0"
  description: Solve CO into 1e/1e.
color_mirror_algs:
  -
    alg: "samecase"
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
    name: "Left Axe / Left Axe"
    short_name: "laxe_laxe"
  -
    name: "Right Spill / Right Spill"
    short_name: "rspill_rspill"
  -
    name: "Left Bird / Left Bird"
    short_name: "lbird_lbird"
  -
    name: "Left Scottie / Left Scottie"
    short_name: "lscottie_lscottie"
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
    name: "Left Axe / Left Axe"
    short_name: "laxe_laxe"
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
      name: Left Cut / Left Kite
      short_name: lcut_lkite
  lr:
    -
      name: Right Kite / Right Cut
      short_name: rkite_rcut
  pseudo:
    -
      name: Right Kite / Left Cut
      short_name: rkite_lcut
    -
      name: Left Kite / Right Cut
      short_name: lkite_rcut


---

