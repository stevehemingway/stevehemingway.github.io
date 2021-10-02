#!/bin/bash

for i in *april*.md
do
	sed -i 's/2020-04-31/2020-04-30/' "$i"
done


