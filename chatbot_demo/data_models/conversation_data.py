from enum import Enum


class Operation(Enum):
    NONE = 0
    NEW = 1
    TRACK = 2


class Case(Enum):
    NONE = 0
    TITLE = 1
    DESCRIPTION = 2
    ID = 3


class ConversationData:
    def __init__(
            self,
            prompted_for_user_name: bool = False,
            prompted_for_survey: bool = False,
            last_case_asked: Case = Case.NONE,
            last_operation_asked: Operation = Operation.NONE,
    ):
        self.prompted_for_user_name = prompted_for_user_name
        self.prompted_for_survey = prompted_for_survey
        self.last_case_asked = last_case_asked
        self.last_operation_asked = last_operation_asked
