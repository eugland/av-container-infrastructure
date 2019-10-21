#!/bin/bash
STR="0,0,0,0,0"
for i in {1..250}
do
    # echo $STR
    STR=$(curl localhost:5000/run/$STR)
done
