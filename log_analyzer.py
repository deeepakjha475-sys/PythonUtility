file_name = "application.log"

info_count = 0
warning_count = 0
error_count = 0
total_records = 0

with open(file_name, "r") as file:
    for line in file:
        total_records += 1

        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "ERROR" in line:
            error_count += 1

print("\n===== Log Analysis Report =====")
print(f"Total Records : {total_records}")
print(f"INFO Count    : {info_count}")
print(f"WARNING Count : {warning_count}")
print(f"ERROR Count   : {error_count}")
