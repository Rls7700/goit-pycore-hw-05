import sys
from collections import defaultdict
from typing import Dict, List, Optional


def parse_log_line(line:str) -> Optional[dict]:
    """парсить рядок логу повертає None якщо рядок неправильий"""
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return None
    
    date, time, level, message = parts
    return {
        "date": date, 
        "time": time, 
        "level": level.upper(), 
        "message": message 
    }


def load_logs(file_path: str) -> List[dict]:
    """Завантажує файл та повертає список логів"""
    logs: List[dict] = []

    try:
        with open(file_path, "r", encoding = "utf-8") as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)

    except FileNotFoundError:
        print(f"Файл не знайдено -> {file_path}")
        sys.exit(1)

    except OSError as e:
        print(f"Помилка читання файлу {e}")
        sys.exit(1)

    return logs


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    """Фільтрує логи за рівнем info/error/debug/warning"""
    level = level.upper()
    return list(filter(lambda log: log.get("level") == level, logs))


def  count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    """Підраховує кількість записів для кожного рівня"""
    counts: Dict[str, int] = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return dict(counts)


def display_log_counts(counts: Dict[str, int]) -> None:
    """Друкує таблицю"""
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    order = ["INFO", "DEBUG", "ERROR", "WARNING"]
    for level in order:
        if level in counts:
            print(f"{level:<16} | {counts[level]}")


def displsy_logs_details(level: str, logs: List[dict]) -> None:
    """Друкує деталі логів для обраного рівня"""
    print(f"\nДеталі логів для рівня '{level.upper()}':")

    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Викоритсання python main.py шлх до лог файлу .log[level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) >= 3 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered = filter_logs_by_level(logs, level)
        displsy_logs_details(level, filtered)
        

if __name__ == "__main__":
    main()