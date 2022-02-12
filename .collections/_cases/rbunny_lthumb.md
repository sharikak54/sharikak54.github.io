---
title: "Case: Right Bunny / Left Thumb"
name: Right Bunny / Left Thumb
short_name: rbunny_lthumb
top: Bunny
top_short_name: bunny
top_lr: Right
bot: Thumb
bot_short_name: thumb
bot_lr: Left

optimal: 4

recognition: Breaking bunny/thumb; preserving tents on top and putting slice between shell and gem on bottom breaks squareshape.

# ALGORITHMS
default_alg:
  alg: "0,-1/-3,0/3,0/4,1/-1,0"
  description: Put shell of thumb in DL and align so slice breaks gem, preserve both tents in UL (goes to scottie/bird).

# RELATED CASES
parents:
  -
    name: "Left Scottie / Right Bird"
    short_name: "lscottie_rbird"
  -
    name: "Left Spill / Left Axe"
    short_name: "lspill_laxe"
mirrors:
  top_bot:
    -
      name: Left Thumb / Right Bunny
      short_name: lthumb_rbunny
  lr:
    -
      name: Left Bunny / Right Thumb
      short_name: lbunny_rthumb
  pseudo:
    -
      name: Left Bunny / Left Thumb
      short_name: lbunny_lthumb
    -
      name: Right Bunny / Right Thumb
      short_name: rbunny_rthumb


---

