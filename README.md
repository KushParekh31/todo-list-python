# To-Do List (Python)

A command-line task management application built with Python that allows users to create, manage, update, and track tasks with persistent JSON storage.

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Edit existing tasks
* Delete tasks
* Automatically save tasks using JSON
* Track task creation timestamps
* Track task update timestamps
* Track task completion timestamps
* Persistent data storage between sessions

## Requirements

* Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/todo-list-python.git
```

Navigate to the project directory:

```bash
cd todo-list-python
```

Run the application:

```bash
python main.py
```

## Example Menu

```text
===== TO-DO LIST =====

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Edit Task
6. Exit
```

## Example Output

```text
1. [✓] Learn Python
   Created: 17-06-2026 08:30:15
   Updated: 17-06-2026 09:15:40
   Completed: 17-06-2026 09:20:05

2. [✗] Build Portfolio
   Created: 17-06-2026 08:45:00
```

## Project Structure

```text
todo-list-python/
│
├── main.py        # Main application
├── task.json      # Task storage file
└── README.md      # Project documentation
```

## Technologies Used

* Python
* JSON
* Datetime Module
* File Handling

## Learning Objectives

This project demonstrates:

* Functions and modular programming
* CRUD operations
* JSON data storage
* File handling
* Error handling
* Date and time management
* User input validation

## Future Improvements

* Task priorities
* Categories
* Due dates
* Search functionality
* Statistics dashboard
* CSV/PDF export
* SQLite database support
* PyQt6 graphical interface

## Author

Kush Amirash Parekh
