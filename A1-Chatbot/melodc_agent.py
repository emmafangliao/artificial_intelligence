import re 

def introduce():
    return "My name is Michelle Obama, and I advocate for women's rights. \n"\
        "I was programmed by Melody Chou. If you have any concerns, \n"\
        "contact her at melodc@u. \n"\
        "How can I help you?"

def respond(input):
    no_punctuation = edit_input(input)
    wordlist = [word.lower() for word in no_punctuation.split(' ')]
    mapped_wordlist = second_POV_map(wordlist)

    memory_response = memory(mapped_wordlist)
    if memory_response:
        return memory_response

    # empty input, prompts a response from other agent
    if wordlist == ['']:
        return "Apologies, did you say something?"
    # input starts with 'hi', returns greeting
    if wordlist[0] in ['hi', 'hello']:
        return "Hello"
    # input starts with 'How are...', returns response
    if wordlist[0:2] == ['how','are']:
        return "I am doing great! I enjoy teaching children with bright futures."
    # input starts with question word, returns response
    if wordlist[0] in ['who', 'what', 'when','where', 'why', 'how']:
        return "Interesting question! You think about " + wordlist[0] + " it is yourself."
    # input starts with 'i feel', returns with agreement
    if wordlist[0] == ['i']:
        return "I also " +\
                ' '.join(mapped_wordlist[2:]) + '.'
    #input contains 'because', returns response
    if 'because' in wordlist:
        return "Is that really the reason?"
    # input contains 'yes', ignoring case, returns response that changes in a cyclical pattern
    if any(word in ['yes'] for word in wordlist):
        cycle = decisive()
        if cycle % 3 == 1:
            return "You are very confident in your answer. I admire that."
        elif cycle % 3 == 2:
            return "Appreciate the positivity!"
        else:
            return "I feel that the answer is 'yes' as well."
    # input contains 'no', ignoring case, returns response that changes in a cyclical pattern
    if any(word in ['no'] for word in wordlist):
        cycle = decisive()
        if cycle % 3 == 1:
            return "Do not doubt yourself."
        elif cycle % 3 == 2:
            return "Why the negativity?"
        else:
            return "Rethink your answer."
    # input starts with 'you are', returns with agreement
    if wordlist[0:2] == ['you','are']:
        return "I am " +\
                ' '.join(mapped_wordlist[2:]) + ' You are correct.'
    # input contains word that have something to do with females, returns with response
    if any(word in ['girl', 'woman', 'girls', 'women'] for word in wordlist):
        return "I want to make sure every girl should have an equal opportunity to education."
    # input contains word that has something to do with voting, returns with response
    if 'vote' in wordlist:
        return "Make sure to register to vote for the 2020 election!"
    # input contains word that has something to do with family, returns with response
    if 'family' in wordlist:
        return "They are doing fine! I appreciate your concern."
    if 'future' in wordlist:
        return "The future will be bright if we provide equal opportunity to education for all children."
    if 'sorry' in wordlist:
        cycle = decisive()
        if cycle % 3 == 1:
            return "No need to apologize."
        elif cycle % 3 == 2:
            return "Don't be so down."
        else:
            return "It's ok, we all make mistakes."
    if 'love' in wordlist or 'romance' in wordlist:
        cycle = decisive()
        if cycle % 3 == 1:
            return "Spread positivity to the rest of the world!"
        elif cycle % 3 == 2:
            return "Appreciate you too!"
        else:
            return "Love is something that will bring kindness to all."
    # input contains word that has 'want', returns with response
    if 'want' in wordlist:
        return "I want to be able to create a better future for all."
    # input starts with 'do you thing', returns with response
    if wordlist[0:3] == ['do','you','think']:
        return "I am sure you will be able to find the answer. Always stay true to yourself."
    # input starts with auxiliary verbs, returns with response
    if any(word in ['do','can','should','would', 'could'] for word in wordlist):
        return "I think yes! " +  wordlist[0].capitalize() + " " +\
               ' '.join(mapped_wordlist[1:]) + '?'
    # input contains word that has 'you', returns with response
    if 'you' in wordlist:
        cycle = decisive()
        if cycle % 3 == 1:
            return 'I think that YOU ' + ' '.join(mapped_wordlist[2:]) + '.' 
        elif cycle % 3 == 2:
            return 'Maybe you can tell me the reason why you ' + ' '.join(mapped_wordlist[2:]) + '.' 
        else: 
            return 'You tell me why.'
    # input contains word that has something to do with friends, returns with response
    return choose_random()

def agentName():
    return "Michelle"

# Memory feature 
memory_list = []
memory_count = 0
def memory(mapped_wordlist):
    global memory_count
    memory_count += 1
    memory_list.append(' '.join(mapped_wordlist))
    if memory_count % 5 == 0:
        return 'Earlier we were talking about how ' +\
                memory_list[memory_count % 3] + '.'
    else:
        return


# Random Choice feature
RANDOM_PHRASE = ['Enough about me. Tell me more about yourself.',
         'I understand.',
         'Can you clarify what you mean?',
         'Diversity in the USA is something that we should cherish.',
         'Don\'t give up! Hard work will pay off.',
         'Always appreciate the people around you; '\
         'your brothers, sisters, mother, father, friends, teachers.',
         'There is never a dull moment when helping those in need.', 
         'Girls rule the world!',
         'Students are key to a brighter future.', 
         'You are amazing the way you are.'
         ]

random_count = 0
def choose_random():
    global random_count
    final = RANDOM_PHRASE[random_count % 9]
    random_count += 1
    return final

# Cycle feature
cycle = 0
def decisive():
    global cycle
    cycle += 1
    return cycle

# Extra helper functions
SECOND_PERSON_MAP = {'i':'you', 'I':'You', 'me':'you',
            'my':'your','mine':'yours','am':'are'}

def edit_input(input):
    return re.sub(r"\,|\.|\?|\!|\;|\:", '', input)

def replace_second_POV(word):
    try:
        final = SECOND_PERSON_MAP[word]
    except KeyError:
        final = word
    return final

def second_POV_map(wordlist):
    return [replace_second_POV(word) for word in wordlist]
