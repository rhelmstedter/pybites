import eatlocal
import cli


def main():
    args = cli.get_args()
    eatlocal.extract_bite(args.extract)
    eatlocal.submit_bite(args.submit)


if __name__ == "__main__":
    main()
