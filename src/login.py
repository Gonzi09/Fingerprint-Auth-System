import sys

sys.path.append(".")
from src.fingerprint import Fingerprint


class MaxTriesExceededError(Exception):
    """Custom exception raised when maximum authentication attempts are exceeded."""

    pass


class Login:
    """Class to handle login attempts with fingerprint authentication."""

    def __init__(self, original: Fingerprint, max_tries: int = 3) -> None:
        """Initialize Login with an original Fingerprint and max tries allowed.

        Stores a private counter for failed attempts.
        """
        self.original = original
        self.max_tries = max_tries
        # private attribute for failed attempts
        self.__failed_attempts = 0

    def authenticate(self, fp: Fingerprint, match_threshold: float = 0.9) -> bool:
        # Given a FingerPrint `fp`, compare it against the original.
        # Return True if access is granted, False if denied (but not yet locked out).
        # Raise MaxTriesExceededException once max_tries is exceeded.
        # If already exceeded or reached max tries, raise
        if self.__failed_attempts >= self.max_tries:
            raise MaxTriesExceededError("Maximum authentication attempts exceeded")

        # Set the class-level threshold for the Fingerprint class as requested
        fp.match_threshold = match_threshold

        # Compare using equality (which uses match_threshold)
        if fp == self.original:
            # reset failed attempts
            self.__failed_attempts = 0
            return True

        # failed authentication
        self.__failed_attempts += 1
        print("Authentication failed")

        # If now exceeded, raise
        if self.__failed_attempts >= self.max_tries:
            raise MaxTriesExceededError("Maximum authentication attempts exceeded")

        return False
