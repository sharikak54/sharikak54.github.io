---
title: "Case: Left Bunny / Right Bunny"
name: Left Bunny / Right Bunny
short_name: lbunny_rbunny
top: Bunny
top_short_name: bunny
top_lr: Left
bot: Bunny
bot_short_name: bunny
bot_lr: Right

optimal: 5

recognition: Bad bunnies; preserving tents breaks cubeshape.

# ALGORITHMS
default_alg:
  alg: "1,0/2,2/0,-3/3,0/1,4/-1,0"
  description: Put all 4 tents on right half of puzzle and slice with either alignment into m2; goes to preserving bunny/thumb or preserving thumb/bunny.
other_algs:
  -
    alg: "1,0/2,-1/0,3/-3,0/4,1/-1,0"
  -
    alg: "0,-1/-2,-2/3,0/0,-3/-4,-1/0,1"
  -
    alg: "0,-1/1,-2/-3,0/0,3/-1,-4/0,1"
    alg: "0,-1/-2,-2/3,0/0,-3/-4,-1/0,1"
  -
    alg: "0,-1/1,-2/-3,0/0,3/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Right Bunny / Left Thumb"
    short_name: "rbunny_lthumb"
  -
    name: "Right Thumb / Left Bunny"
    short_name: "rthumb_lbunny"
  -
    name: "Tie / Left Cut"
    short_name: "tie_lcut"
  -
    name: "Left Axe / Squid"
    short_name: "laxe_squid"
  -
    name: "Tree / Right Cut"
    short_name: "tree_rcut"
  -
    name: "Left Scottie / Hazard"
    short_name: "lscottie_hazard"
  -
    name: "Right Thumb / Left Bunny"
    short_name: "rthumb_lbunny"
  -
    name: "Tie / Left Cut"
    short_name: "tie_lcut"
  -
    name: "Left Axe / Squid"
    short_name: "laxe_squid"
  -
    name: "Tree / Right Cut"
    short_name: "tree_rcut"
  -
    name: "Left Scottie / Hazard"
    short_name: "lscottie_hazard"
mirrors:
  lr:
    -
      name: Right Bunny / Left Bunny
      short_name: rbunny_lbunny
  pseudo:
    -
      name: Right Bunny / Right Bunny
      short_name: rbunny_rbunny
    -
      name: Left Bunny / Left Bunny
      short_name: lbunny_lbunny


---

