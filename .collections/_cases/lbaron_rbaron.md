---
title: "Case: Left Baron / Right Baron"
name: Left Baron / Right Baron
short_name: lbaron_rbaron
top: Baron
top_short_name: baron
top_lr: Left
bot: Baron
bot_short_name: baron
bot_lr: Right

optimal: 5

recognition: Bad baron/baron; preserving tents breaks cubeshape.

# ALGORITHMS
default_alg:
  alg: "1,0/2,2/-3,0/0,3/4,1/-1,0"
  description: Put all 4 tents on right half of puzzle and slice with either alignment into m2; goes to preserving baron/dish or preserving dish/baron.
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
    name: "Right Baron / Left Dish"
    short_name: "rbaron_ldish"
  -
    name: "Right Dish / Left Baron"
    short_name: "rdish_lbaron"
  -
    name: "Moth / Right Zero"
    short_name: "moth_rzero"
  -
    name: "Right Snoopy / Angel"
    short_name: "rsnoopy_angel"
  -
    name: "Plane / Left Zero"
    short_name: "plane_lzero"
  -
    name: "Right Scottie / Hazard"
    short_name: "rscottie_hazard"
mirrors:
  lr:
    -
      name: Right Baron / Left Baron
      short_name: rbaron_lbaron
  pseudo:
    -
      name: Right Baron / Right Baron
      short_name: rbaron_rbaron
    -
      name: Left Baron / Left Baron
      short_name: lbaron_lbaron


---

