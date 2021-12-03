---
title: "Case: Right Baron / Left Baron"
name: Right Baron / Left Baron
short_name: rbaron_lbaron
top: Baron
top_short_name: baron
top_lr: Right
bot: Baron
bot_short_name: baron
bot_lr: Left

optimal: 5

recognition: Bad baron/baron; preserving tents breaks cubeshape.

# ALGORITHMS
default_alg:
  alg: "1,0/2,2/0,-3/3,0/1,4/-1,0"
  description: Put all 4 tents on right half of puzzle and slice with either alignment into m2; goes to preserving baron/dish or preserving dish/baron.
other_algs:
  -
    alg: "1,0/2,-1/0,3/-3,0/4,1/-1,0"
  -
    alg: "0,-1/-2,-2/3,0/0,-3/-4,-1/0,1"
  -
    alg: "0,-1/1,-2/-3,0/0,3/-1,-4/0,1"

# RELATED CASES
parents:
  -
    name: "Left Baron / Right Dish"
    short_name: "lbaron_rdish"
  -
    name: "Left Dish / Right Baron"
    short_name: "ldish_rbaron"
  -
    name: "Moth / Left Zero"
    short_name: "moth_lzero"
  -
    name: "Left Snoopy / Angel"
    short_name: "lsnoopy_angel"
  -
    name: "Plane / Right Zero"
    short_name: "plane_rzero"
  -
    name: "Left Scottie / Hazard"
    short_name: "lscottie_hazard"
mirrors:
  lr:
    -
      name: Left Baron / Right Baron
      short_name: lbaron_rbaron
  pseudo:
    -
      name: Left Baron / Left Baron
      short_name: lbaron_lbaron
    -
      name: Right Baron / Right Baron
      short_name: rbaron_rbaron


---

