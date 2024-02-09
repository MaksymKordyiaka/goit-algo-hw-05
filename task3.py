import sys
import re

def parse_log_line(line: str) -> dict:
    # Розбиваємо рядок логу на компоненти за допомогою регулярного виразу
    match = re.match(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)$', line)
    if match:
        # Розпаковуємо результати регулярного виразу
        timestamp, level, message = match.groups()
        # Повертаємо словник з розібраними компонентами логу
        return {'timestamp': timestamp, 'level': level, 'message': message}
    # Якщо рядок логу не відповідає формату, повертаємо None
    return None

def load_logs(file_path: str) -> list:
    logs = []
    try:
        # Відкриваємо файл для читання
        with open(file_path, 'r') as file:
            # Зчитуємо кожен рядок у файлі
            for line in file:
                # Розбираємо рядок логу та додаємо результат у список логів
                log_entry = parse_log_line(line.strip())
                if log_entry:
                    logs.append(log_entry)
    # Обробляємо помилку відсутності файлу
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    # Фільтруємо логи за рівнем логування
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    # Ініціалізуємо словник для підрахунку логів за рівнем логування
    log_counts = {'INFO': 0, 'DEBUG': 0, 'ERROR': 0, 'WARNING': 0}
    # Підраховуємо кількість логів для кожного рівня логування
    for log in logs:
        log_counts[log['level']] += 1
    return log_counts

def display_log_counts(counts: dict):
    # Виводимо заголовок таблиці
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    # Виводимо кількість логів для кожного рівня логування
    for level, count in counts.items():
        print(f"{level.ljust(17)}| {count}")

def display_log_details(logs: list, level: str):
    # Виводимо деталі логів для вказаного рівня логування
    filtered_logs = filter_logs_by_level(logs, level)
    print(f"\nДеталі логів для рівня '{level}':")
    for log in filtered_logs:
        print(f"{log['timestamp']} - {log['message']}")

def main():
    # Перевіряємо, чи вказано шлях до файлу логу
    if len(sys.argv) < 2:
        print("Usage: python task3.py <log_file> [log_level]")
        sys.exit(1)

    # Отримуємо шлях до файлу логу з аргументів командного рядка
    log_file = sys.argv[1]
    # Отримуємо рівень логування, якщо він вказаний
    log_level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    # Завантажуємо логи з файлу
    logs = load_logs(log_file)
    # Підраховуємо кількість логів за рівнями логування
    counts = count_logs_by_level(logs)
    # Виводимо кількість логів для кожного рівня логування
    display_log_counts(counts)

    # Якщо вказаний рівень логування, виводимо деталі для цього рівня
    if log_level:
        display_log_details(logs, log_level)

if __name__ == "__main__":
    main()