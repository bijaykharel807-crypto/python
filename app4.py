import sqlite3
import argparse
import sys


DB_NAME = "tasks.db"

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the tasks table if it doesn't exist."""
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'Pending'
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def add_task(self, title, description):
        """CREATE: Add a new task."""
        query = "INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)"
        self.cursor.execute(query, (title, description, "Pending"))
        self.conn.commit()
        print(f"✅ Task '{title}' added successfully.")

    def list_tasks(self):
        """READ: List all tasks."""
        query = "SELECT id, title, description, status FROM tasks"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        
        if not rows:
            print("📭 No tasks found.")
            return

        print(f"{'ID':<5} {'Status':<12} {'Title':<20} {'Description'}")
        print("-" * 60)
        for row in rows:
            t_id, title, desc, status = row
            
            desc_display = (desc[:30] + '..') if len(desc) > 30 else desc
            print(f"{t_id:<5} {status:<12} {title:<20} {desc_display}")

    def update_task_status(self, task_id, new_status):
        """UPDATE: Update the status of a task."""
    
        self.cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        if not self.cursor.fetchone():
            print(f"❌ Task ID {task_id} not found.")
            return

        query = "UPDATE tasks SET status = ? WHERE id = ?"
        self.cursor.execute(query, (new_status, task_id))
        self.conn.commit()
        print(f"🔄 Task ID {task_id} updated to '{new_status}'.")

    def delete_task(self, task_id):
        """DELETE: Remove a task."""
        self.cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        if not self.cursor.fetchone():
            print(f"❌ Task ID {task_id} not found.")
            return

        query = "DELETE FROM tasks WHERE id = ?"
        self.cursor.execute(query, (task_id,))
        self.conn.commit()
        print(f"🗑️  Task ID {task_id} deleted.")

    def close(self):
        self.conn.close()


def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager with CRUD operations")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Task title")
    add_parser.add_argument("--desc", type=str, default="", help="Task description (optional)")


    subparsers.add_parser("list", help="List all tasks")

    
    update_parser = subparsers.add_parser("update", help="Update task status")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("status", type=str, choices=["Pending", "InProgress", "Done"], help="New status")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    
    args = parser.parse_args()
    
    
    db = DatabaseManager()

    
    try:
        if args.command == "add":
            db.add_task(args.title, args.desc)
        elif args.command == "list":
            db.list_tasks()
        elif args.command == "update":
            db.update_task_status(args.id, args.status)
        elif args.command == "delete":
            db.delete_task(args.id)
        else:
            parser.print_help()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()