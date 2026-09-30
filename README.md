## Python Comprehensions

Python comprehensions provide a concise, single-line syntax to create new collections (lists, dictionaries, sets, and generators) from existing iterables. They replace verbose `for` loops, making code cleaner and often faster.

### Quick Syntax Guide

*   **List Comprehension:** Generates a new list.
    ```python
    squares = [x**2 for x in range(10) if x % 2 == 0]
    ```
*   **Dictionary Comprehension:** Builds key-value pairs.
    ```python
    square_dict = {x: x**2 for x in range(5)}
    ```
*   **Set Comprehension:** Creates a collection of unique elements.
    ```python
    unique_lengths = {len(word) for word in ["apple", "banana", "apple"]}
    ```
*   **Generator Expression:** Memory-efficient, lazy evaluation (uses parentheses).
    ```python
    lazy_squares = (x**2 for x in range(1000000))
    ```

### Why Use Them?
*   **Readability:** Reduces boilerplate code by turning multi-line loops into expressive, single lines.
*   **Performance:** Optimized internally in C, making them faster than standard `.append()` loops.
