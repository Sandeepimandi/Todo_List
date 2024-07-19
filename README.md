# To-Do List Application

#### Video Demo:https://youtu.be/nXT2b-i7I5Q

#### Description:

This project is a simple To-Do List Application implemented in Python. The application allows users to add tasks, mark tasks as complete, and view the list of tasks. The program is designed to be run from the command line and provides a user-friendly interface for managing tasks.

### Features

- **Add Task**: Users can add new tasks to their to-do list.
- **Complete Task**: Users can mark tasks as completed.
- **View Tasks**: Users can view all tasks along with their completion status.

### Project Structure

The project consists of two main files:

1. `project.py`: This file contains the main application code, including the main function and three additional functions: `add_task`, `complete_task`, and `view_tasks`.
2. `test_project.py`: This file contains the test functions for the `add_task`, `complete_task`, and `view_tasks` functions, implemented using `pytest`.

### Implementation Details

#### `project.py`

- **main()**: Provides an interactive command-line interface for the user to interact with the application. Users can choose to add tasks, complete tasks, view tasks, or exit the application.
- **add_task(task)**: Adds a new task to the list. Each task is represented as a dictionary with an `id`, `task`, and `completed` status.
- **complete_task(task_id)**: Marks a specified task as completed based on the task ID.
- **view_tasks()**: Displays all tasks along with their completion status. Tasks are listed with their IDs, descriptions, and statuses (Pending or Done).

#### `test_project.py`

- **test_add_task()**: Tests the `add_task` function to ensure that tasks are added correctly.
- **test_complete_task()**: Tests the `complete_task` function to ensure that tasks are marked as completed correctly.
- **test_view_tasks(capsys)**: Tests the `view_tasks` function to ensure that tasks are displayed correctly. Uses `capsys` to capture print output for verification.

### Installation

1. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

To run the To-Do List Application, execute the following command:
```bash
python project.py
