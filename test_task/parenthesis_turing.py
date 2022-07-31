def isValid(s: str) -> bool:
    result = None

    for i in range(len(s)):
        try:
            trigger = s[i] + s[i+1] 
            if trigger in ["(]", "(}", "[)", "[}", "{)", "{]"]:
                return False
            else:
                result = True
        except:
            pass

    return result


if __name__ == "__main__":
    line = input()
    if isValid(line):
        print("valid")
    else:
        print("invalid")