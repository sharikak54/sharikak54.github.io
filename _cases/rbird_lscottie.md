---
name: Right Bird / Left Scottish Terrier
short_name: rbird_lscottie
top: Bird
top_short_name: bird
top_lr: Right
bot: Scottish Terrier
bot_short_name: scottie
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
        name: Left Scottish Terrier / Right Bird
        short_name: lscottie_rbird
  -
    type: lr
    values: 
      -
        name: Left Bird / Right Scottish Terrier
        short_name: lbird_rscottie
  -
    type: pseudo
    values: 
      -
        name: Left Bird / Left Scottish Terrier
        short_name: lbird_lscottie
      -
        name: Right Bird / Right Scottish Terrier
        short_name: rbird_rscottie


---

Description TODO

