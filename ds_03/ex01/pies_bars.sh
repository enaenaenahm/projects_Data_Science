#!/bin/bash
if [ -n "$VIRTUAL_ENV" ]; then
echo -e "\033[45m \033[0m \033[35mPies\033[0m   \033[41m \033[0m \033[31mBars\033[0m"
fi
termgraph data.txt --color {magenta,red} 
