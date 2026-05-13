"""
5.2PP Collection of Strings
"""


def add_word(word_list: list[str], word: str):
    if word == "":
        print("Empty words cannot be added.")
        return 
    if word in word_list:
        print("word already exists in the list.")
    else:
        word_list.append(word)
        print(f'"{word}" added successfully.')


def display_entries(word_list: list[str]):
    if len(word_list)==0:
        print("No entries.")
        return 
    
    for i, word in enumerate(word_list):
        if i < len(word_list)-1:
            print (word ,end = ",")
        else :
            print(word)
         
            
def average_len(word_list: list[str]) -> float:
    if len(word_list)== 0 :
        return 0.0
    
    total=0
    for word in word_list:
        total+= len(word)
        
    return total / len(word_list)
        

def main():
    words:list[str]=[]
    choice: str=""

    print("Words!")
    
    while choice != "4":
        print("\n1. Add a word")
        print("2. Display entries")
        print("3. Display average word length")
        print("4. Quit")
        
        choice=input("Action:")
        
        match choice :
            case"1":
                new_word = input ("Enter a word:")
                add_word(words,new_word)
                
            case "2":
                display_entries(words)

            case "3":
                avg = average_len(words)
                print(f"Average word length: {avg:.2f}")

            case "4":
                print("Goodbye!")

            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
