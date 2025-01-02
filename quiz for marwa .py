# difin what a quistion is using class
# make choices
# tell the computer about the right answers
# make fuction
# make loob for answer
name = input (' type your name :\n')
print (f'hello {name} are you ready to take a simple test ? \n let`s start ')

class quistion:
    def __init__(self,promet,answer,):
        self.promet = promet
        self.answer = answer

quistion_promets = [
     '1....what tense is this sentens ? (i work with my frind whenever he is home )\n A past simple \n B present simple \n C present continues \n D past continues \n',
     '2....what tense is this sentens ? (what are you boys doing ? )\n A past simple \n B present simple \n C present continues \n D past continues \n',
     '3....what tense is this sentens ? (i smiled at my dad)\n A past simple \n B present simple \n C present continues \n D past continues \n ',
     '4....what tense is this sentens ? (my dad`s frind turned and burst into laghter when we were looking at him )\n A past simple \n B present simple \n C present continues \n D past continues \n',
     '5....what tense is this sentens ? (you mean this is illegal !)\n A past simple \n B present simple \n C present continues \n D past continues \n ',
     '6....what tense is this sentens ? (mike and i ran around our neighborhood knocking in doors )\n A past simple \n B present simple \n C present continues \n D past continues \n ',
     '7....what tense is this sentens ? (i don`t want to hear again that it is a businnes secert)\n A past simple \n B present simple \n C present continues \n D past continues \n ',
     '8....what tense is this sentens ? (Dad, can you till me how to get rich ? )\n A past simple \n B present simple \n C present continues \n D past continues \n ',
     '9....what tense is this sentens ? (today jimmy`s mom drove up i their new Cadillac )\n A past simple \n B present simple \n C present continues \n D past continues \n '
]

quistions=[
    quistion (quistion_promets[0] ,'B'),
    quistion (quistion_promets[1] ,'C'),
    quistion (quistion_promets[2] ,'A'),
    quistion (quistion_promets[3] ,'A'),
    quistion (quistion_promets[4] ,'B'),
    quistion (quistion_promets[5] ,'D'),
    quistion (quistion_promets[6] ,'B'),
    quistion (quistion_promets[7] ,'B'),
    quistion (quistion_promets[8] ,'A'),
]    


def run_test(choises):
    score =0
    for quistion in quistions:
        choice = input (quistion.promet)
        if choice == quistion.answer:
            score +=1
            print(f'great job you got {score}')
        else:
            print (f'wrong answer your score still {score}')    


run_test(quistion) 

close = input (' the quiz is done type yes if you want to close the program\n')