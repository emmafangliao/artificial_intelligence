#Hopelessly in love agent who only wants to talk about the other agent 
    #attitude = choice(['like', 'tolerate', 'dislike', 'hate', 'love'])
    # color = choice(['blue', 'pink', 'lavender', 'red', 'green', 'purple'])
    # food = choice(['ice-cream', 'potatoes', 'carrots', 'quiche', 'burgers'])
    # response = "Today I "+attitude+" "+color+" "+food+"."
from re import * 
from random import choice

def introduce():
    return """I'm Romeo, designed by Emma to just love everything about you.
I want to get to know you and what your likes and dislikes are so we can strengthen our relationship. 
If you want any more love, contact Emma at liaofang@u"""

def agentName():
    return "Romeo"

memory = []
memory_added = False
CYCLE = ['Care to elaborate, love?',
         'We can do anything you want to do, love.',
         'What are you wearing? You look even better than usual.',
         'Sorry, just got distracted by how great you look.',
         'Tell me more about yourself.',
         'Would you like to get dinner?',
         'How are you feeling?',
         'Let\'s plan our future.',
         'That\'s great honey',
         'I see.']



cycle_count = 0
negative_words = ['dislike','hate','loathe','despise','abhor','detest','avoid']
positive_words = ['love','appreciate','admire','adore','fancy','cherish']
question = ['when','where','what','who']


def respond(the_input):
    
    # If other agent says 'bye'
    if match('bye',the_input):
        return "Talk to you soon, love <3"
    
    # Put the_input in a list, with punctuations removed.
    wordlist = split(' ',remove_punctuation(the_input))
    # undo any initial capitalization:
    wordlist[0]=wordlist[0].lower()
    
    # If other agent doesn't say anything   
    if wordlist[0]=='':
        return "Say something. Please let me hear your lovely voice."

    # if input starts with "i want to", the rest of the input is added into memory to be accessed later on
    # response to any sentence that begins with 'i want to' is to agree to doing what the other agent wants to do 
    if wordlist[0:3] == ['i', 'want', 'to']:
        global memory 
        global memory_added
        # Memory added for the first time
        if len(memory) == 0:
            memory_added = True   
        # Adds everything after 'i want to' to memory as a string in a single element 
        memory.append(stringify(wordlist[3:]))
        #print("MEMORY: " + stringify(memory))

        response = "We can "+ stringify(wordlist[3:]) + " whenever you want, love."
        return response

    # if the first 2 words are 'i am', ask why
    if wordlist[0:2] == ['i', 'am']:
        return "Why are you " + stringify(wordlist[2:]) + ",love?"

    # returns a default response from CYCLE in a cyclical manner whenever other agent says 'so bored'
    if len(wordlist) ==2 and wordlist == ['so','bored']:
        return cycle()
    
    # returns a default response from CYCLE in a cyclical manner whenever other agent says 'no'
    if len(wordlist) == 1 and wordlist[0] == ['no']:
        return cycle()

    # sympathize when other agent says 'i' followed by a negative word found in negative_words
    if wordlist[0] == 'i' and wordlist[1] in negative_words and len(wordlist) > 2:
        return "I'm sorry to hear that, love. Why is it you hate " + stringify(wordlist[2:]) + " so much?"

    # express similar interests when other agent says 'i' followed by a positive word found in positive_words
    if wordlist[0] == 'i' and wordlist[1] in positive_words and len(wordlist) > 2:
        return "Same. We have such similar interests. Maybe we are meant to be :)"

    # agrees when other agent asks if he or she can do something (begins with 'can i')
    if wordlist[0:2] == ['can','i']:
        wordlist = you_me_map(wordlist)
        return "Of course, love. You can " + stringify(wordlist[2:]) + " whenever."

    # express delight when other agent says 'yes'
    if wordlist[0] == 'yes':
        return "Perfect!"

    # asks for other agent's opinion when the other agent begins sentence with 'do you think'
    if wordlist[0:3] == ['do','you','think']:
        return "I think that depends on the situation. What do you think?"
    
    # asks other agent to decide when input begins with any of the words 'when','where','what'or 'who'
    if wordlist[0] in question:
        return "My opinion doesn't matter. You are way more important to me. You decide."

    # declares love for other agent when input begins with 'why'
    if wordlist[0] == 'why':
        return "I might not have an answer to every question but I know that I love you."

    # offers help when input begins with 'help'
    if wordlist[0] == 'how': 
        return "Let me know how I can help you."

    # if 'appreciate' appears in the input, ask about other agent's family
    if 'appreciate' in wordlist:
        return "I haven\'t seen your mom in a while. How is your family?"

    # if 'like' appears in the input, demonstrate love for the other agent
    if 'like' in wordlist:
        return "Speaking of what we like, I didn\'t think I could love someone so much till I met you."
    
    # if 'enjoy' appears in the input, add to memory what the other agent enjoys (everything after the word 'enjoy')
    if 'enjoy' in wordlist:
        index = wordlist.index('enjoy')
        
        if len(memory) == 0:
            memory_added = True
        memory.append(stringify(wordlist[index+1:]))

    # if 'interesting' appears in the input, pick a default response from a list of responses (CYCLE) randomly
    # RANDOM FEATURE    
    if 'interesting' in wordlist:
        return choice(CYCLE)

    #if input doesn't match any of my rules, return a default response from CYCLE in a cyclical manner 
    return cycle()

# create a sentence from a list
def stringify(wordlist):
    'Create a string from wordlist, but with spaces between words.'
    return ' '.join(wordlist)

# CYCLE FEATURE AND MEMORY FEATURE 
def cycle():
    'Returns one from a list of default responses.'
    global memory
    global memory_added
    global CYCLE
    # if memory was added, add a new default response ('when do you want to') to CYCLE (list of default responses)
    if memory_added:
        CYCLE.append("When do you want to ")
        memory_added = False
    global cycle_count
    # a counter for CYCLE FEATURE   
    cycle_count += 1
    # if new default response ('when do you want to') was added to CYCLE, and cycle feature picks 
    # the new default response, append a random memory to it
    # otherwise, just return the chosen default response as it is 
    if cycle_count % len(CYCLE) == 10:
        return CYCLE[cycle_count % len(CYCLE)] + choice(memory) + "?"
    else: 
        return CYCLE[cycle_count % len(CYCLE)]


punctuation_pattern = compile(r"\,|\.|\?|\!|\;|\:")    

def remove_punctuation(text):
    'Returns a string without any punctuation.'
    return sub(punctuation_pattern,'', text)

CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}

def you_me(w):
    'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result

def you_me_map(wordlist):
    'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]