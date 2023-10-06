from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Code status is not equal to expected."
    WRONG_NUMBER_OF_POSTS = "The number of posts is not the correct expected."
