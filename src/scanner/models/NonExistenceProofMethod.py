from enum import Enum


class NonExistenceProofMethod(Enum):
    NSEC = "NSEC"
    NSEC3 = "NSEC3"
    INVALID = "Invalid"
    NONE = "None"
