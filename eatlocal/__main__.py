import eatlocal
import cli


def main():
    args = cli.get_args()
    if args.extract:
        eatlocal.extract_bite(args.extract)
    else:
        eatlocal.submit_bite(args.submit)


if __name__ == "__main__":
    main()
