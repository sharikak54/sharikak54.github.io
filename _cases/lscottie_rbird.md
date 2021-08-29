---
name: Left Scottish Terrier / Right Bird
short_name: lscottie_rbird
top: Scottish Terrier
top_short_name: scottie
top_lr: Left
bot: Bird
bot_short_name: bird
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
    type: top_bot
    values: 
      -
        name: Right Bird / Left Scottish Terrier
        short_name: rbird_lscottie
  -
    type: lr
    values: 
      -
        name: Right Scottish Terrier / Left Bird
        short_name: rscottie_lbird
  -
    type: pseudo
    values: 
      -
        name: Right Scottish Terrier / Right Bird
        short_name: rscottie_rbird
      -
        name: Left Scottish Terrier / Left Bird
        short_name: lscottie_lbird


---

Description TODO

