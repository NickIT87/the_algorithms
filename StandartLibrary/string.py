#!/usr/bin/python3

s = 'the quick brown fox jumped over the lazy dog.'
f = s.upper()
print( f )

string_ = "Revert me please:)"

def method_1(string_):
    return string_[::-1]
    
def method_2(string_):
    mystr = ""
    for i in string_:
        mystr = i + mystr
    return mystr
    
def method_3(string_):
    if len(string_) == 0:
        return string_
    else:
        return method_3(string_[1:]) + string_[0]
    
print("1 -->", method_1(string_))
print("2 -->", method_2(string_))
print("3 -->", method_3(string_))
