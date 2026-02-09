# Python Refresher: Data Structures & Logic (Week 2) - Student Workbook
*The Foundation of the "Course Assignment Manager" Data Model*

**Instructions:** This is your workbook for the week. As we go through the concepts, you will write the code in the provided Python files. The code blocks here are empty placeholders for you to fill in during the lesson or practice.


## 0. Start Here: Create the Assignment Manager Project + GitHub Repo
*A clean starting point so we can code, save, and submit all semester.*

**Goal:** By the end of this setup, you will have:
- A project folder on your computer
- A `week2/` folder with small Python files (one per sub-goal)
- A `.env` file (ignored by Git) for later course configuration
- A GitHub repo connected to your folder (so you can push/submit work)

### Step A: Create and open the project folder
1. Create a folder named `misy350-assignment-manager`.
2. Open it in VS Code: **File > Open Folder...**

### Step B: Create the starter files
Create these files in the project folder:
- `week2/` (folder)
- `week2/01_variables.py` (start here; we will create a new file for each section)
- `.gitignore` (**Root folder**, NOT inside `week2/`)
- `.env` (**Root folder**, NOT inside `week2/`)

> **Double Check:** Make sure `.gitignore` and `.env` are in the main project folder `misy350-assignment-manager/`, alongside the `week2/` folder.

Paste this into `.gitignore` (minimum recommended):
```gitignore
# Secrets (never commit these)
.env

# Python
__pycache__/
*.pyc
.venv/

# OS junk
.DS_Store
Thumbs.db
```

Create a file named `.env` and add **fake/placeholder values** (never real secrets):
```bash
API_KEY="paste_key_here" #replace paste_key_here with a random value
DEBUG=true
```

> **Note:** We are creating this `.env` file now to establish good security habits. We won't actually read these values in our Python code this week.

For a quick sanity check, paste this into `week2/01_variables.py`:
```python
# TODO: Write a print statement to confirm setup is working
```

Run it in the VS Code terminal:

> **What is `bash`?** When you see a code block labeled `bash`, it stands for "Bourne Again SHell". It simply means "Type these commands into your Terminal window" (not into a file).

```bash
python week2/01_variables.py
# If you're on macOS and `python` doesn't work:
python3 week2/01_variables.py
```

After it runs, replace the contents of `week2/01_variables.py` with the code in Section 1 below.

### Step C: Turn the folder into a GitHub repo (first push)
In the VS Code terminal (inside your project folder):
```bash
git init
git add .
git commit -m "Initialize Assignment Manager project"
```

If `git commit` fails with "Please tell me who you are", see `Git_Setup.md` Part 3 (“Configure Git Identity”).

Then publish to GitHub from VS Code (recommended):
- Open **Source Control**
- Click **Publish Branch / Publish to GitHub**
- Choose **private** unless your instructor says public

**If you get stuck:** see `Git_Setup.md` (Part 6: Create a Repo + Push to GitHub).

### Quick Practice (2-3 min)
1. In VS Code Source Control, check which files are tracked vs untracked.
2. Confirm `.env` is ignored by Git (not tracked).
3. Create a new file `week2/00_notes.txt` and write one sentence (this is just a practice change you can commit).

---

### Why We Use Multiple Files in Week 2
This week we intentionally create **multiple small `.py` files** (one per mini-goal). This keeps each part short, runnable, and focused so students don't lose the point of the current section.

**Week 2 file map (create as we go):**
1. `week2/01_variables.py`
2. `week2/02_lists.py`
3. `week2/03_assignment_dict.py`
4. `week2/04_database_list_of_dicts.py`
5. `week2/05_nested_questions.py`
6. `week2/06_loops_enumerate.py`
7. `week2/07_conditionals_and_comparisons.py`
8. `week2/08_crud_by_id.py`
9. `week2/09_cli_assignment_tracker.py`

Run any file like this:
```bash
python week2/02_lists.py
# If you're on macOS and `python` doesn't work:
python3 week2/02_lists.py
```

**Git checkpoint:** Save your work to GitHub at the end of this section.

## 1. Defining Variables
*Naming and storing a single piece of data.*

Variables let us store a value under a name so we can reuse it later.

**File:** `week2/01_variables.py`

*   **Syntax:** `name = value`
*   **Naming:** Use clear, lowercase names with underscores.
*   **Reassignment:** Variables can be updated as the program runs.

### Constants (Static Values)
Values that should not change while the app runs are often called "constants". In Python, we use **ALL_CAPS** to signal “constant-ish” values.

*   **Tip:** Define these at the top of your file.
*   **Examples:** `APP_TITLE`, `DEFAULT_POINTS`, `ALLOWED_STATUSES`.

```python
# TODO: Define constants (UPPERCASE) like APP_TITLE, DEFAULT_POINTS, ALLOWED_STATUSES
# TODO: Define standard variables (lowercase) like assignment_title, description, due_date, and is_published
# TODO: Print each variable

# TODO: Experiment with f-strings
```

### f-Strings (Formatted Strings)
Sometimes you want to build **one string** that includes values (common in apps, especially for UI labels, status messages, and errors).

- **Syntax:** put an `f` before the quotes: `f"..."`, then use `{}` to insert values.

```python
# TODO: Write code to print "Due date:" followed by the variable, using f-strings
```

### Quick Practice (2-3 min)
1. Add a constant named `COURSE_CODE` with value `"MISY350"` and print it.
2. Change `assignment_title` to a different database-related assignment (keep it realistic).
2. Add one more variable named `points_possible` and print it.
3. Change `is_published` to `True` and print it again.

**Git checkpoint:** Save your work to GitHub.

## 2. The List: Ordered Collections
*Storing multiple values in a single variable.*

Lists keep items in order and let you add, remove, or look up values by position.

**File:** `week2/02_lists.py`

*   **Definition:** An ordered collection of values.
*   **Use Cases:** Student names, assignment titles, scores.
*   **Common Ops:** `len`, indexing (`items[0]`), adding items with `.append()`.

```python
# TODO: Create a list of 'titles'
# TODO: Add a new title using .append()
# TODO: Print the list, the first item, the last item, and the count (len)
```

### Quick Practice (2-3 min)
1. Add one more title using `.append()`.
2. Print the second item in the list using indexing.
3. Print `"Total assignments:"` with `len(titles)`.

**Git checkpoint:** Save your work to GitHub.

## 3. The Dictionary: Modeling "Things"
*The most important data structure for this course.*

We don't use 5 separate lists (`titles = []`, `dates = []`). We use **Dictionaries** to group related data into a single object.

**File:** `week2/03_assignment_dict.py`

*   **Definition:** A dictionary is a collection of key–value pairs that maps a unique key to a value.
*   **Use Cases:** Model real-world “things” (assignments, students, products) where each field has a name.

*   **Concept:** Key-Value pairs (e.g., `"title"` is the key, `"Homework 1"` is the value).
*   **The "Assignment" Model:**
    ```python
    # TODO: Create the 'assignment' dictionary with keys: id, title, description, due_date, available, questions
    
    # TODO: Check if a key exists before accessing it (safe pattern)

    # TODO: Update the 'available' status to True

    # TODO: Add a new key for 'feedback'
    ```
*   **Crucial Operations:**
    *   **Accessing:** `assignment["title"]`
    *   **Updating:** `assignment["available"] = True`
    *   **Adding Keys:** `assignment["feedback"] = "Great job!"`

### Quick Practice (3 min)
1. Create a second dictionary named `assignment2` with a new `"id"` and `"title"` (keep it realistic).
2. Add a new key on `assignment2` named `"points_possible"` and set it to `100`.
3. Use `if "description" in assignment2:` to decide whether to print the description (don’t crash if it’s missing).

**Git checkpoint:** Save your work to GitHub.

## 4. The List of Dictionaries: The "Database"
*How we store the entire course history.*

In Phase 1 & 2, our "Database" is simply a Python List containing Dictionary objects (not a real database yet). This list matches how real databases return results (as rows of data).

**File:** `week2/04_database_list_of_dicts.py`

*   **The Structure:**
    ```python
    # TODO: Create the 'course_data' list containing multiple assignment dictionaries

    # TODO: Add one more record using .append()

    # TODO: Loop through course_data and print the details
    ```
*   **Crucial Operations:**
    *   **Adding (Create):** `course_data.append(new_assignment)`
    *   **Looping (Read):** Iterating through the list to print summaries.
    *   **Filtering:** Creating a new list of only "A" grades.

### Quick Practice (3 min)
1. Add one more record (a dictionary) to `course_data` using `.append()`.
2. Write a loop that counts how many items have `score == 0` and print the count.
3. Write a loop that finds the title for `"HW2"` and prints it (use an `if` inside the loop).

**Git checkpoint:** Save your work to GitHub.

## 5. Nested Data: Questions (List Inside the Dictionary)
In the running case, each assignment contains a `questions` list. Each question is also a dictionary.

**File:** `week2/05_nested_questions.py`

```python
# TODO: Create an assignment dictionary that includes an empty 'questions' list

# TODO: Create question dictionaries (Task 1, Task 2...)

# TODO: Add the questions to assignment["questions"]

# TODO: Update the content of the first question

# TODO: Delete a question by index
```

### Quick Practice (3 min)
1. Create `question_4` (a dictionary) and add it to `assignment["questions"]` using `.append()`.
2. Update the `"content"` of the first question using indexing (no loops needed).
3. Delete the last question using `del` with an index.

**Git checkpoint:** Save your work to GitHub.

## 6. The Loop: Processing Data
*Connecting Data to Action.*

We rarely work with single items. We work with *collections*. The `for` loop is our primary tool for processing these collections.

**File:** `week2/06_loops_enumerate.py`

```python
# TODO: Create a list of titles
# TODO: Use enumerate() to look through titles and print them with a number (Index + 1)

# TODO: Loop through a list of dictionaries (course_data) and access keys inside the loop

# TODO: Search for a specific record (The "Challenge" pattern)
# 1. Define search_title
# 2. Loop through course_data
# 3. If title matches, save to found_assignment and break
# 4. Print result
```

### Quick Practice (3 min)
1. Make a new list named `statuses = ["Draft", "Published", "Archived"]` and print a numbered menu using `enumerate(..., start=1)`.
2. Using `course_data`, print only the assignments where `score >= 90`.
3. **Bulk Update:** Add `"status": "Published"` to one assignment in `course_data`. Write a loop that finds any assignment with `status == "Published"` and changes it to `"Archived"`.

**Git checkpoint:** Save your work to GitHub.

## 7. If/Else & Logical Operators
*The decision engine for validation and filtering.*

*   **`if / elif / else`:** Branching logic to handle required fields and edge cases.
*   **Logical Operators:** `and`, `or`, `not` let you combine conditions.

**File:** `week2/07_conditionals_and_comparisons.py`

```python
# TODO: Define variables for testing (points, title, due_date)

# TODO: Write 'if' statements to validate the data
# Example: Check if points are < 0 or > 100
# Example: Check if title is empty

# TODO: Print "Ready to save" only if valid
```
### Quick Practice (3 min)
1. Set `points = 120` and confirm your validation prints `"Invalid points."`.
2. Set `title = ""` and confirm your validation prints `"Title required"`.
3. Restore valid values and confirm it prints `"Ready to save."`.

**Git checkpoint:** Save your work to GitHub.

## 8. Operands & Comparing Strings
*Comparisons are about values (operands) and operators.*

**File:** `week2/07_conditionals_and_comparisons.py` (continue)

```python
# TODO: Compare strings (e.g., status == "Draft")
# TODO: Compare numbers (points, average)
# TODO: Use boolean variables in if statements

# TODO: Complex logic: combine conditions with 'and' / 'not'
```

### Quick Practice (2-3 min)
1. Create a variable `status = "Published"` and write an `if` that prints `"Show on dashboard"` only when the status is exactly `"Published"`.
2. Create two strings that differ only by case (example: `"Draft"` and `"draft"`) and compare them with `==` to see what happens.

**Git checkpoint:** Save your work to GitHub.

---

## 9. Debugging: The "Top 3" Errors
*What will break your code this week.*

1.  **`KeyError`**: Trying to access a dictionary key that doesn't exist.
2.  **`IndexError`**: Trying to access a list index that is out of range.
3.  **`TypeError`**: Trying to call a variable like a function (e.g., naming a variable `list` then calling `list()`).

### Quick Practice (3 min)
1. Create a `course_data` list with one dictionary, then purposely type the wrong key name once to trigger a `KeyError`, and fix it.
2. Make a list with 2 items, then try to print `items[2]` to see an `IndexError`, and fix it by using a valid index.
3. Name a variable `dict = {}` once, see what breaks, then rename it to `assignment_dict`.

**Git checkpoint:** Save your work to GitHub.

---

## 10. CRUD Patterns (Create / Read / Update / Delete) By `id`
This is the core logic behind the Streamlit app screens.

**File:** `week2/08_crud_by_id.py`

**What is CRUD?**
* **C**reate: Add a new record.
* **R**ead: Display records or find a specific one.
* **U**pdate: Change details of an existing record.
* **D**elete: Remove a record permanently.

### 10A. Create (Adding Items with IDs)

```python
assignments = []
next_id_number = 1  # State variable to track the next ID

# --- CREATE ---
# TODO: Generate a new ID ("HW" + next_id_number)
# TODO: Increment next_id_number
# TODO: Create a dictionary and append it to 'assignments'
```

**Practice Tasks:**
1.  **Add a 3rd assignment:** Manually generate a new ID (using `next_id_number`) and append a "Homework 3".
2.  **Add a 4th assignment:** Do it again for "Midterm Project".

### 10B. Read (Print & Find/Search)

```python
# --- READ (List All) ---
# TODO: Loop through 'assignments' and print ID + Title

# --- READ (Find/Search) ---
# TODO: Define a search_id
# TODO: Loop to find the matching dictionary
# TODO: Print the result if found, else print "Not found"
```

**Practice Tasks:**
1.  **Print only available:** Write a loop that prints *only* assignments where `"available"` is `True`.
2.  **Search by Title:** Create a variable `search_title = "Homework 3"`. Loop through the list to find the assignment with that title.

### 10C. Update (Find ID then Modify)

```python
# --- UPDATE ---
# TODO: Define an update_id
# TODO: Loop to find the record
# TODO: If found, update title or available status
```

**Practice Tasks:**
1.  **Publish HW2:** Find the assignment with ID `"HW2"` and change its `"available"` status to `True`.
2.  **Rename HW3:** Find `"HW3"` and add `" (Final Version)"` to the end of its title.

### 10D. Delete (Find Index then Remove)

```python
# --- DELETE ---
# TODO: Define a delete_id
# TODO: Loop using enumerate() to find the index
# TODO: If index found, use 'del' to remove it
```

**Practice Tasks:**
1.  **Delete First Item:** Set `delete_id` to `"HW1"` and run the delete logic.
2.  **Delete Non-Existent:** Set `delete_id` to `"HW99"` (which doesn't exist) and verify your code prints "ID not found" instead of crashing.

**Git checkpoint:** Save your work to GitHub.

## 11. Example: The "CLI" Assignment Tracker
*CLI = Command-Line Interface: a text-based way to run programs by typing commands.*
*A text-based practice for what will become the Streamlit App.*

**File:** `week2/09_cli_assignment_tracker.py`

```python
# The Data (State)
# TODO: Create a list of assignments with 'id', 'title', 'is_completed'

# Show pending (Read)
# TODO: Loop through and print only incomplete assignments

# Mark completed (Update)
# TODO: Find an assignment by ID (set a variable first), mark it True, and break

# Show pending again
# TODO: Print the list again to verify the change
```

Run it:
```bash
python week2/09_cli_assignment_tracker.py
# If you're on macOS and `python` doesn't work:
python3 week2/09_cli_assignment_tracker.py
```

### Quick Practice (4 min)
1. Add a third assignment dictionary to `assignments` using `.append()` (set `"is_completed": False`).
2. Change the target `assignment_id` and confirm your update logic marks it completed.
3. Add a delete step: find the index for a chosen `assignment_id` using `enumerate` then `del` that item.

**Git checkpoint:** Save your work to GitHub.