import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from json import JSONDecodeError

BASE_DIR = Path(__file__).resolve().parent
TASK_FILE = BASE_DIR / "tasks.json"


    

app = FastAPI()

class Task (BaseModel):
    title: str
    description: str
    completed: bool
    @field_validator ("title")
    @classmethod
    def strip_whitespace (cls, value: str) -> str:
        cleaned_value = value.strip()
        if cleaned_value == "":
            raise ValueError("Field cannot be empty")
        return cleaned_value

def load_tasks():
    
    try:
        with open (TASK_FILE, "r") as file:
            tasks = json.load(file)

    
            
            if not isinstance (tasks, list):
                raise ValueError("tasks.json must be a list")
            required_keys = {"id", "title", "description", "completed"}
            seen_ids = set()
            
            for task in tasks:
                if not isinstance (task, dict):
                    raise ValueError("every task must be a dictionary")

                if not required_keys.issubset(task):
                    raise ValueError ("tasks is missing one or more required keys")

                if not isinstance (task["title"], str):
                    raise ValueError ("title must be a string")
                                
                cleaned_title = task["title"].strip()
                if cleaned_title == "":
                    raise ValueError("title cannot be empty")
                
                if type(task["id"]) != int:
                    raise ValueError ("task ID must be an integer")
                if task["id"] <= 0:
                    raise ValueError ("task ID cannot be less than 1")
                if task["id"] in seen_ids:
                    raise ValueError("task IDs must be unique")
                
                seen_ids.add(task["id"])

                if not isinstance (task["description"], str):
                    raise ValueError ("description must contain only strings")
                if not isinstance (task["completed"], bool):
                    raise ValueError ("completed must be a bool")
            return tasks
    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("your file tasks.json contains invaid JSON")
        raise


def save_tasks(tasks):
    with open (TASK_FILE, "w") as file:
        json.dump(tasks, file, indent = 4)

@app.get ("/tasks")
def get_all_tasks():
    tasks = load_tasks()
    return tasks 

@app.post ("/tasks")
def add_tasks(task: Task):
    tasks = load_tasks()
    highest_id = max((single_task["id"] for single_task in tasks), default = 0)
    new_id = highest_id + 1

    new_task = {
        "id": new_id,
        "title" : task.title,
        "description": task.description,
        "completed": task.completed
    }

    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return task
            
    raise HTTPException(status_code=404, detail= "No task with this ID exists")

@app.put ("/tasks/{task_id}")
def update_task(task_id: int, task: Task):  
    tasks = load_tasks()
    for current_task in tasks:
        if current_task["id"] == task_id:
            current_task["title"] = task.title
            current_task["description"] = task.description
            current_task["completed"] = task.completed
            
            save_tasks(tasks)
            return current_task
raise HTTPException(status_code=404, detail= "No task with that ID exists")

    


    

