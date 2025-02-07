from enum import Enum


class DNSKeyType(Enum):
    KSK = "Key Signing Key (KSK)"
    ZSK = "Zone Signing Key (ZSK)"
