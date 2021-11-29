---
title: "Case: Right Bird / Shell"
name: Right Bird / Shell
short_name: rbird_shell
top: Bird
top_short_name: bird
top_lr: Right
bot: Shell
bot_short_name: shell

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/4,1/2,5/0,1"
  description: preserve shell on bottom, pair with gem on top to form whale/tent
color_mirror_algs:
  -
    alg: "0,-1/-3,0/4,1/-4,-1/0,1"
  -
    alg: "4,3/2,-1/4,1/-1,-4/0,1"
  -
    alg: "-2,-3/-1,2/4,1/-4,-1/0,1"
other_algs:
  -
    alg: "4,3/2,-1/4,1/5,2/0,1"
  -
    alg: "-2,-3/-1,2/4,1/2,5/0,1"

# RELATED CASES
parents:
  -
    name: "Left Whale / Right Tent"
    short_name: "lwhale_rtent"
mirrors:
  top_bot:
    -
      name: Shell / Right Bird
      short_name: shell_rbird
  lr:
    -
      name: Left Bird / Shell
      short_name: lbird_shell


---

