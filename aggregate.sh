#!/bin/bash

mkdir "./matching"
mkdir "./matching/tornet.plot.data"

mkdir "./discount"
mkdir "./discount/tornet.plot.data"

mkdir "./vanilla"
mkdir "./vanilla/tornet.plot.data"

python_script="./aggregate.py"
arg1="matching"
python3 "$python_script" "$arg1"

arg2="discount"
python3 "$python_script" "$arg2"

arg3="vanilla"
python3 "$python_script" "$arg3"

