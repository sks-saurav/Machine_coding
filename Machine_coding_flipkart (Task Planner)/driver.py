from model.type import Story, Feature, Bug
from repository.sprint_repo import SprintRepo
from repository.task_repo import TaskRepo
from enums import  Severity, Impact, FeatureStatus, BugStatus, StoryStatus, SubTaskStatus

from service.spirnt_service import SprintService
from service.task_service import TaskService
from datetime import date


def main():
    task_repo = TaskRepo()
    sprint_repo = SprintRepo()
    task_service = TaskService(task_repo)
    sprint_service = SprintService(sprint_repo, task_repo)

    try:
        task_service.create_task(
            title='Create a console for debugging',
            creator='Brad',
            assignee='Peter',
            due_date=date(2024, 12, 12),
            task_type = Feature('Create a console for debugging', Impact.LOW),
            status=FeatureStatus.OPEN
        )
        sprint_service.create_sprint('Sprint-1')
        sprint_service.add_task_to_sprint(
            task_title='Create a console for debugging',
            sprint_name='Sprint-1'
        )
        task_service.create_task(
            title='Fix MySQL Issue',
            creator='Ryan',
            assignee='Ryan',
            due_date=date(2024, 12, 14),
            task_type=Bug(Severity.P0),
            status=BugStatus.OPEN
        )
        sprint_service.add_task_to_sprint(
            task_title='Fix MySQL Issue',
            sprint_name='Sprint-1'
        )

        task_service.display_task_assigned(assingee_name="Ryan")
        task_service.display_task_assigned(assingee_name="Peter")


        sprint_service.display_sprint_snapshot(sprint_name='Sprint-1')

        task_service.change_status_task(
            task_title='Create a console for debugging',
            new_task_status=FeatureStatus.IN_PROGRESS
        )

        print('-'*50)
        task_service.create_task(
            title='Create a Microservice',
            creator='Amy',
            assignee='Ryan',
            due_date=date(2024, 12, 18),
            task_type=Story(summary='Story Summary'),
            status=StoryStatus.IN_PROGRESS
        )
        sprint_service.add_task_to_sprint(
            task_title='Create a Microservice',
            sprint_name='Sprint-1'
        )
        task_service.create_a_subtask(
            task_title='Create a Microservice',
            subtask_title='Development',
            subtask_status=SubTaskStatus.OPEN,
        )
        task_service.create_a_subtask(
            task_title='Create a Microservice',
            subtask_title='Unit Test',
            subtask_status=SubTaskStatus.OPEN,
        )
    except Exception as e:
        print(e)

    # task_service.change_status_task(
    #     task_title='Create a Microservice',
    #     new_task_status=StoryStatus.COMPLETED
    # )
    try:
        task_service.create_a_subtask(
            task_title='Create a Microservice',
            subtask_title='Integration Test',
            subtask_status=SubTaskStatus.OPEN,
        )
    except Exception as e:
        print(e)
    sprint_service.display_sprint_snapshot(sprint_name='Sprint-1')
    task_service.display_task_assigned(assingee_name="Ryan")



if __name__ == '__main__':
    main()

