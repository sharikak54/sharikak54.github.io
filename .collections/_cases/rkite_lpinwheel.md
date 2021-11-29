---
title: "Case: Right Kite / Left Pinwheel"
name: Right Kite / Left Pinwheel
short_name: rkite_lpinwheel
top: Kite
top_short_name: kite
top_lr: Right
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Left

optimal: 4

recognition: bad kite/pinwheel - aligning blocks to slice breaks squareshape

# ALGORITHMS
default_alg:
  alg: "0,-1/1,-5/2,-1/-3,0/0,1"
  description: pair edge on top with tent on bottom to form snoopy/gem

# RELATED CASES
parents:
  -
    name: "Gem / Left Snoopy"
    short_name: "gem_lsnoopy"
  -
    name: "Left Scottie / Shell"
    short_name: "lscottie_shell"
  -
    name: "Right Whale / Left Tent"
    short_name: "rwhale_ltent"
  -
    name: "Plane / Moth"
    short_name: "plane_moth"
mirrors:
  top_bot:
    -
      name: Left Pinwheel / Right Kite
      short_name: lpinwheel_rkite
  lr:
    -
      name: Left Kite / Right Pinwheel
      short_name: lkite_rpinwheel
  pseudo:
    -
      name: Left Kite / Left Pinwheel
      short_name: lkite_lpinwheel
    -
      name: Right Kite / Right Pinwheel
      short_name: rkite_rpinwheel


---

