import csv

def analyze_log(file_name):
    info_count = 0
    warning_count = 0
    error_count = 0

    error_messages = {}

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()

            if "INFO" in line:
                info_count += 1

            elif "WARNING" in line:
                warning_count += 1

            elif "ERROR" in line:
                error_count += 1

                error = line.replace("ERROR", "").strip()

                if error in error_messages:
                    error_messages[error] += 1
                else:
                    error_messages[error] = 1

    if error_messages:
        most_common_error = max(error_messages, key=error_messages.get)
        occurrence = error_messages[most_common_error]
    else:
        most_common_error = "No Errors Found"
        occurrence = 0

    return (
        info_count,
        warning_count,
        error_count,
        most_common_error,
        occurrence
    )


if __name__ == "__main__":

    file_name = input("Enter log file name: ")

    info, warning, error, common_error, occurrence = analyze_log(file_name)

    print("\n===== Log Analysis Report =====")
    print(f"INFO Count    : {info}")
    print(f"WARNING Count : {warning}")
    print(f"ERROR Count   : {error}")

    print("\n===== Most Common Error =====")
    print(f"Error       : {common_error}")
    print(f"Occurrences : {occurrence}")

    with open("log_report.csv", "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow(["Metric", "Count"])

        writer.writerow(["INFO", info])
        writer.writerow(["WARNING", warning])
        writer.writerow(["ERROR", error])
        writer.writerow(["Most Common Error", common_error])
        writer.writerow(["Occurrences", occurrence])

    print("\nCSV report generated successfully.")
