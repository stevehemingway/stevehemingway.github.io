#!/bin/sh

for i in *.md 
do
	sed -i '1 a date: 2020-03-30' $i
done

