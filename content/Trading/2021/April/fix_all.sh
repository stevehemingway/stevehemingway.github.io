#!/bin/bash -v

for i in *.md
	do
	mv $i $i.#
	uniq $i.# >$i
	done
