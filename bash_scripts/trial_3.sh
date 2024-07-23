#!/usr/bin/bash
#elden ring
echo "Hello Ninja Samurai"
#first beast battle
beast=$(( $RANDOM % 10 ))
echo "Your first beast approaches. Prepare to battle. Pick a number between 0-9. (0/9)"
read input

if [[ $beast == $input ]]; then
	echo "Beast VANQUISHED!! Congrats"
else
	echo "You Died"
fi
#END
