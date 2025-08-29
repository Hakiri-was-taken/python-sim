
import re

#TODO: Clean up Code
# test function calls in various orders: DONE?
# zak wants me to check into how i am validating user input everywhere its being used.
# debug


class Tournament():
    
    # TODO: back to menu option for option 6:test
    #initalization
    def __init__(self):
    # Set up our data variables we need for the WHOLE tournament
        # not quite sure about this.
        self.characters = []
        
    # Print application name and instructions
        print("Initializing the Tournament")
        print("Options:\n",
                "1: User Signup\n",
                "2: Run Tournament\n",
                "3: Points Tally\n",
                "4: Display Results\n",
                "5: Display StatCards\n",
                "6: Reset Tournament\n",
                "9: Options\n",
                "0: Exit")
            
            # take the input first, then handle the info
        
        bool=True
        while(bool):
           # Request Command from user
            try:
                user_input = input("Choose an option: ")
            except:
                print("something went wrong!")
            # checks user input
            if user_input.isdigit() and int(user_input) == (0) or user_input == "Exit":
                print("are you sure you want to exit the tournament?")
                try:
                    user_input = input("Y/N: ")
                except:
                    print("something went wrong!")
                # are you sure you want to exit?
                if user_input == "Y" or user_input == "y":
                       print("Shutting down, Goodbye...")
                       bool=False
                elif user_input == "N" or user_input == "n":
                    print("Resuming the Tournament")
                else:
                    print("Please choose Y/N")
                    user_input = input("Y/N: ")
            elif user_input == "":
                print("Please choose an option")

            elif user_input.isdigit() and int(user_input) == (1) or user_input == ("User Signup"):
                try:
                    self.user_call_signup()
                except:
                    print("something went wrong!")
            
            elif user_input.isdigit() and int(user_input) == (2) or user_input == ("Run Tournament"):
                if len(self.characters) >= 2:
                    try:
                        self.run_tournament()
                    except:
                        print("something went wrong!")
                else:
                    print("there is not enough contestants to compete!")
            elif user_input.isdigit() and int(user_input) == (3) or user_input == ("Points Tally"):
                if len(self.characters) >= 2:
                    try:
                        self.points_tally()
                        self.characters = self.sort_by_points()
                    except:
                        print("something went wrong!")
                else:
                    print("there are not enough or no contestants to tally...")
            elif user_input.isdigit() and int(user_input) == (4) or user_input == ("Display Results"):
                if len(self.characters) >= 2:
                    try:
                        self.display_results_with_ties()
                    except:
                        print("something went wrong!")
                else:
                    print("there are not enough or no contestants to display...")
            
            elif user_input.isdigit() and int(user_input) == (5) or user_input == ("Display StatCards"):
                if len(self.characters) >= 0:
                    try:
                        self.display_statcards()
                    except:
                        print("something went wrong!")
                else:
                    print("there are no contestants to display...")
            elif user_input.isdigit() and int(user_input) == (6) or user_input == ("Reset Tournament"):
                print("Tournament Reset Options\n",
                    "1: Complete reset\n",
                    "2: Results reset\n",
                    "3: Back to options")
                    
                user_input = input("Choose an option: ")
                if user_input.isdigit() and int(user_input) == (1) or user_input == ("Complete reset"):
                    print("are you sure you want to reset the Tournament?")
                    user_input = input("Y/N: ")
                    if user_input == "Y" or user_input == "y":
                        try:
                            self.reset_tournament()
                            print("Tournament Sucsessfully Reset...")
                        except:
                            print("Something went wrong!")
                    elif user_input == "N" or user_input == "n":
                        print("Reset Aborted")
                    elif user_input == "":
                        print("Please choose an option")
                        user_input = input("Y/N: ")
                    else:
                        print("Please choose Y/N")
                        user_input = input("Y/N: ")
                elif user_input.isdigit() and int(user_input) == (2) or user_input == ("Results reset"):
                    print("are you sure you want to reset the Tournament Results?")
                    user_input = input("Y/N: ")
                    if user_input == "Y" or user_input == "y":
                        try:
                            self.reset_results()
                            print("Tournament Results Sucsessfully Reset...")
                        except:
                            print("Something went wrong!")
                    elif user_input == "N" or user_input == "n":
                        print("Reset Aborted")
                    elif user_input == "":
                        print("Please choose an option")
                        user_input = input("Y/N: ")
                    else:
                        print("Please choose Y/N")
                        user_input = input("Y/N: ")
                else:
                    print("Options:\n",
                "1: User Signup\n",
                "2: Run Tournament\n",
                "3: Points Tally\n",
                "4: Display Results\n",
                "5: Display StatCards\n",
                "6: Reset Tournament\n",
                "9: Options\n",
                "0: Exit")

    #  return to options and request a new command.
            elif user_input.isdigit() and int(user_input) == (9) or user_input == ("Options"):
                print("Options:\n",
                "1: User Signup\n",
                "2: Run Tournament\n",
                "3: Points Tally\n",
                "4: Display Results\n",
                "5: Display StatCards\n",
                "6: Reset tournament\n",
                "9: Options\n",
                "0: Exit")
            # reject incorrect commands
            else: 
                print("that is not an option...")
    
    # TODO: test to make sure it works as intended
    # calls user_signup for however many times the user wants.
    def user_call_signup(self):
        bool = True
        index = 0
        while bool:
            try:
                call_signup = input("How many combatants would you like to battle?: ")
            except:
                print("something went wrong!")
            if call_signup.isdigit():
                print(call_signup+" Contenders shall Duel in the Tournament!")
                call_signup = int(call_signup)
                while index < call_signup:
                    self.user_signup()
                    index += 1
                bool = False
            elif call_signup == "":
                print("You must enter a number!")
            else:
                print("Please Enter a valid number...")
    
    # allows user input for characters with power, has functionality for preventing duplicate names and power.
    def user_signup(self):
        # the while loop will restart if there is a duplicate entry user
        is_duplicate_user = 0
        while is_duplicate_user == 0:
            entry_user = {"name": "",
                            "power": ""}
            print("Welcome to the fight pits!!! Please enter your name:")
            while entry_user["name"] == "":
                entry_user["name"] = input("Name: ")

            print("now enter your level:")
            # input is character
            while entry_user["power"] == "":
                level = input("Level: ")
                if contains_only_numbers(level):
                    level = (int(level))
                    entry_user["power"] = level
                else:
                    print("Please Enter a valid number...")
            # checking if the current character is the same as a character in the list.
            already_exists = False
            for character in self.characters:
                if entry_user["name"] == character["name"] and entry_user["power"] == character["power"]:
                        print("That was a duplicate entry... That contender already exists...")
                        print("Please use a different name!")
                        already_exists = True
            if already_exists == False:
                # character casted to int
                # character default values
                entry_user["wins"] = 0
                entry_user["losses"] = 0
                entry_user["draws"] = 0
                entry_user["points"] = 0
                print("Thank you for joining the pits! May the odds forever be in your favor.")
                print(entry_user["name"])
                print(entry_user["power"])
                self.characters.append(entry_user)
                # exits while loop when the user successfully enter a character.
                is_duplicate_user = 1
    
    # counts characters points.
    def points_tally(self):
        points_value = {"wins":1,
                        "losses":0,
                        "draws":.5}
        
        for character in (self.characters):
            character["points"] = 0
            
            if character["wins"] > (0):
                print("calculating wins points")
                
                character["points"] += points_value["wins"] * character["wins"] 

                print(f"{character["name"]} = {character["points"]}")

            if character["draws"] > (0):
                print("calculating draws points")
                character["points"] += points_value["draws"] * character["draws"] 
                print(f"{character["name"]} = {character["points"]}")

    # indexed # sorts character position based on points with an index.
    def points_tally_with_indexed_for_loop(self):
        wins = 1
        losses = 0
        draws = .5

        for index1 in range(len(self.characters)):
            self.characters[index1]["points"] = 0
            if  self.characters[index1]["wins"] > (0):
                print("calculating wins points")
                self.characters[index1]["points"] += wins *  self.characters[index1]["wins"]
                print(f"{ self.characters[index1]["name"]} = { self.characters[index1]["points"]}")
            
            if  self.characters[index1]["draws"] > (0):
                print("calculating draws points")
                self.characters[index1]["points"] += draws *  self.characters[index1]["draws"] 
                print(f"{ self.characters[index1]["name"]} = {draws * self. characters[index1]["draws"] }")
            print("calculating total points")
            print(f"{ self.characters[index1]["name"]} = { self.characters[index1]["points"]}")

    # sorts character position based on points.
    def sort_by_points(self):
        items =  self.characters.copy()
        total = len(items)

        for index1 in range(total):
            lowest_index = index1
            
            for index2 in range(index1 + 1, total):
                if "points" not in items[index2] or "points" not in items[lowest_index]:
                    continue

                if items[index2]["points"] > items[lowest_index]["points"]:
                    lowest_index = index2

            if lowest_index != index1:
                items[index1], items[lowest_index] = items[lowest_index], items[index1]
        
        return items

    # compares power lvl and assigns points to winners.
    def run_tournament(self):
        index1 = 0
        index2 = 0
        while(index1 < len( self.characters)):
            index2 = index1
            while(index2 < len( self.characters)):
                if( self.characters[index1] !=  self.characters[index2]):
                    print(f"{ self.characters[index1]["name"]} VS { self.characters[index2]["name"]}")
                    
                    if( self.characters[index1]["power"] ==  self.characters[index2]["power"]):
                        print("It was A draw!\n")
                        self.characters[index1]["draws"] += 1
                        self.characters[index2]["draws"] += 1
                    
                    elif( self.characters[index1]["power"] <  self.characters[index2]["power"]):
                        print(f"{ self.characters [index2]["name"]} Is the winner!\n")
                        self.characters[index2]["wins"] += 1
                        self.characters[index1]["losses"] += 1
                    
                    elif(self.characters[index1]["power"] > self.characters[index2]["power"]):
                        print(f"{self.characters[index1]["name"]} Is the winner!\n")
                        self.characters[index1]["wins"] += 1
                        self.characters[index2]["losses"] += 1
                index2 +=1
            index1 += 1

    # redundant...
    # displays the postion of characters.
    def display_results(self):
        index = 1
        
        for character in (self.characters):
            
            if index == 1:
                print(f"first place goes to {character["name"]}!")
            
            elif index == 2:
                print(f"second place goes to {character["name"]}!")
            
            elif index == 3:
                print(f"third place goes to {character["name"]}!")
            
            elif index > 3:
                print(f"{index}th place {character["name"]}")
            index +=1 
    
    # displays charater position based on points and handles if there are draws
    def display_results_with_ties(self):
        # TODO: add in "drumroll".mp3 in python.

        
        index1 = 0
        # checks to make sure we haven't checked everything in index1
        while index1 < len(self.characters):
            index2 = index1+1
            ties = []
            current_place = index1+1
            '''{"name": "Grim Reaper",
               "power": 9001,
               "wins": 0,
               "losses": 0,
               "draws": 0,
               "points": 0}, '''
            # 1: = index1
            # 2: = index2
            # 3:
            # 4:
            # checks for a tie.
            if index2 < len(self.characters):
            # going to bump index1 and index2 inside this loop.
                #if there is a tie check the while loop condition.
                while self.characters[index1]["points"] == self.characters[index2]["points"]:
                    if self.characters[index1] not in ties:
                        ties.append(self.characters[index1])
                    if self.characters[index2] not in ties:
                        ties.append(self.characters[index2])  
                    if index2 < len(self.characters)-1: 
                        index1+=1
                        index2+=1   
            
            # ties do this
            if len(ties) != 0:
                # need to print "name" of every character at the current index.
                if current_place == 1:
                    print(f"There was a tie for {current_place}st place!!!")
                elif current_place == 2:
                    print(f"There was a tie for {current_place}nd place!!!")
                elif current_place == 3:
                    print(f"There was a tie for {current_place}rd place!!!")
                elif current_place > 3:
                    print(f"There was a tie for {current_place}th place!!!")
                # prints the names in the tie.
                for character in (ties):
                    print(f"\t{character["name"]}")
                index1+=1
            
            # there are no ties.
            else:
                # print the "name" at the current index.
                if current_place == 1:
                    print(f"{current_place}st place goes to!")
                    print(f"\t{self.characters[index1]["name"]}")
            
                elif current_place == 2:
                    print(f"{current_place}nd place goes to!")
                    print(f"\t{self.characters[index1]["name"]}")
            
                elif current_place == 3:
                    print(f"{current_place}rd place goes to!")
                    print(f"\t{self.characters[index1]["name"]}")
            
                elif current_place > 3:
                    print(f"{current_place}th place goes to!")
                    print(f"\t{self.characters[index1]["name"]}")
                index1 +=1 

    # redundant...
    # function... list all characters and print out their statcards.
    def display_statcards(self):
        if (len(self.characters) <= 0):
            print("there are no contenders!")
        else:
            for character in self.characters:
                print(character)

    # resets all user entries.
    def reset_tournament(self):
        self.characters = []

    # resets tournament reults but leaves the current entries.
    def reset_results(self):
        for character in self.characters:
            character["wins"] = 0
            character["losses"] = 0
            character["draws"] = 0
            character["points"] = 0
    
# helper functions
def contains_only_numbers(input_string):
    pattern = r"^\d+$"  # ^ matches start, \d matches digits, + matches 1 or more, $ matches end
    if re.match(pattern, input_string):
        return True
    return False

# IF we run THIS specific PY file then do this.
if __name__ == "__main__":
    # Initialize the tournament class
    tournament = Tournament()


