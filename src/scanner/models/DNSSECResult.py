from dataclasses import dataclass
import pandas as pd

from src.scanner.models.Algorithm import Algorithm
from src.scanner.models.DNSSECStatus import DNSSECStatus
from src.scanner.models.DigestAlgorithm import DigestAlgorithm
from src.scanner.models.NonExistenceProofMethod import NonExistenceProofMethod
from src.scanner.models.grade import Grade


@dataclass
class DNSSECResult:
    assessment_datetime: pd.Timestamp
    raw_result: str
    algorithms: list[Algorithm]
    digest_algorithms: list[DigestAlgorithm]
    non_existence_proof_method: NonExistenceProofMethod
    score: float
    grade: Grade
    dnssec_status: DNSSECStatus
