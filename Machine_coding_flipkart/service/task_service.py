from collections import defaultdict
from model.task import Task, SubTask
from model.type import Story, Feature, Bug
from enums import  Severity, Impact, FeatureStatus, BugStatus, StoryStatus, SubTaskStatus


class TaskService:
    def __init__(self, task_repo):
        self.task_repo =task_repo

    def create_task(self, title , creator ,assignee , status, task_type, due_date):
        task = Task( title , creator ,assignee , status, task_type, due_date)
        self.task_repo.add_task(task)

    def create_a_subtask(self, task_title, subtask_title, subtask_status):
        task = self.task_repo.get_task(task_title)
        if not isinstance(task.task_type, Story):
            raise Exception("Subtask cannot be created for non-story task")
        if task.status == StoryStatus.COMPLETED:
            raise Exception("Subtask cannot be added to already completed task")

        sub_task = SubTask(subtask_title, subtask_status)
        task.task_type.sub_tasks.append(sub_task)

    def change_status_task(self, task_title, new_task_status):
        task = self.task_repo.get_task(task_title)
        task.status = new_task_status

    def change_assignee(self, task_title, new_task_assignee):
        task = self.task_repo.get_task(task_title)
        task.assignee = new_task_assignee

    def display_task_assigned(self, assingee_name):
        result = defaultdict(list)

        for task in self.task_repo.get_all_tasks():
            if task.assignee != assingee_name:
                continue

            if isinstance(task.task_type, Story):
                result['Story'].append(str(task))
            elif isinstance(task.task_type, Bug):
                result['Bug'].append(str(task))
            else:
                result['Feature'].append(str(task))

        print(str(result))