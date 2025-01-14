from collections import defaultdict

from model.sprint import  Sprint
from model.type import Story, Feature, Bug
from datetime import datetime

class SprintService:
    def __init__(self, sprint_repo , task_repo):
        self.sprint_repo = sprint_repo
        self.task_repo = task_repo

    def create_sprint(self, name):
        sprint = Sprint(name)
        self.sprint_repo.add_sprint(sprint)

    def delete_sprint(self, sprint_name):
        self.sprint_repo.remove_sprint(sprint_name)

    def add_task_to_sprint(self, task_title, sprint_name):
        sprint = self.sprint_repo.get_sprint(sprint_name)
        sprint.tasks.add(task_title)
        task = self.task_repo.get_task(task_title)
        task.sprint = sprint_name

    def delete_task_from_sprint(self, task_title, sprint_name):
        sprint = self.sprint_repo.get_sprint(sprint_name)
        sprint.tasks.remove(task_title)

    def display_sprint_snapshot(self, sprint_name):
        result = defaultdict(list)
        sprint = self.sprint_repo.get_sprint(sprint_name)

        curr_date = datetime.now().date()
        for task_name in sprint.tasks:
            task = self.task_repo.get_task(task_name)
            if  task.due_date > curr_date:
                result['On Track Task'].append(task_name)
            elif isinstance(task, Bug):
                result['Delayed'].append(task_name)

        print(str(result))