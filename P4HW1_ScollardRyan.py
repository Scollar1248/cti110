#
# Score List
# 09 MAY 2022
# CTI-110 P4HW1 - Score List
# Ryan Scollard
#

#Empty list to hold scores
scores = []

#Function to take user input, evaluate if it is between 0 and 100. Then add it to list.
def new_scores():
    number_of_scores = int(input('How many scores do you want to enter? '))
    print()
    for number in range(number_of_scores):
        number += 1
        new_number = input(f'Enter score #{number}: ')    
        if int(new_number) < 0 or int(new_number) > 100:
            print('INVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            scores.append(float(input(f'Enter score #{number} again: ')))      
        else:
            scores.append(float(new_number))
            print(scores)
            
    
       

new_scores()



# # #Outputs results of program calculations with seperation 
print('\n---------Results----------')

# # # #Prints lowest score
print(f'Lowest Score  : {min(scores)}')

# # # #Removes lowest score from list
scores.remove(min(scores))

# # # #Prints list containting scores
print(f'Modified List : {scores}')

# # # #Calcualtes average. Total scores(sum) divided by number of scores(len).
print(f'Scores Average: {sum(scores)/len(scores):.2f}')


#Calculates avarage and give it a letter represenation.
grade_score = int(sum(scores)/len(scores))

A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 59 

if grade_score >= A_score:
    print(f'Grade         : A')
elif grade_score >= B_score:
    print(f'Grade         : B')
elif grade_score >= C_score:
    print(f'Grade         : C')
elif grade_score >= D_score:
    print(f'Grade         : A')
else:
    print(f'Grade         : D')



# # # #Prints dashes for aesthetics
print('----------------------------')

