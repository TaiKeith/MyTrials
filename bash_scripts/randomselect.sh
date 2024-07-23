#!/usr/bin/bash
#LUCKY NUMBER GUESS GAME
#This is a script that selects a random number or person from a pool
echo "Hello"
sleep 2
echo "Welcome members"
sleep 1
echo "Let us find out who the lucky person is."
sleep 1
echo "Please pick a number between 0-9. (0/9)"
luck=$(( $RANDOM % 10 ))
read input

if [[ $luck == $input ]]; then
	echo "BINGO!!!!! You are the LUCKY WINNER!!!!!"
else
	echo "You were ALMOST there. Better luck next time"
fi
#END
