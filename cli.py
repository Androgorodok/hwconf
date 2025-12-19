import argparse
import sys
import tomli_w

from parser import parser
from transformer import ConfigTransformer


def main():
    ap = argparse.ArgumentParser(
        description="Учебный конфигурационный язык → TOML"
    )
    ap.add_argument("-o", "--output", required=True, help="Выходной TOML-файл")
    args = ap.parse_args()

    # Чтение из stdin согласно заданию
    source = sys.stdin.read()

    try:
        tree = parser.parse(source)
        result = ConfigTransformer().transform(tree)
    except Exception as e:
        print(f"Ошибка трансляции: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(args.output, "wb") as f:
            # Записываем весь результат как TOML документ
            f.write(tomli_w.dumps(result).encode())
    except OSError as e:
        print(f"Ошибка записи файла: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()