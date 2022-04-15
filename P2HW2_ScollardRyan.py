#
# Score Average
# 14 APR 2022
# CTI-110 P2HW1 - Score Average
# Ryan Scollard
#


#Empty list in which scores will be stored
scores = []

#Asks user input for scores and stores float in to an score variable.
score_one = float(input('Enter score #1: '))

#Appends score variable to list
scores.append(score_one)

#Asks user input for scores and stores float in to an score variable.
score_two = float(input('Enter score #2: '))

#Appends score variable to list
scores.append(score_two)

#Asks user input for scores and stores float in to an score variable.
score_three = float(input('Enter score #3: '))

#Appends score variable to list
scores.append(score_three)

#Asks user input for scores and stores float in to an score variable.
score_four = float(input('Enter score #4: '))

#Appends score variable to list
scores.append(score_four)

#Asks user input for scores and stores float in to an score variable.
score_five = float(input('Enter score #5: '))

#Appends score variable to list
scores.append(score_five)

#Asks user input for scores and stores float in to an score variable.
score_six = float(input('Enter score #6: '))

#Appends score variable to list
scores.append(score_six)

#Asks user input for scores and stores float in to an score variable.
score_seven = float(input('Enter score #7: '))

#Appends score variable to list
scores.append(score_seven)




#Outputs results of program calculations with seperation 
print('\n---------Results----------')

#Prints lowest score
print(f'Lowest Score  : {min(scores)}')

#Removes lowest score from list
scores.remove(min(scores))

#Prints list containting scores
print(f'Modified List : {scores}')

#Calcualtes average. Total scores(sum) divided by number of scores(len).
print(f'Scores Average: {sum(scores)/len(scores)}')

#Prints dashes for aesthetics
print('----------------------------')

