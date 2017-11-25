#!/bin/bash

I=0
CNT=100
RC=0

while [[ ${RC} -eq 0 ]] && [[ ${I} -lt ${CNT} ]]
do
	I=$((${I} + 1))
	./qsort.py > /dev/null
	RC=$?
done

if [[ ${I} -eq ${CNT} ]]
then
	echo "PASS"
else
	echo "FAIL"
fi

