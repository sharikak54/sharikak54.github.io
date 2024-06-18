---
title: "Case: Right Bunny / Left Bunny"
name: Right Bunny / Left Bunny
short_name: rbunny_lbunny
top: Bunny
top_short_name: bunny
top_lr: Right
bot: Bunny
bot_short_name: bunny
bot_lr: Left

optimal: 5

recognition: Bad bunnies; preserving tents breaks cubeshape.

# ALGORITHMS
default_alg:
  alg: "1,0/2,2/-3,0/0,3/4,1/-1,0"
  description: Dabs / Bunnies
other_algs:
  -
    alg: "1,0/-1,2/3,0/0,-3/1,4/-1,0"
  -
    alg: "0,-1/-2,-2/0,3/-3,0/-1,-4/0,1"
  -
    alg: "0,-1/-2,1/0,-3/3,0/-4,-1/0,1"

# RELATED CASES
parents:
  -
    name: "Left Bunny / Right Thumb"
    short_name: "lbunny_rthumb"
  -
    name: "Left Thumb / Right Bunny"
    short_name: "lthumb_rbunny"
  -
    name: "Tie / Right Cut"
    short_name: "tie_rcut"
  -
    name: "Right Axe / Squid"
    short_name: "raxe_squid"
  -
    name: "Tree / Left Cut"
    short_name: "tree_lcut"
  -
    name: "Right Scottie / Hazard"
    short_name: "rscottie_hazard"
mirrors:
  lr:
    -
      name: Left Bunny / Right Bunny
      short_name: lbunny_rbunny
  pseudo:
    -
      name: Left Bunny / Left Bunny
      short_name: lbunny_lbunny
    -
      name: Right Bunny / Right Bunny
      short_name: rbunny_rbunny


---

