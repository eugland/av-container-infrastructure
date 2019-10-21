#!/bin/bash
STR="0,0,0,0,0"
start=`date +%s`
for i in {1..250}
do
    # echo $STR
    STR=$(python gausse.py $STR)
done
end=`date +%s`
runtime=$((end-start))
echo $runtime