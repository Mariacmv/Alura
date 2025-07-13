#!/bin/bash
loop=1

while [ $loop -le 5 ];do
	echo "$loop"
	((loop++))
	sleep 1
done
