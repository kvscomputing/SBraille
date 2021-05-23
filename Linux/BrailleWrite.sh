#!/bin/bash
> BrailleOutputs.txt
sh BrailleRead.sh | tee -a /home/pi/python/BrailleOutputs.txt
echo finished
