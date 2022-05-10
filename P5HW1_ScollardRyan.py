#
# Score List
# 09 MAY 2022
# CTI-110 P5W1 - Score List
# Ryan Scollard
#

#Empty list to hold scores
scores = []

#Function to take user input, evaluate if it is between 0 and 100. Then add it to list.
def new_scores():
    number_of_scores = int(input('\nHow many scores do you want to enter? '))
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
    return scores
               

#Function to give results
def score_output(scores):
    print('\n---------Results----------')
    print(f'Lowest Score  : {min(scores)}')
    scores.remove(min(scores))
    print(f'Modified List : {scores}')
    print(f'Scores Average: {sum(scores)/len(scores):.2f}')
    grade_score = int(sum(scores)/len(scores))

    if grade_score >= 90:
        print(f'Grade         : A')
    elif grade_score >= 80:
        print(f'Grade         : B')
    elif grade_score >= 70:
        print(f'Grade         : C')
    elif grade_score >= 60:
        print(f'Grade         : D')
    else:
        print(f'Grade         : F')
    print('----------------------------\n')

#Creates menu
while True:  
    print("\n-----------MENU-----------")  
    print("1) Create Score List")  
    print("2) Display Results")  
    print("3) Exit")
    print("--------------------------")
    users_choice = int(input("\nPlease choose one of the menu options: "))  
  
# based on the users choice the relevant method is called
    if users_choice == 1:
        new_scores(scores)
    elif users_choice == 2:
        if not scores:
            users_choice = int(input("\nNo scores are currently stored. \n \nPlease choose one of the menu options: "))        
        else:
            score_output(scores) 
  # exit the while loop
    elif users_choice == 3:  
        break   
    else:  
        print( "Please enter a valid Input from the list")  
