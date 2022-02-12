---
title: "Case: Left Bunny / Right Thumb"
name: Left Bunny / Right Thumb
short_name: lbunny_rthumb
top: Bunny
top_short_name: bunny
top_lr: Left
bot: Thumb
bot_short_name: thumb
bot_lr: Right

optimal: 4

recognition: Breaking bunny/thumb; preserving tents on top and putting slice between shell and gem on bottom breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "1,0/3,0/-3,0/-4,-1/0,1"
  description: Put shell of thumb in DL and align so slice breaks gem, preserve both tents in UL (goes to scottie/bird).

# RELATED CASES
parents:
  -
    name: "Right Scottie / Left Bird"
    short_name: "rscottie_lbird"
  -
    name: "Right Spill / Right Axe"
    short_name: "rspill_raxe"
mirrors:
  top_bot:
    -
      name: Right Thumb / Left Bunny
      short_name: rthumb_lbunny
  lr:
    -
      name: Right Bunny / Left Thumb
      short_name: rbunny_lthumb
  pseudo:
    -
      name: Right Bunny / Right Thumb
      short_name: rbunny_rthumb
    -
      name: Left Bunny / Left Thumb
      short_name: lbunny_lthumb


---

