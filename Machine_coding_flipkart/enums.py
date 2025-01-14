from enum import Enum

class Severity(Enum):
    P0=0,
    P1=1,
    P2=2

class Impact(Enum):
    LOW=0,
    MODERATE=1,
    HIGH=2

class FeatureStatus(Enum):
    OPEN=0,
    IN_PROGRESS=1,
    TESTING=2,
    DEPLOYED=3

class BugStatus(Enum):
    OPEN=0,
    IN_PROGRESS=1,
    FIXED=2,

class StoryStatus(Enum):
    OPEN=0,
    IN_PROGRESS=1,
    COMPLETED=2,

class SubTaskStatus(Enum):
    OPEN=0,
    IN_PROGRESS=1,
    COMPLETED=2,


