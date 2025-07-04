#!/bin/bash
file=$1
echo "Running steg tools on $file..."
binwalk $file
strings $file | grep flag
steghide extract -sf $file -p ''
