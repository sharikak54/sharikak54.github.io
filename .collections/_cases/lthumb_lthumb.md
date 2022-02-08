---
title: "Case: Left Thumb / Left Thumb"
name: Left Thumb / Left Thumb
short_name: lthumb_lthumb
top: Thumb
top_short_name: thumb
top_lr: Left
bot: Thumb
bot_short_name: thumb
bot_lr: Left

optimal: 2

recognition: Good thumbs; thumbs are the same as each other, or making a kite on one face makes a kite on the other face.

# ALGORITHMS
default_alg:
  alg: "1,0/-4,-1/0,1"
  description: Keep bottom shell in DL, pair gem on top with isolated corner on bottom to form kite/kite.
color_mirror_algs:
  -
    alg: "1,0/2,5/0,1"
  -
    alg: "-5,6/5,2/0,1"
    alg: "-5,6/5,2/0,1"
other_algs:
  -
    alg: "-5,6/-1,-4/0,1"
# RELATED CASES
parents:
  -
    name: "Left Kite / Left Kite"
    short_name: "lkite_lkite"
mirrors:
  lr:
    -
      name: Right Thumb / Right Thumb
      short_name: rthumb_rthumb
  pseudo:
    -
      name: Right Thumb / Left Thumb
      short_name: rthumb_lthumb
    -
      name: Left Thumb / Right Thumb
      short_name: lthumb_rthumb


---

