import random

strategy_name = 'Random With Strategy'

def move(my_history, their_history):
    

    if len(their_history)==0:
        my_move = 'p'
    else:
        prediction = predict_they_will_repeat(their_history.lower())
        my_move = beat_prediction(prediction)
    return my_move
    
def predict_they_will_repeat(their_history):
  

    return their_history[-1]
        
def beat_prediction(prediction):


    if prediction =='r':
        winning_move = pick = random.choice(["p", "p", "p", "p", "p", "p", "s", "s", "s", "r"])        
        return pick
    elif prediction == 'p':
        winning_move = pick = random.choice(["s", "s", "s", "s", "s", "s", "r", "r", "r", "p"])
        return pick
    elif prediction == 's':
        winning_move = pick = random.choice(["r", "r", "r", "r", "r", "r", "p", "p", "p", "s"])
        return pick
    
    else:
        winning_move = '' 
        print ('Error in beat_prediction(): prediction was not r, p, or s.')
    return winning_move
