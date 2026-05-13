"""6.1  Option 4: To Do"""


from enum import Enum


class Category(Enum):
    HOME = "Home"
    WORK = "Work"
    UNI = "Uni"


class Task:
    def __init__(self, description: str, category: Category,
                 days_until_due: int, percent_complete: float):
        self.description = description
        self.category = category
        self.days_until_due = days_until_due
        self.percent_complete = percent_complete

    def __str__(self):
        result = f"{self.description} ({self.category.name}) - " \
                 f"{self.days_until_due} days until due - " \
                 f"{self.percent_complete}% complete"

        if self.percent_complete <= 20:
            result += " (Should work on this more)"
        elif self.percent_complete >= 80:
            result += " (Almost there!)"

        return result


def input_category() -> Category:
    """
    Allow the user to select a category from a menu.
        args:none
        return:Category
    """
    print("Select a category:")
    for i, cat in enumerate(Category, start=1):
        print(f"{i}. {cat.value}")

    choice = int(input("Enter choice: "))
    return list(Category)[choice - 1]


def input_task() -> Task:
    """
    Read task details, validate input, and return a Task object.
        args:none
        return:Task
    """
    description = input("Enter description: ")
    days_until_due = int(input("Enter days until due: "))

    percent_complete = float(input("Enter percent complete: "))
    while percent_complete < 0 or percent_complete > 100:
        print("Invalid input. Must be between 0 and 100.")
        percent_complete = float(input("Enter percent complete: "))

    category = input_category()

    return Task(description, category, days_until_due, percent_complete)


def main():
    """This function is for storing tasks to be completed."""
    description: str
    percent_complete: float
    days_until_due: int
    category: Category
    task: Task

    print("Enter task details")

    task = input_task()

    print("Your entered:")
    print(task)


if __name__ == "__main__":
    main()
