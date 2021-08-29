---
name: Right Scottish Terrier / Left Bird
short_name: rscottie_lbird
top: Scottish Terrier
top_short_name: scottie
top_lr: Right
bot: Bird
bot_short_name: bird
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
    type: top_bot
    values: 
      -
        name: Left Bird / Right Scottish Terrier
        short_name: lbird_rscottie
  -
    type: lr
    values: 
      -
        name: Left Scottish Terrier / Right Bird
        short_name: lscottie_rbird
  -
    type: pseudo
    values: 
      -
        name: Left Scottish Terrier / Left Bird
        short_name: lscottie_lbird
      -
        name: Right Scottish Terrier / Right Bird
        short_name: rscottie_rbird


---

Description TODO

