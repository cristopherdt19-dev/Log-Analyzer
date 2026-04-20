"""
Log Analyzer Script

This script reads a log file and analyzes the number of
errors, warnings, and informational messages.

"""

from datetime import datetime


# Analyzes a log file and displays a summary of detected message types
def analyze_log(file_path):
    file_path = file_path.strip()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: file not found.")
        return

    error_count = 0
    warning_count = 0
    info_count = 0
    unmatched_count = 0

    for line in lines:
        line_lower = line.lower()

        if "error" in line_lower:
            error_count += 1
        elif "warning" in line_lower:
            warning_count += 1
        elif "info" in line_lower:
            info_count += 1
        else:
            unmatched_count += 1

    total_lines = len(lines)

    print("\nLog Analysis Results:")
    print(f"Total lines analyzed: {total_lines}")
    print(f"Errors: {error_count}")
    print(f"Warnings: {warning_count}")
    print(f"Info: {info_count}")
    print(f"Unmatched lines: {unmatched_count}")

    save_report = input("\nDo you want to save this analysis to a report file? (yes/no): ").strip().lower()

    if save_report == "yes":
        save_analysis_report(
            file_path,
            total_lines,
            error_count,
            warning_count,
            info_count,
            unmatched_count
        )


# Saves the analysis summary to a text report file
def save_analysis_report(file_path, total_lines, error_count, warning_count, info_count, unmatched_count):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"log_analysis_report_{timestamp}.txt"

    with open(report_name, "w", encoding="utf-8") as report_file:
        report_file.write("Log Analysis Report\n")
        report_file.write("===================\n")
        report_file.write(f"Source file: {file_path}\n")
        report_file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        report_file.write(f"Total lines analyzed: {total_lines}\n")
        report_file.write(f"Errors: {error_count}\n")
        report_file.write(f"Warnings: {warning_count}\n")
        report_file.write(f"Info: {info_count}\n")
        report_file.write(f"Unmatched lines: {unmatched_count}\n")

    print(f"Report saved successfully as: {report_name}")


while True:
    file_path = input("\nEnter log file path (or type 'exit' to quit): ").strip()

    if file_path.lower() == "exit":
        print("Exiting program...")
        break

    analyze_log(file_path)