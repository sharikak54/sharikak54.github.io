---
title: "Case: Left Bird / Shell"
name: Left Bird / Shell
short_name: lbird_shell
top: Bird
top_short_name: bird
top_lr: Left
bot: Shell
bot_short_name: shell

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/-4,-1/-2,-5/-1,0"
  description: Preserve shell on bottom, pair with gem on top to form whale/tent.
color_mirror_algs:
  -
    alg: "1,0/3,0/-4,-1/4,1/-1,0"
  -
    alg: "-3,-4/-2,1/-4,-1/1,4/-1,0"
  -
    alg: "3,2/1,-2/-4,-1/4,1/-1,0"
    alg: "-3,-4/-2,1/-4,-1/1,4/-1,0"
  -
    alg: "3,2/1,-2/-4,-1/4,1/-1,0"
other_algs:
  -
    alg: "-3,-4/-2,1/-4,-1/-5,-2/-1,0"
  -
    alg: "3,2/1,-2/-4,-1/-2,-5/-1,0"
    alg: "3,2/1,-2/-4,-1/-2,-5/-1,0"

# RELATED CASES
parents:
  -
    name: "Right Whale / Left Tent"
    short_name: "rwhale_ltent"
mirrors:
  top_bot:
    -
      name: Shell / Left Bird
      short_name: shell_lbird
  lr:
    -
      name: Right Bird / Shell
      short_name: rbird_shell


---

