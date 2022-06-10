from glob import glob
import sys

for i in glob('*.md'):
    print(i)