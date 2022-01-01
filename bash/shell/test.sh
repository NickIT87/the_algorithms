#!/bin/bash

if [ -d /run/media/salamander/F29EADFA9EADB80D/programming/the_algorithms/bash/shell ];
then
    echo "Yes directory exists"
else
    echo "The directory does not exist"
fi

if [ -e /run/media/salamander/F29EADFA9EADB80D/programming/the_algorithms/bash/shell/hello.sh ];
then
    echo "file exists"
else
    echo "The file does not exist"
fi
