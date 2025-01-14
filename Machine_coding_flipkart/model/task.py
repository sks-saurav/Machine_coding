class Task:
    def __init__(self, title , creator ,assignee , status, task_type, due_date):
        self.title = title
        self.creator = creator
        self.assignee = assignee
        self.status = status
        self.task_type = task_type
        self.due_date = due_date
        self.sprint = None

    def __repr__(self):
        return f'Task: {self.title} , {self.creator} ,{self.assignee} , {self.status}, {str(self.task_type)}, {self.due_date}'

class SubTask:
    def __init__(self, title, status):
        self.title = title
        self.status = status

    def __repr__(self):
        return f'SubTask: {self.title}, {self.status}'