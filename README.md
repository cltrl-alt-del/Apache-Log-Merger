# Apache-Log-Merger
Python script to merge multiple Apache2 access log files into a single file, sorting the entries by date and time in either ascending or descending order.
✅ Covers all log file extensions (access.log, access.log.2, ..., access.log.13).
✅ Sorts files correctly (so access.log is read first, then access.log.2, etc.).
✅ Efficient log processing (merges, sorts, and writes logs correctly).
✅ User input for flexibility (log directory, output file, sorting order).


Features:
User Input: Asks for log directory and output file location.
Sorting Order: Allows user to choose ascending or descending order.
Validation: Ensures sorting order input is correct.
Efficiency: Reads, sorts, and writes efficiently.

Steps:
Read all log files.
Extract timestamp and sort entries.
Write sorted logs to a new file.


Can be used to multiple merger error.log files
