# SHAKE256 (First project for [INF568 Advanced Cryptology](https://moodle.polytechnique.fr/course/view.php?id=2655) @ Ecole polytechnique)

This repository hosts my submission for the first project for INF568 @ Ecole polytechnique, which consists of implementing the SHAKE256 extendable output hash function following FIPS202 and finding collisions for small values of the output. The code is written in Python3.  
* __code__ contains the _.py_ source files.  
* __collisions-__**X** contains a several files of the format ex-*Y*.A or ex-*Y*.B, each containing a string the hash of which collides with the other.  

## Code structure
* **shake.py** is the main file for the hash function, the one you want import to compute hashes. It also implements the "sponge" algorithm.  
* **conversion.py** contains a several functions that make it easier to convert between ints, strings, bits, bytes, and lists of those.  
* **state.py** contains the State class where the permutation used in the "sponge" algorithm is implemented, along with a printing functions useful for debugging.  

* **collisions.py** implements a brute force approach to finding collusions on phrases of the form "The secret password is: <some number>". This is the script we use for N=8 and N=16.  
Time to find collision for N=8: 13.6636s.  
68 collisions are found for N=8.  
For N=16 the algorithm takes around two hours and finds over 10000 collisions, only some of which are included here.  

* **collisions2.py** implements Floyd's cycle finding algorithm on the set of messages of the form "The secret password is: <some number>" with <some number> being between 0 and (2^N)-1. To send an hash back to this set, we simply turn it into an integer and append it to ""The secret password is: ". This is the script we use for N=24 and N=32.  

  Time to find collision for N=24: 633.3119s.  
Time to find collision for N=24: 590.2657s.  
Time to find collision for N=24: 1387.1400s.  
Time to find collision for N=24: 763.8776s.  
Time to find collision for N=32: 5245.8591s.  
Time to find collision for N=32: 59348.9417s.  
Time to find collision for N=32: 49291.8220s.  

* **collisions3.py** implements Floyd's cycle finding algorithm when the set of messages is *N* predefined lines of text, with the *i* th line being followed by an extra ' ' iff *x* 's *i* th bit is 1, for *x* between 0 and (2^N)-1. This is the script we use for N=32.  

  Time to find collision for N=32: 37794.5170s.  
Time to find collision for N=32: 22826.5792s.  
Time to find collision for N=32: 42135.4453s.  


## Computing hashes
~~~~
>>> import shake
>>> shake.shake("INF568",256)
'c2a04900675df541c258c6f77d9b3946f525c4dc5709f390c5b999415c487a47299ac1f6d6f42a0
c2d21d79d4e2abea3e3f0117239965d967e9eeaf5425d76555c772e80da6db26c9fbdbfd5c6db9e2
e287644dc17769e39710ebd0c218dbf44b92be2b676b66f82ef09e4598f8a397274badf9312ebff4
c294d9dd0ff403166'
~~~~
