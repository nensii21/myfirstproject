# MyTodo - Simple To-Do List Application

A lightweight, interactive command-line to-do list application built with Python. Perfect for beginners learning Python fundamentals and for anyone who prefers a simple, terminal-based task manager.

## 📋 Project Description

**MyTodo** is a minimalist to-do list application that allows users to:
- View all their tasks in a numbered list
- Add new tasks interactively
- Exit the application cleanly

This project demonstrates core Python concepts including:
- Functions and code organization
- User input handling
- Lists and data structures
- Control flow (loops and conditionals)
- String formatting

## ✨ Features

- **Simple & Intuitive:** Easy-to-use menu-driven interface
- **Task Management:** Add and view tasks with minimal overhead
- **Clean Code:** Well-organized, readable Python code suitable for learning
- **Lightweight:** No external dependencies required
- **Cross-Platform:** Runs on Windows, macOS, and Linux

## 📁 Project Structure

```
myfirstproject/
├── mytodo.py          # Main application file
├── README.md          # Project documentation
├── .gitignore         # Git ignore configuration
└── .vscode/           # VS Code workspace settings
```

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- Git (optional, for cloning the repository)

### Steps

1. **Clone the repository** (or download the files):
```bash
git clone https://github.com/nensii21/myfirstproject.git
cd myfirstproject
```

2. **(Optional) Create and activate a virtual environment:**

   **Windows (PowerShell):**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux (Bash):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

## 💻 Usage

Run the application:
```bash
python mytodo.py
```

### Menu Options

Once the application starts, you'll see:
```
Options: [1] Show Tasks [2] Add Task [3] Exit
Choose an option: 
```

- **[1] Show Tasks** — Display all tasks in a numbered list
- **[2] Add Task** — Add a new task (enter the task description when prompted)
- **[3] Exit** — Quit the application

### Example Session

```
Options: [1] Show Tasks [2] Add Task [3] Exit
Choose an option: 2
Enter a new task: Buy groceries
Added task: Buy groceries

Options: [1] Show Tasks [2] Add Task [3] Exit
Choose an option: 2
Enter a new task: Complete Python project
Added task: Complete Python project

Options: [1] Show Tasks [2] Add Task [3] Exit
Choose an option: 1
Your Tasks:
1. Buy groceries
2. Complete Python project

Options: [1] Show Tasks [2] Add Task [3] Exit
Choose an option: 3
Bye!
```

## 🔧 Technical Details

- **Language:** Python 3.6+
- **Dependencies:** None (uses only the Python standard library)
- **Code Size:** ~25 lines of core logic
- **Concepts:** Functions, lists, user input, loops, conditionals

## 📚 Learning Resources

This project is ideal for beginners to learn:
- How to structure Python code with functions
- Working with data structures (lists)
- Implementing user-driven menus
- Input validation and error handling

## 🛠️ Future Enhancements

Potential improvements for this project:
- [ ] Delete/edit existing tasks
- [ ] Save tasks to a file (persistence)
- [ ] Task priority levels
- [ ] Due dates for tasks
- [ ] Web-based interface using Flask or Django

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by [nensii21](https://github.com/nensii21)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork this repository and submit pull requests.

---

**Happy coding!** 🎉 Feel free to use this project as a learning tool or starting point for more advanced to-do list applications.
