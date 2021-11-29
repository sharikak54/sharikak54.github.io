---
title: "Case: Shell / Shell"
name: Shell / Shell
short_name: shell_shell
top: Shell
top_short_name: shell
bot: Shell
bot_short_name: shell

optimal: 4

recognition:

# ALGORITHMS
default_alg:
  alg: "0,-1/4,1/-1,2/6,3/0,1"
  description: Preserve shell on bottom; send tent from top to form gem/snoopy.
color_mirror_algs:
  -
    alg: "0,-1/4,1/-1,2/0,-3/0,1"
  -
    alg: "0,-1/4,1/-4,-1/3,0/0,1"
  -
    alg: "-5,0/-4,-1/1,-2/0,3/-1,0"
  -
    alg: "-5,0/-4,-1/4,1/-3,0/-1,0"
other_algs:
  -
    alg: "-5,0/-4,-1/1,-2/6,-3/-1,0"
  -
    alg: "-5,0/-4,-1/4,1/3,6/-1,0"

# RELATED CASES
parents:
  -
    name: "Gem / Left Snoopy"
    short_name: "gem_lsnoopy"
  -
    name: "Gem / Right Snoopy"
    short_name: "gem_rsnoopy"
---

