import pytest
from project import add_task, complete_task, view_tasks, tasks

def test_add_task():
    tasks.clear()
    add_task("Test Task 1")
    assert len(tasks) == 1
    assert tasks[0]['task'] == "Test Task 1"
    assert not tasks[0]['completed']

def test_complete_task():
    tasks.clear()
    add_task("Test Task 1")
    complete_task(1)
    assert tasks[0]['completed']

def test_view_tasks(capsys):
    tasks.clear()
    add_task("Test Task 1")
    view_tasks()
    captured = capsys.readouterr()
    assert "1. Test Task 1 - Pending" in captured.out
    complete_task(1)
    view_tasks()
    captured = capsys.readouterr()
    assert "1. Test Task 1 - Done" in captured.out

if __name__ == "__main__":
    pytest.main()
