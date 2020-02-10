import argparse


def add(a, b):
    return a + b


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--job', type=str, required=True)
    parser.add_argument('--a', type=str, required=True)
    parser.add_argument('--b', type=str, required=True)

    args = parser.parse_args()

    print(args.job)
    print(int(args.a) + int(args.b))


if __name__ == "__main__":
    main()
