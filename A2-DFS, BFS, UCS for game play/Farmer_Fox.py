'''Farmer_Fox.py
by Emma Liao
UWNetID: liaofang
Student number: 1669805

Assignment 2, in CSE 415, Autumn 2019.
 
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''

#<METADATA>
SOLUZION_VERSION = "2.0"
PROBLEM_NAME = 'Farmer and Fox'
PROBLEM_VERSION = '2.0'

PROBLEM_AUTHORS = ['Emma Liao']
PROBLEM_DESC=\
''' Rules: 
    Farmer can only carry one thing with him on the boat
    Fox & Chicken, Chicken & Grain can't be on the same side of bank alone'''
#</METADATA>

#<COMMON_CODE>
LEFT=0
RIGHT=1
FOX=0
CHICKEN=1
GRAIN=2
FARMER=3
#[fox, chicken, grain, farmer]

class State():
    def __init__(self, d=None):
        if d==None:
            d={'item': [[0,0],[0,0],[0,0],[0,0]],
                'boat': LEFT}
        self.d=d

    def __eq__(self,s2):
        for prop in ['item', 'boat']:
          if self.d[prop] != s2.d[prop]: return False
        return True

    def __str__(self):
        # Produces a textual description of a state.
        p = self.d['item']
        txt = "\n Number of Foxes on left:"+str(p[FOX][LEFT])+"\n"
        txt += " Number of Chicken on left:"+str(p[CHICKEN][LEFT])+"\n"
        txt += " Number of Grain on left:"+str(p[GRAIN][LEFT])+"\n"
        txt += " Number of Farmer on left:"+str(p[FARMER][LEFT])+"\n"
        txt += "\n   Number of Foxes on right:"+str(p[FOX][RIGHT])+"\n"
        txt += "    Number of Chicken on right:"+str(p[CHICKEN][RIGHT])+"\n"
        txt += "    Number of Grain on right:"+str(p[GRAIN][RIGHT])+"\n"
        txt += "    Number of Farmer on right:"+str(p[FARMER][RIGHT])+"\n"
        
        side='left'
        if self.d['boat']==1: side='right'
        txt += " boat is on the "+side+".\n"
        return txt

    def __hash__(self):
        return (self.__str__()).__hash__()

    def copy(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        news = State({})
        news.d['item']=[self.d['item'][allItems][:] for allItems in [FOX, CHICKEN, GRAIN, FARMER]]
        news.d['boat'] = self.d['boat']
        return news 

    


    def can_move(self, fox, chicken, grain, farmer):
        
        side = self.d['boat'] # Where the boat is.
        p = self.d['item']
        if farmer<1: return False # Need a farmer to steer boat.
        fox_available = p[FOX][side]
        if fox_available < fox: return False # Can't take more foxes than available
        chicken_available = p[CHICKEN][side]
        if chicken_available < chicken: return False # Can't take more chickens than available
        grain_available = p[GRAIN][side]
        if grain_available < grain: return False
        farmer_available = p[FARMER][side]
        if farmer_available < farmer: return False

        fox_remaining = fox_available - fox
        chicken_remaining = chicken_available - chicken
        grain_remaining = grain_available - grain
        farmer_remaining = farmer_available - farmer

        # Fox and chicken can't be alone, chicken and grain can't be alone :
        if fox_remaining > 0 and chicken_remaining >0 and farmer_remaining==0 and grain_remaining==0: return False
        if chicken_remaining > 0 and grain_remaining >0 and farmer_remaining==0 and fox_remaining==0: return False

        return True



    def move(self,fox,chicken,grain,farmer):
        '''Assuming it's legal to make the move, this computes
         the new state resulting from moving the boat carrying
         m missionaries and c cannibals.'''
        news = self.copy()      # start with a deep copy.
        side = self.d['boat']         # where is the boat?
        p = news.d['item']          # get the array of arrays of people.
        p[FOX][side] = p[FOX][side]-fox     # Remove people from the current side.
        p[CHICKEN][side] = p[CHICKEN][side]-chicken
        p[GRAIN][side] = p[GRAIN][side]-grain
        p[FARMER][side] = p[FARMER][side]-farmer 

        p[FOX][1-side] = p[FOX][1-side]+fox # Add them at the other side.
        p[CHICKEN][1-side] = p[CHICKEN][1-side]+chicken
        p[GRAIN][1-side] = p[GRAIN][1-side]+grain
        p[FARMER][1-side] = p[FARMER][1-side]+farmer

        news.d['boat'] = 1-side       # Move the boat itself.
        return news

def goal_test(s):
  '''If all Ms and Cs are on the right, then s is a goal state.'''
  p = s.d['item']
  return (p[FARMER][RIGHT]==1 and p[CHICKEN][RIGHT]==1 and p[GRAIN][RIGHT]==1 and p[FOX][RIGHT]==1 )


def goal_message(s):
    return 'Congratulations!'

class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)

#<INITIAL_STATE>
CREATE_INITIAL_STATE = lambda : State(d={'item':[[1,0],[1,0],[1,0],[1,0]],
                                            'boat': LEFT})
#</INITIAL_STATE>

#<OPERATORS>
#[FOX,CHICKEN,GRAIN,FARMER]
combinations = [(1,0,0,1),(0,1,0,1),(0,0,1,1),(0,0,0,1)]

OPERATORS = [Operator(
  "Farmer crosses the river with "+str(fox)+" foxes, "+str(chicken)+" chickens, " +str(grain) +" grains and "+str(farmer)+" farmers",
  lambda s, f1=fox, c1=chicken, g1=grain, f2=farmer: s.can_move(f1,c1,g1,f2),
  lambda s, f1=fox, c1=chicken, g1=grain, f2=farmer: s.move(f1,c1,g1,f2) ) 
  for (fox,chicken,grain,farmer) in combinations]
#</OPERATORS>



#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>






