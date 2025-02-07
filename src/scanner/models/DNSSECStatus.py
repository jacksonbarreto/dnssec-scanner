from enum import Enum


class DNSSECStatus(Enum):
    BAD_DELEGATION = "Bad Delegation"
    INVALID = "Invalid"
    NONE = "None"
    VALID = "Valid"
