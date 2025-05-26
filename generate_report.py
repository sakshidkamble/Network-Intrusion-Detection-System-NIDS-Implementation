import os

def generate_report(analysis_results):
    report_file = "NIDS_report.txt"
    with open(report_file, "w") as f:
        f.write("Network Intrusion Detection System Report\n")
        f.write("="*70 + "\n\n")
        f.write("Analysis Results:\n\n")
        for result in analysis_results:
            f.write(result + "\n")

    print(f"Report generated successfully! You can view it in {os.path.abspath(report_file)}")
    return os.path.abspath(report_file)
