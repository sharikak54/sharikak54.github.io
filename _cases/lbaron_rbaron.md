---
name: Left Red Baron / Right Red Baron
short_name: lbaron_rbaron
top: Red Baron
top_short_name: baron
top_lr: Left
bot: Red Baron
bot_short_name: baron
bot_lr: Right

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
        name: Right Red Baron / Left Red Baron
        short_name: rbaron_lbaron
  -
    type: pseudo
    values: 
      -
        name: Right Red Baron / Right Red Baron
        short_name: rbaron_rbaron
      -
        name: Left Red Baron / Left Red Baron
        short_name: lbaron_lbaron


---

Description TODO

