---
name: Left Bird / Right Scottish Terrier
short_name: lbird_rscottie
top: Bird
top_short_name: bird
top_lr: Left
bot: Scottish Terrier
bot_short_name: scottie
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
        name: Right Scottish Terrier / Left Bird
        short_name: rscottie_lbird
  -
    type: lr
    values: 
      -
        name: Right Bird / Left Scottish Terrier
        short_name: rbird_lscottie
  -
    type: pseudo
    values: 
      -
        name: Right Bird / Right Scottish Terrier
        short_name: rbird_rscottie
      -
        name: Left Bird / Left Scottish Terrier
        short_name: lbird_lscottie


---

Description TODO

