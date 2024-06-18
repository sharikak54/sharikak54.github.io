---
title: "Case: Shell / Right Bird"
name: Shell / Right Bird
short_name: shell_rbird
top: Shell
top_short_name: shell
bot: Bird
bot_short_name: bird
bot_lr: Right

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/-1,2/1,4/-4,-1/0,1"
  description: Swap tent from top with full bird on bottom.
other_algs:
  -
    alg: "-5,6/2,-1/1,4/-1,-4/0,1"
  -
    alg: "-3,-4/0,-3/1,4/-1,-4/0,1"
  -
    alg: "3,2/-3,0/1,4/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Left Whale / Right Tent"
    short_name: "lwhale_rtent"
mirrors:
  top_bot:
    -
      name: Right Bird / Shell
      short_name: rbird_shell
  lr:
    -
      name: Shell / Left Bird
      short_name: shell_lbird


---

