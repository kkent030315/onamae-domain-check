import domainchecker


def main() -> None:
    print(domainchecker.check_domain('google', ['.com']))


if __name__ == '__main__':
    main()
