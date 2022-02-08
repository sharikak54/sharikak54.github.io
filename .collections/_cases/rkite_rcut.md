---
title: "Case: Right Kite / Right Cut"
name: Right Kite / Right Cut
short_name: rkite_rcut
top: Kite
top_short_name: kite
top_lr: Right
bot: Cut
bot_short_name: cut
bot_lr: Right

optimal: 6

recognition: Bad kite/cut; aligning kite with bird preserves squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/0,-3/-3,0/2,-1/-2,1/3,0/-1,0"
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
    name: "Right Axe / Right Axe"
    short_name: "raxe_raxe"
  -
    name: "Left Spill / Left Spill"
    short_name: "lspill_lspill"
  -
    name: "Right Bird / Right Bird"
    short_name: "rbird_rbird"
  -
    name: "Right Scottie / Right Scottie"
    short_name: "rscottie_rscottie"
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
      name: Right Cut / Right Kite
      short_name: rcut_rkite
  lr:
    -
      name: Left Kite / Left Cut
      short_name: lkite_lcut
  pseudo:
    -
      name: Left Kite / Right Cut
      short_name: lkite_rcut
    -
      name: Right Kite / Left Cut
      short_name: rkite_lcut


---

