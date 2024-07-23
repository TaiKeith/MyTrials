#!/usr/bin/bash

echo "Hello"
sleep 1
echo "What is your name?"
read name
if [[ $name == "Keith" ]]; then
       	echo "Welcome $name."
else
	echo "Error, ACCESS DENIED"
fi
#END
