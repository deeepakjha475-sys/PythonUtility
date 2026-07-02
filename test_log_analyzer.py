from log_analyzer_v5 import analyze_log

info, warning, error, common_error, occurrence = analyze_log("application.log")

assert info == 3
assert warning == 1
assert error == 2

assert common_error == "Database Connection Failed"
assert occurrence == 2

print("All tests passed successfully")
