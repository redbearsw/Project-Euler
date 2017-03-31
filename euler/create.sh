#!/bin/bash

if [ -e "p$1.c" ]; then
	echo "File p$1.c already exists!"
else
	echo  "#include <stdio.h>\n#include <stdlib.h>\n\nint p$1 () {\n}\n\nint main() {\n}" >> p$1.c
fi
