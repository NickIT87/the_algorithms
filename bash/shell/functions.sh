#!/bin/bash

PWD="/run/media/salamander/F29EADFA9EADB80D/programming/the_algorithms/bash/shell/names.txt"

function test() {
    if [ -e $PWD ];
    then
        echo "Names exists"
    else
        echo "File does not exist"
    fi
}

test2() {
    echo $PWD
}

# functions call 
test
test2