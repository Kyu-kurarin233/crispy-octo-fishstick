crispy-octo-fishstick

# Programming Principles

Structured programming is an important foundation of software development. It helps programmers create code that is clear, organised, reusable, and easier to maintain.
## Sequence
instructions should be executed in a specific order.
```python
first_place: str = input("Enter the name of the rider in first place: ")
time_1: float = float(input("Enter the total time: "))
margin = time_2 - time_1
print(f"They beat {second_place} by just {margin:.2f} hours.")
```
This sequence is important because the program cannot calculate the margin before the times are entered. The correct order allows the program to function logically and accurately.
```python
margin = time_2 - time_1
```
## Selection
Allows a program to make decisions based on conditions. I used selection in both the Maths Tutorial and Word List programs through if, else, and match-case statements.
```python
if attempt == num1 - num2:
    print("Correct!")
else:
    print(f"Incorrect.The correct answer is {num1-num2}")
```
This allows the program to respond differently depending on the input.
I also used match-case in the Word List to create a menu system:
```python
match choice:
    case "1":
        add_word(words,new_word)
    case "2":
        display_entries(words)
```
This improves readability compared to using many if-elif statements.
Selection allows a program to make decisions based on conditions. I used if、elseand match-casein the Maths Tutorial and Word List programs.
For example:
```python
if attempt == num1 - num2:
```
Used to judge the answer is true or not,and :
```python
match choice:
```
This is used in menu selection systems to make the code clearer.
## Repetition (Loops)
Also called iteration, allows code to run multiple times efficiently. I used both while and for loops in my assignments.
In the Word List , a while loop keeps the menu running until the user decides to quit:
```python
while choice != "4":
```
This prevents the program from ending after only one action.
Also used a for loop to display all words stored in the list:
```python
for i, word in enumerate(word_list):
    print(word)
```
Similarly,  Maths Tutorial  repeatedly generates maths questions using a loop:
```python
while correct < target:
```
Loops reduce duplicated code and make programs more efficient and interactive.
For example,  **while choice != "4":**  keeps the menu running until the user exits,however,
```python
for i, word in enumerate(word_list):
```
is used to iterate through all the words in the list.
## Modularity & Functional Decomposition
Modularity means dividing a program into smaller reusable parts. Functional decomposition means breaking a large problem into smaller functions.
Demonstrated this clearly in the stopping distance calculator program through the calculate_distance() function:
```python
`def calculate_distance(velocity: float, time: float) -> float:
    distance = velocity*time+(velocity**2)/(2*FRICTION*GRAVITY)
    return distance
```
This function performs only one task, which makes the code easier to test and reuse.
I also applied modularity in the Turtle graphics :
```python
def place_stamp(stamper: Turtle, x: float , y: float, ink:str):
```
Instead of placing all drawing instructions inside main(), I separated the drawing logic into its own function. This improves code organisation and readability.
For example:
```python
def calculate_distance():
```
Specifically responsible for calculating braking distances.
```python
def place_stamp():
```
This separates the drawing logic from the main program, making the code easier to maintain.
## Variables
Store data that can change during execution.
```python
velocity = float(input("Input initial velocity:"))
```
```python
words: list[str] = []
```
Allowed programs to store user input and process information dynamically.
## Functions
Improve code reuse and organisation.
```python
show_heading()
average_len()
one_attempt()
```
Each function performs a specific task, making the overall program easier to understand.
## main() Function
Programs used a main() function as the entry point.This structure improves professionalism and allows functions to be reused in other files.
```python
if __name__ == "__main__":
    main()
```
## Lists & Dictionaries
Dictionaries store data using key-value pairs and are useful in larger software systems.
```python
words:list[str]=[]
```
This structure is useful because related information can be grouped together using key-value pairs.
```python
For example, a dictionary could store rider information in the Tour de France program:

```python
rider = {
    "name": first_place,
    "country": country_1,
    "time": time_1
}
```
## Dataclasses
Custom data types are important for organizing complex data, as they can improve the readability and maintainability of programs.
```python
@dataclass
class Rider:
```
