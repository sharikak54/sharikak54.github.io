---
title: "Case: Left Cut / Left Kite"
name: Left Cut / Left Kite
short_name: lcut_lkite
top: Cut
top_short_name: cut
top_lr: Left
bot: Kite
bot_short_name: kite
bot_lr: Left

optimal: 6

recognition: Bad cut/kite; aligning bird with kite preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/3,0/-3,0/-2,-2/2,-1/-3,0/0,1"
  description: Preserve kite on bottom, send isolated corner to form bad spill/spill.
color_mirror_algs:
  -
    alg: "samecase"
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
    name: "Left Axe / Left Axe"
    short_name: "laxe_laxe"
  -
    name: "Left Scottie / Left Scottie"
    short_name: "lscottie_lscottie"
mirrors:
  top_bot:
    -
      name: Left Kite / Left Cut
      short_name: lkite_lcut
  lr:
    -
      name: Right Cut / Right Kite
      short_name: rcut_rkite
  pseudo:
    -
      name: Right Cut / Left Kite
      short_name: rcut_lkite
    -
      name: Left Cut / Right Kite
      short_name: lcut_rkite


---

