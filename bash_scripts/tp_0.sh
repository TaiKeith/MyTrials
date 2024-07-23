#!/usr/bin/bash
#Personal Trial Project 0
echo "Hello"
sleep 2
echo "Please enter your name: $name"
read -s name
if [[ $name == "Lillian" ]]; then
	echo "Hello, $name. Please enter your pin"
else
	echo "UNAUTHORIZED USER.ERROR! ERROR!! ERROR!!!"
fi

read -s pin
if [[ $pin == "3142" ]]; then
	echo "Hello, $name. WELCOME"
else
	echo "LOGIN ERROR! INTRUDER!!!"
fi
