import re

#we get the simple text from your notesapp or from your manual typying, either way works
def food_input():
    #food_item = input("Just copy paste your note app texts! \n")
    #food_item="chicken breast - 300 cheese - 125 sub- 1200 + 500 cheesy bites - 600 cookie - 250 muffin - 460 lipton tea - 100 icecream - 350"
    items=""
    print("Paste your multiline input. Press Ctrl+D (Unix/Linux) or Ctrl+Z (Windows) to finish:")

    try:
        while True:
            food_items = input()
            items += food_items + '\n'
    except EOFError:
        pass  # End-of-File detected
    
    # now that i've learned that python doesnt handle even the input strings without proper intendation , i need to fix them when i get them from the clipboard
    
    """
    def text_intent(food_item):
        # Split the text into lines
        lines = food_item.split('\n')

    # Remove leading and trailing whitespaces from each line
        trimmed_lines = [line.strip() for line in lines]

    # Print the reformatted text
        print("\nReformatted Text:")
        for line in trimmed_lines:
            print(line)
        
        return line
        """
    print(items)
    return items

# created a seperate function for splitiing the text, such that only integers are being calcualted and the floats, doubles will be rounded off nearest upper number.
def calorie_splitter():
    text_input= food_input()
    
    food_list = re.split(r'[,\s;\\-:_=*]+',text_input) 
    #print(food_list)
    calories = [int(food) for food in food_list if food.isdigit()]
   
    total_calories=0
 
    for item in calories:
        print(item)
        total_calories+=item
        

    return total_calories

user_choice = int(input("1. Calculate Total calories from the text!\n2.Exit\n"))

if(user_choice==1):
   
    
    print("The total calories for the day is: ",calorie_splitter())
    
else:
    exit

