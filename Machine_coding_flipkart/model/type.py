class Feature:
    def __init__(self, summary, impact):
        self.summary = summary
        self.impact = impact

    def __repr__(self):
        return f'Feature: {self.summary}, {self.impact}'

class Bug:
    def __init__(self, severity):
        self.severity = severity

    def __repr__(self):
        return f'Bug: {self.severity}'

class Story:
    def __init__(self , summary):
        self.summary = summary
        self.sub_tasks = []

    def __repr__(self):
        return f'Story: {self.summary}, {self.sub_tasks}'
