class quistion :
    def __init__(self , promet , answer ,) :
        self.promet = promet
        self.answer = answer


quistion_promets = [
    ' what color are apples \n (a) red \n  (b) green  \n (c) purple  \n (d) orange  ',
    ' what color are bananas \n (a) red \n  (b) green  \n (c) yelow  \n (d) orange ',
 ' what color are strwbaries \n (a) red \n  (b) green  \n (c) purple  \n (d) orange  '
]



quistions =[
   quistion (quistion_promets[0], 'a'),
   quistion (quistion_promets[1], 'c'),
   quistion (quistion_promets[2], 'a')
]

def run_test(quistions) :
    score =0
    for quistion in quistions:
        answer = input ( quistion.promets)
        if answer == quistion.answer :
            score +=1

        print ('you got '+str (score))


run_test(quistions)