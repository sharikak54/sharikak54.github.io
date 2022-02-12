---
title: "Case: Left Kite / Right Kite"
name: Left Kite / Right Kite
short_name: lkite_rkite
top: Kite
top_short_name: kite
top_lr: Left
bot: Kite
bot_short_name: kite
bot_lr: Right

optimal: 5

recognition: Bad kites; not the 1-slicer.

# ALGORITHMS
default_alg:
  alg: "1,0/0,3/-4,-1/-2,1/-3,0/-1,0"
  description: Preserve kite on bottom, send single corner to bottom to form gem/gem.
color_mirror_algs:
  -
    alg: "samecase"
other_algs:
  -
    alg: "1,0/0,3/-4,-1/-3,0/-2,1/-1,0"
  -
    alg: "1,0/2,-1/4,1/3,0/2,-1/0,1"
  -
    alg: "1,0/2,-1/4,1/2,-1/3,0/0,1"

# RELATED CASES
parents:
  -
    name: "Gem / Gem"
    short_name: "gem_gem"
  -
    name: "Shell / Shell"
    short_name: "shell_shell"
mirrors:
  lr:
    -
      name: Right Kite / Left Kite
      short_name: rkite_lkite
  pseudo:
    -
      name: Right Kite / Right Kite
      short_name: rkite_rkite
    -
      name: Left Kite / Left Kite
      short_name: lkite_lkite


---

