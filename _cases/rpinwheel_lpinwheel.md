---
name: Right Pinwheel / Left Pinwheel
short_name: rpinwheel_lpinwheel
top: Pinwheel
top_short_name: pinwheel
top_lr: Right
bot: Pinwheel
bot_short_name: pinwheel
bot_lr: Left

recognition: TODO

# ALGORITHMS
default_alg:
  alg: "0,0/"
  description: TODO
mirror_algs:
  -
    alg: "0,0/"
    description: TODO
other_algs:
  -
    alg: "0,0/"
    description: TODO

# RELATED CASES
parents:
  -
    name: TODO
    short_name: TODO
mirrors:
  -
    type: lr
    values: 
      -
        name: Left Pinwheel / Right Pinwheel
        short_name: lpinwheel_rpinwheel
  -
    type: pseudo
    values: 
      -
        name: Left Pinwheel / Left Pinwheel
        short_name: lpinwheel_lpinwheel
      -
        name: Right Pinwheel / Right Pinwheel
        short_name: rpinwheel_rpinwheel


---

Description TODO

