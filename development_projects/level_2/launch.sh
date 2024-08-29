#!/bin/bash

source ../venv/Scripts/activate


python ./server.py &
SERVER_ID=$!
sleep 5


python ./client.py 1:4 a &
C1=$!
python ./client.py 5:8 b &
C2=$!
python ./client.py 9:12 c &
C3=$!
wait $C1 
wait $C2 
wait $C3 

kill $SERVER_ID
wait $SERVER_ID



