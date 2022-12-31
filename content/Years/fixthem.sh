#!/bin/bash

for i in *.md
do
	sed -i '1 a category: politics' "$i"
done

