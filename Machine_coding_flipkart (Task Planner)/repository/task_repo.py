from model.sprint import  Sprint
from model.task import Task, SubTask
from model.type import Story, Feature, Bug
from repository.sprint_repo import SprintRepo
from repository.sprint_repo import SprintRepo
from enums import  Severity, Impact, FeatureStatus, BugStatus, StoryStatus, SubTaskStatus

class TaskRepo:
    def __init__(self):
        self.tasks = {}

    def get_task(self, task_title):
        if task_title not in self.tasks:
            raise Exception(f"Task: {task_title} Not Found")
        return  self.tasks[task_title]

    def add_task(self, task):
        if task.title in self.tasks:
            raise Exception(f"Task: {task.title} already Exists")
        self.tasks[task.title] = task

    def remove_task(self, task_title):
        if task_title in self.tasks:
            del self.tasks[task_title]

    def get_all_tasks(self):
        return list(self.tasks.values())