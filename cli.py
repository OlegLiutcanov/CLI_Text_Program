# cli.py
import argparse
from core import reverse_text, is_palindrome, count_vowels, word_count, slugify


def main() -> None:
    parser = argparse.ArgumentParser(description="TextLab CLI")
    parser.add_argument("text", help="The text to process")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--reverse", action="store_true", help="Reverse the text")
    group.add_argument("--palindrome", action="store_true", help="Check if text is a palindrome")
    group.add_argument("--count-vowels", action="store_true", help="Count vowels (a, e, i, o, u)")
    group.add_argument("--word-count", action="store_true", help="Count words (split by whitespace)")
    group.add_argument("--slugify", action="store_true", help="Slugify text for URLs")
    args = parser.parse_args()

    if args.reverse:
        print(reverse_text(args.text))
    elif args.palindrome:
        print(is_palindrome(args.text))
    elif args.count_vowels:
        print(count_vowels(args.text))
    elif args.word_count:
        print(word_count(args.text))
    elif args.slugify:
        print(slugify(args.text))


if __name__ == "__main__":
    main()
