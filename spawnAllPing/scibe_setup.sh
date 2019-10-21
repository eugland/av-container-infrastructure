#!/bin/bash
docker build -t gausse:latest .

# inspect image 
# docker run --rm -it --entrypoint=/bin/bash name-of-image
# inspect running container
# docker exec -it name-of-container bash
# chown 101:101  /home/eugene/devspace/container/log
STR="0,0,0,0,0"
for i in {1..250}
do
    # echo $STR
    STR=$(docker run -v /home/eugene/devspace/container/log:/home/eugene/devspace/container/    gausse $STR )
done
