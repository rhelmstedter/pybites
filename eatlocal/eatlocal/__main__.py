from .eatlocal import extract_bite, submit_bite
from .cli import get_args


def main():
    args = get_args()
    if args.extract:
        extract_bite(args.extract)
    elif args.submit:
        submit_bite(args.submit)


if __name__ == "__main__":
    main()
