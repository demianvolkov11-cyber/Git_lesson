import json
import sys
from collections import Counter
from pathlib import Path


def process_records(src: Path, dst: Path) -> int:
    try:
        data = json.loads(src.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Ошибка чтения {src}: {exc}", file=sys.stderr)
        return 1

    if not isinstance(data, list):
        print("Ожидался JSON-массив объектов.", file=sys.stderr)
        return 1

    counts = Counter(str(item.get("status", "unknown")) for item in data if isinstance(item, dict))
    report = {"total": len(data), "by_status": dict(counts)}
    dst.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


def main() -> int:
    if len(sys.argv) != 3:
        print("Использование: python script.py <input.json> <output.json>", file=sys.stderr)
        return 2
    return process_records(Path(sys.argv[1]), Path(sys.argv[2]))


if __name__ == "__main__":
    sys.exit(main())

x = 1

print('Hi')