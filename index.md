---
layout: default
title: Home
---

## What is OBL?
OBL stands for "Orient Both Layers".  The most common method for solving the Square-1, the Vandenbergh Method, breaks down the puzzle into 5 steps:
1. Form cubeshape
2. Orient all corners
3. Orient all edges
4. Permute all corners
5. Permute all edges

OBL combines steps 2 and 3 above into one step.  We do it for 3x3, so why not for Square-1?

### Some history
Before about 2015, this idea had been considered but was immediately dismissed as "too many cases".  Shari didn't believe this, and started mathing out how many cases there actually are.  She produced a full OBL tree of 74 cases, with only two cases taking more than 5 slices optimal to solve, and hosted it on her personal Caltech website (which expired after her graduation) winter 2015.

However, initial resources were fairly minimal at the time (essentially just the original OBL tree) - Not Kevin was manually figuring out the method, but neither dedicated time to recording further results, so it never took off.  Some people tried to fill the resource void - most notably, Paul Besci's [video walkthrough](https://www.youtube.com/watch?v=506oBmtuYcU) and Stefan Lidström's [computer-generated table](http://hem.bredband.net/_zlv_/rubiks/sq1/sq1-obl.html) - but eventually people moved on to other ways of improving their times, such as resolving parity during cubeshape, or CSP (which was in its infancy at the time).

Fast forward to 2020 - at this point, CSP has been proven to be not only doable, but almost essential for world-class solving.  Naturally, cubers started looking for ways to improve on CSP Vandenbergh, and started looking more seriously at OBL once again.  Combined with some significant steps in Permiting Both Layers, or PBL (now feasible due to CSP eliminating all parity cases), "3-look Vandenbergh" became more and more appealing.

With the increased interest in OBL, Not Kevin started looking into the right way to disseminate all the personal knowledge he had developed, particularly from a competitive cuber's perspective.  While talking with Shari, it became clear that a website (with its ability to go in-depth on specific cases while providing summaries on other pages, as well as links between related concepts) would be more effective than existing attempts, and here we are :)

## Why OBL?
Okay, I hear you saying that 74 cases is still a lot.  That may be true, but hear me out:
* Most OBL cases (just over 70%) are optimal 4 slices or less -- the average slicecount for OBL, weighted by probability of appearing, is actually _less_ than 4 -- and many of the 5-slicers are pure CO or EO, so you already know them!
* OBL is roughly as hard as full cubeshape:
  * Cubeshape has 65 unique cases with a max length of 7 (compared to OBL's 74 cases with a max length of 6), and
  * Both have the same tree-like property that each cubeshape/OBL goes into another cubeshape/OBL - this means that your learning rate on OBL naturally speeds up as you recognize more cases, and learning one case will teach you every case on its way to solved.
* It's easy to build up your OBL skills without disrupting your times much - if you don't recognize a case immediately or you're not comfortable with the OBL yet, just do CO/EO :)
* Also, let's be honest - it's pretty awesome to solve OBL in half the slicecount that others do it :)

> **Not Kevin says:** The 6-slice optimal algs are optimal by just doing CO -> EO, so you already have 2 done :)

## Okay, how OBL?
Go to the [Start page](/start) to learn more!
