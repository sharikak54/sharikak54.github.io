---
title: "Case: Right Thumb / Right Thumb"
name: Right Thumb / Right Thumb
short_name: rthumb_rthumb
top: Thumb
top_short_name: thumb
top_lr: Right
bot: Thumb
bot_short_name: thumb
bot_lr: Right

optimal: 2

recognition: Good thumbs; thumbs are the same as each other, or making a kite on one face makes a kite on the other face.

# ALGORITHMS
default_alg:
  alg: "0,-1/4,1/-1,0"
  description: Keep bottom shell in DL, pair gem on top with isolated corner on bottom to form kite/kite.
color_mirror_algs:
  -
    alg: "0,-1/-2,-5/-1,0"
  -
    alg: "6,5/5,2/-1,0"
    alg: "6,5/5,2/-1,0"
other_algs:
  -
    alg: "6,5/-1,-4/-1,0"
# RELATED CASES
parents:
  -
    name: "Right Kite / Right Kite"
    short_name: "rkite_rkite"
mirrors:
  lr:
    -
      name: Left Thumb / Left Thumb
      short_name: lthumb_lthumb
  pseudo:
    -
      name: Left Thumb / Right Thumb
      short_name: lthumb_rthumb
    -
      name: Right Thumb / Left Thumb
      short_name: rthumb_lthumb


---

