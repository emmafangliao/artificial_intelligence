# QUESTION 1 

def five_x_cubed_plus_2(x):
    return 5*(x**3)+2


# QUESTION 2

def triple_up(x):
    n=0
    tripleList = []
    while n+2<=len(x):
        tripleList.append(x[n:n+3])
        n+=3
    if n<len(x):
        tripleList.append(x[n:])
    return tripleList


# QUESTION 3 

def mystery_code(x):
    mapping = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    newcode = ""
    for input in x:
        # alphabetical 
        if input.lower() in mapping:
            index = (mapping.index(input.lower()) + 21) % 26
            # alphabet originally in lower case
            if input.islower():
                newcode += mapping[index].upper()
            else:
                newcode +=mapping[index]
        else:
            newcode +=input

    return newcode
   

# QUESTION 4 

def future_tense(x):
    past = "ate had am went been is".split()
    verbs = "now yesterday today".split()
    future = "eat have be go be be".split()
    sentence = ""
    for input in x:
        if input.lower() in past:
            toAdd = "will " + future[past.index(input.lower())] + " "
            sentence += toAdd
        elif input.lower() in verbs:
            if input[0].isupper():
                sentence += "Tomorrow "
            else:
                sentence += "tomorrow "
        else:
            sentence += input + " "
    return sentence.split()


    



    
