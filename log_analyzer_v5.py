def analyze_log(file_name):
    info_count = 0
    warning_count = 0
    error_count = 0

    with open(file_name, "r") as file:
        for line in file:
            if "INFO" in line:
                info_count += 1
            elif "WARNING" in line:
                warning_count += 1
            elif "ERROR" in line:
                error_count += 1

    return info_count, warning_count, error_count


if __name__ == "__main__":
    file_name = input("Enter log file name: ")

    info, warning, error = analyze_log(file_name)

    print("\n===== Log Analysis Report =====")
    print(f"INFO Count    : {info}")
    print(f"WARNING Count : {warning}")
    print(f"ERROR Count   : {error}")
