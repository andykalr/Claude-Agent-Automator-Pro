from agent.utils import helper_print
from datetime import datetime

tasks = ["Collect data", "Analyze data", "Generate report"]

def complete_task(task_name: str, completed_count: int) -> int:
    helper_print(f"Completing task: {task_name}")
    completed_count += 1
    helper_print(f"Task '{task_name}' completed. Total tasks: {completed_count}")
    return completed_count

def run_all_tasks():
    completed_count = 0
    helper_print("Starting Claude Agent")
    for task in tasks:
        completed_count = complete_task(task, completed_count)
    last_run = datetime.now().isoformat()
    helper_print(f"All tasks done. Total completed: {completed_count}, Last run: {last_run}")