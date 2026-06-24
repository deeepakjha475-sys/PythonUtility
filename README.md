# Log Analyzer Utility

## Overview

Log Analyzer Utility is a Python-based automation tool designed to analyze application log files and generate useful operational insights.

The utility reads application logs, categorizes log entries, extracts error details, and generates reports that can assist support and operations teams in troubleshooting and monitoring activities.

---

## Technologies Used

- Python 3.13
- Git
- GitHub
- CSV

---

## Project Evolution

### Version 1 - Basic Log Analyzer

File:
```
log_analyzer.py
```

Features:
- Reads application log file
- Counts INFO messages
- Counts WARNING messages
- Counts ERROR messages
- Displays summary report

Sample Output:

```
===== Log Analysis Report =====
Total Records : 6
INFO Count    : 3
WARNING Count : 1
ERROR Count   : 2
```

---

### Version 2 - Enhanced Log Analyzer

File:
```
log_analyzer_upgraded.py
```

Additional Features:
- Extracts ERROR messages
- Displays detailed error information
- Improves troubleshooting visibility

Sample Output:

```
===== Error Details =====

1. ERROR Database Connection Failed
2. ERROR Timeout Occurred
```

---

### Version 3 - CSV Report Generator

File:
log_analyzer_v3.py

Additional Features:
- Generates CSV report
- Stores analysis results in structured format
- Enables reporting and data sharing

Generated File:

```
log_report.csv
```

Sample CSV Output:

```csv
Metric,Count
INFO,3
WARNING,1
ERROR,2
```

---

### Version 4 - User Input Support

File:

log_analyzer_v4.py

Additional Features:
- Accepts log file name from the user at runtime
- Eliminates hardcoded file dependency
- Improves reusability and flexibility
- Supports analysis of different log files without code changes

Sample Execution:

python log_analyzer_v4.py

Sample Input:

application.log

Sample Output:

===== Log Analysis Report =====
Total Records : 6
INFO Count    : 3
WARNING Count : 1
ERROR Count   : 2

CSV report generated successfully

## Execution Steps

Run Version 1:

python log_analyzer.py

Run Version 2:

python log_analyzer_upgraded.py

Run Version 3:

python log_analyzer_v3.py

Run Version 4:
python log_analyzer_v4.py

---

## Business Value

- Helps identify application issues quickly
- Provides summarized log analysis
- Reduces manual effort in log review
- Demonstrates automation and scripting capability
- Can be extended for enterprise monitoring solutions

---

## Future Enhancements

- User-supplied input file
- JSON report generation
- Dashboard reporting
- Email notifications
- AWS deployment

---

## Author

Deepak Kumar Jha
Analyst II Software Engineering
