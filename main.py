
#def round6(num: float):
    #"""This function has a bug in it"""
    #return int(num + .6)


def upper_lower(text):
    """
    Checks if a given string contains an occurrence
    of upper case letter followed by lower case letter.
    Returns True if such thing exists, False otherwise.
    """
    for i in range(len(text) - 1):
        if text[i].isupper():
            if text[i+1].islower():
                return True
    return False

# ---- automated unit test ----

assert upper_lower("lowlow") == False
assert upper_lower("blaBla") == True
assert upper_lower("blabLa") == True
assert upper_lower("byE") == False
assert upper_lower("Hello") == True
assert upper_lower("BOOM") == False
assert upper_lower("") == False

print("All tests passed!")