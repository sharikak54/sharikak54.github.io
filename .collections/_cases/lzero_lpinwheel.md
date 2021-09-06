---
name: Left Zero / Left Pinwheel
short_name: lzero_lpinwheel
top: Zero
top_short_name: zero
top_lr: Left
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Left

optimal: 4

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "1,0/-1,-4/-3,3/4,1/-1,0"
  description: TODO
other_algs:
  -
    alg: "1,3/-4,-1/-3,3/-5,-2/-1,0"
    description: TODO
  -
    alg: "0,-1/-3,3/1,1/2,-1/0,3/0,1"
    description: TODO
  -
    alg: "0,2/-3,3/1,1/-4,-1/-3,0/0,1"
    description: TODO

# RELATED CASES
parents:
  -
    name: TODO
    short_name: TODO
mirrors:
  top_bot:
    -
      name: Left Pinwheel / Left Zero
      short_name: lpinwheel_lzero
  lr:
    -
      name: Right Zero / Right Pinwheel
      short_name: rzero_rpinwheel
  pseudo:
    -
      name: Right Zero / Left Pinwheel
      short_name: rzero_lpinwheel
    -
      name: Left Zero / Right Pinwheel
      short_name: lzero_rpinwheel


---

Notes: aligned zero/n; optimal intentionally misaligns both layers to go to good baron/baron, but aligning both is still plenty fast

Description TODO

