import re


def reverse_text(s: str) -> str:
    """Return the reversed string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """
    Return True if s is a palindrome, ignoring case and non-letters.

    We normalize by keeping only alphabetic characters and lowercasing them,
    then compare from both ends (two-pointer).
    """
    normalized = "".join(ch.lower() for ch in s if ch.isalpha())
    i, j = 0, len(normalized) - 1
    while i < j:
        if normalized[i] != normalized[j]:
            return False
        i += 1
        j -= 1
    return True


def count_vowels(s: str) -> int:
    """Count vowels a/e/i/o/u (case-insensitive)."""
    vowels = {"a", "e", "i", "o", "u"}
    return sum(1 for ch in s.lower() if ch in vowels)


def word_count(s: str) -> int:
    """Count words separated by any whitespace."""
    return len(s.split())


def slugify(s: str) -> str:
    """
    Convert s into a URL-friendly 'slug'.

    Steps:
      1) lowercase
      2) replace any whitespace run with '-'
      3) remove any char not a-z, 0-9, or '-'
      4) collapse multiple '-' into one
      5) strip leading/trailing '-'
    """
    s = s.lower()
    s = re.sub(r"\s+", "-", s)          # whitespace -> single dash
    s = re.sub(r"[^a-z0-9-]", "", s)    # keep only a-z, 0-9, hyphen
    s = re.sub(r"-{2,}", "-", s)        # collapse multiple dashes
    s = s.strip("-")                     # trim ends
    return s

