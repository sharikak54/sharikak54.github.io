---
title: "Case: Right Cut / Right Kite"
name: Right Cut / Right Kite
short_name: rcut_rkite
top: Cut
top_short_name: cut
top_lr: Right
bot: Kite
bot_short_name: kite
bot_lr: Right

optimal: 6

recognition: Bad cut/kite; aligning bird with kite preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/-3,0/3,0/2,2/-2,1/3,0/-1,0"
  description: Preserve kite on bottom, send isolated corner to form bad spill/spill.
color_mirror_algs:
  -
    alg: "samecase"
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
    name: "Right Axe / Right Axe"
    short_name: "raxe_raxe"
  -
    name: "Right Scottie / Right Scottie"
    short_name: "rscottie_rscottie"
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
    name: "Right Axe / Right Axe"
    short_name: "raxe_raxe"
  -
    name: "Right Scottie / Right Scottie"
    short_name: "rscottie_rscottie"
mirrors:
  top_bot:
    -
      name: Right Kite / Right Cut
      short_name: rkite_rcut
  lr:
    -
      name: Left Cut / Left Kite
      short_name: lcut_lkite
  pseudo:
    -
      name: Left Cut / Right Kite
      short_name: lcut_rkite
    -
      name: Right Cut / Left Kite
      short_name: rcut_lkite


---

