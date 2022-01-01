#!/bin/bash

echo "Hi!"
date
NAME='Alexis'

echo 'My name is' $NAME 
# input data command
read -p "Enter your name and age: " USRNAME AGE

echo "Hello" $USRNAME $AGE

if [ $AGE == "21" ];
then
    echo "your age is ok"
elif [ $AGE -lt "18" ];
then
    echo "your age is illegal"
elif [ $AGE -gt "18" ];
then
    echo "your age is legal"
else
    echo "none of the age"
fi

test=12
if [ $test == 12 ];
then
    echo $test
fi