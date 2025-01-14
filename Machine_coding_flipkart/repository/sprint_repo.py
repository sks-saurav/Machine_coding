class SprintRepo:
    def __init__(self):
        self.sprints = {}

    def get_sprint(self, sprint_name):
        if sprint_name not in self.sprints:
            raise Exception("Sprint not found!!")
        return self.sprints[sprint_name]

    def add_sprint(self, sprint):
        if sprint.name  in self.sprints:
            raise Exception("Sprint already Exists")
        self.sprints[sprint.name] = sprint

    def remove_sprint(self, sprint_name):
        if sprint_name in self.sprints:
            del self.sprints[sprint_name]

    def get_all_sprints(self):
        return list(self.sprints.values())
