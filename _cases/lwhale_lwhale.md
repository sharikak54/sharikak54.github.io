---
name: Left Whale / Left Whale
short_name: lwhale_lwhale
top: Whale
top_short_name: whale
top_lr: Left
bot: Whale
bot_short_name: whale
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
        name: Right Whale / Right Whale
        short_name: rwhale_rwhale
  -
    type: pseudo
    values: 
      -
        name: Right Whale / Left Whale
        short_name: rwhale_lwhale
      -
        name: Left Whale / Right Whale
        short_name: lwhale_rwhale


---

Description TODO

