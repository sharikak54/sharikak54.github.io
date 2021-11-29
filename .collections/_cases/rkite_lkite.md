---
title: "Case: Right Kite / Left Kite"
name: Right Kite / Left Kite
short_name: rkite_lkite
top: Kite
top_short_name: kite
top_lr: Right
bot: Kite
bot_short_name: kite
bot_lr: Left

optimal: 5

recognition: bad kite/kite; not the 1-slicer

# ALGORITHMS
default_alg:
  alg: "0,-1/-2,1/-4,-1/-2,1/-3,0/-1,0"
  description: preserve kite on bottom, send single corner to bottom to form gem/gem
other_algs:
  -
    alg: "0,-1/-2,1/-4,-1/-3,0/-2,-1/-1,0"

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
      name: Left Kite / Right Kite
      short_name: lkite_rkite
  pseudo:
    -
      name: Left Kite / Left Kite
      short_name: lkite_lkite
    -
      name: Right Kite / Right Kite
      short_name: rkite_rkite


---

