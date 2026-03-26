from agent.tasks import run_all_tasks
from agent.utils import get_claude_key

def main():
    claude_key = get_claude_key()  # safe API access
    run_all_tasks()

if __name__ == "__main__":
    main()