"""
Problem 1: Duplicate Tracker
You are given a collection of product IDs. Some IDs may appear more than once.

Write a function that returns True if any duplicates are found, and False otherwise.

Example:

Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen_ids = set()

    for product_id in product_ids:
        if product_id in seen_ids:
            return True
        seen_ids.add(product_id)

    return False


# I chose a set because sets are good for quickly checking whether a value
# has already been seen. Checking and adding values are expected to take O(1)
# time on average, so the full list can be checked in O(n) time.


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.

Implement a class that supports add_task(task) and remove_oldest_task().

Example:

task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if not self.tasks:
            return None

        return self.tasks.pop(0)


# I chose a queue because tasks need to be removed in the same order they
# were added, which follows First In, First Out. Adding to the end of this
# list is O(1) on average, while removing from the front is O(n) because the remaining items shift.


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:

tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:

    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)


# I chose a set because a set automatically keeps only unique values.
# Adding a value is expected to take O(1) time on average, and getting the
# number of unique values with len() is also O(1).