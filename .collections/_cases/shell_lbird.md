---
title: "Case: Shell / Left Bird"
name: Shell / Left Bird
short_name: shell_lbird
top: Shell
top_short_name: shell
bot: Bird
bot_short_name: bird
bot_lr: Left

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/1,-2/-1,-4/4,1/-1,0"
  description: Swap tent from top with full bird on bottom.
other_algs:
  -
    alg: "6,5/-2,1/-1,-4/1,4/-1,0"
  -
    alg: "4,3/0,3/-1,-4/1,4/-1,0"
  -
    alg: "-2,-3/3,0/-1,-4/4,1/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Whale / Left Tent"
    short_name: "rwhale_ltent"
mirrors:
  top_bot:
    -
      name: Left Bird / Shell
      short_name: lbird_shell
  lr:
    -
      name: Shell / Right Bird
      short_name: shell_rbird


---

