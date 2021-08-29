---
name: Left Pinwheel / Left Pinwheel
short_name: lpinwheel_lpinwheel
top: Pinwheel
top_short_name: pinwheel
top_lr: Left
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
        name: Right Pinwheel / Right Pinwheel
        short_name: rpinwheel_rpinwheel
  -
    type: pseudo
    values: 
      -
        name: Right Pinwheel / Left Pinwheel
        short_name: rpinwheel_lpinwheel
      -
        name: Left Pinwheel / Right Pinwheel
        short_name: lpinwheel_rpinwheel


---

Description TODO

