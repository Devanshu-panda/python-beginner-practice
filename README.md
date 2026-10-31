# Python Beginner Practice

This repository contains my beginner Python practice codes as I build strong programming fundamentals.

I have completed the **CodingBat Python** practice sections and uploaded my solutions here to track my learning progress. I have also started building small beginner-level Python mini-projects to apply the concepts I have learned.

## Current Progress

✅ Completed CodingBat Python
✅ Created beginner Python mini-project: Student Marks Analyser
✅ Created beginner Python mini-project: Personal Expense Tracker
✅ Created beginner Python mini-project: Tic-Tac-Toe

## Folder Structure

```text
python-beginner-practice/
├── CodingBat/
│   ├── warmup_1.py
│   ├── warmup_2.py
│   ├── string_1.py
│   ├── string_2.py
│   ├── list_1.py
│   ├── list_2.py
│   ├── logic_1.py
│   └── logic_2.py
│
├── python_mini_projects/
│   ├── student_marks_analyser.py
│   ├── personal_expense_tracker.py
│   └── tic_tac_toe.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Topics Practiced

* Python functions
* Conditional statements
* Loops
* String operations
* List operations
* Boolean logic
* Basic problem solving
* Lists and dictionaries
* Input validation
* Menu-based program flow
* Game logic

## Mini Projects

### Student Marks Analyser

A beginner Python program that takes student marks as input and analyzes the result.

#### Features

* Takes marks as input
* Calculates total marks
* Calculates average marks
* Displays grade/result
* Uses basic conditions and loops

#### Concepts Used

* Variables
* Lists
* Loops
* Conditional statements
* Basic calculations
* Input handling

---

### Personal Expense Tracker

A menu-based Python program to add, view, delete, and summarize personal expenses.

#### Features

* Add expenses with amount, category, and description
* View all expenses
* View total spending
* View expenses by category
* Show highest expense
* Delete an expense
* Show category-wise summary

#### Concepts Used

* Lists
* Dictionaries
* Loops
* Conditional statements
* Input validation
* Menu-based program flow
* Basic data handling

---

### Tic-Tac-Toe

A command-line Tic-Tac-Toe game built using Python, featuring both
two-player gameplay and computer opponents with different difficulty levels.

#### Features

* Player vs Player mode
* Player vs Computer (Easy) — computer selects a random available position
* Player vs Computer (Intelligent) — uses Groq API with the
  `openai/gpt-oss-20b` model to analyse the board and choose moves
* Interactive 3×3 game board
* Custom player names
* Input validation and prevention of occupied-position selection
* Automatic winner and draw detection
* Intelligent mode includes retries for invalid AI moves and a random
  legal-move fallback

#### Concepts and Technologies Used

* Python functions and modular programming
* Lists and loops
* Conditional statements
* Input validation
* Random module
* Groq API
* Large Language Models (LLMs)

#### How to Run

Follow these steps to run the Tic-Tac-Toe game on macOS or Linux.

**1. Clone the repository**

```bash
git clone https://github.com/Devanshu-panda/python-beginner-practice.git
cd python-beginner-practice
```

**2. Create a virtual environment**

```bash
python3 -m venv .venv
```

**3. Activate the virtual environment**

```bash
source .venv/bin/activate
```

**4. Install the required dependencies**

```bash
pip install -r requirements.txt
```

**5. Set your Groq API key**

```bash
export GROQ_API_KEY="your_groq_api_key"
```

Replace `your_groq_api_key` with your actual API key.

**6. Run the game**

```bash
python python_mini_projects/tic_tac_toe.py
```

**7. Deactivate the virtual environment when finished**

```bash
deactivate
```

**Note:** The Groq API key is currently required at startup, even if you select Player vs Player or Easy mode.

## What I Learned

Through CodingBat practice and beginner mini-projects, I improved my ability to:

* Break problems into small steps
* Write function-based solutions
* Use if-else conditions correctly
* Work with strings and lists
* Use dictionaries for storing structured data
* Validate user input
* Build simple menu-based programs
* Implement basic game logic
* Think logically before writing code

## Note

The CodingBat solutions are kept as part of my beginner learning journey. Some solutions may not be the most optimized or Pythonic, but they represent my original practice work while learning Python fundamentals.

The mini-projects are also part of my learning process and will be improved as I learn more Python concepts.

## Next Steps

Now that I have completed CodingBat Python and started building beginner mini-projects, my next goals are:

* Practice more beginner-to-intermediate Python problems
* Build more small Python projects
* Improve code structure using functions
* Learn basic file handling
* Continue improving problem-solving skills
* Gradually build more advanced Python projects

## License

This repository is licensed under the MIT License.
