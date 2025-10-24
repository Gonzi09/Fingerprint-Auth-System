import sys

sys.path.append(".")
from src.fingerprint import Fingerprint


class MaxTriesExceededError(Exception):
    """Custom exception raised when maximum authentication attempts are exceeded."""

    pass


class Login:
    """Class to handle login attempts with fingerprint authentication."""

    def __init__(self, original: Fingerprint, max_tries: int = 3) -> None:
        # Don't forget to add documentation!
        pass

    def authenticate(self, fp: Fingerprint, match_threshold: float = 0.9) -> bool:
        # Given a FingerPrint `fp`, compare it against the original.
        # Return True if access is granted, False if denied (but not yet locked out).
        # Raise MaxTriesExceededException once max_tries is exceeded.
        pass
