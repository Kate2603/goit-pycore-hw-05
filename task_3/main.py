import sys
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    """
    Parse a log line into a dictionary containing date, time, level, and message.
    """
    components = line.strip().split(maxsplit=2)
    return {
        "date": components[0],
        "time": components[1],
        "level": components[2].split()[0],
        "message": components[2].split(maxsplit=1)[1]
    }

def load_logs(file_path: str) -> list:
    """
    Load logs from the specified file path.
    """
    try:
        with open(file_path, "r") as file:
            return [parse_log_line(line) for line in file]
    except FileNotFoundError:
        print("Error: Log file not found.")
        sys.exit(1)

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filter logs by the specified logging level.
    """
    return [log for log in logs if log["level"].upper() == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    """
    Count the number of log entries for each logging level.
    """
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return counts

def display_log_counts(counts: dict):
    """
    Display log counts in a formatted table.
    """
    print("Logging level\tNumber")
    print("-----------------------")
    for level, count in counts.items():
        print(f"{level}\t\t{count}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_3/logfile.log [level] ")
        sys.exit(1)

    log_file = sys.argv[1]
    logs = load_logs(log_file)

    if len(sys.argv) == 3:
        log_level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, log_level)
        counts = count_logs_by_level(filtered_logs)
        display_log_counts(counts)
        if filtered_logs:
            print(f"\nLog details for '{log_level.upper()}' level:")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

if __name__ == "__main__":
    main()
