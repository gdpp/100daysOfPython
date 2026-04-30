logs = [
    "INFO: User login successful",
    "ERROR: Database connection failed",
    "WARNING: Disk space low",
    "INFO: Product created",
    "ERROR: Invalid token",
    "INFO: User logout",
]


def _split_log(log):
    if len(log.strip()) == 0:
        return

    return log.split(":")


def validate_logs(logs):
    report = {"total": 0, "info": 0, "warn": 0, "error": 0, "errors": []}

    report["total"] = len(logs)

    for log in logs:
        sp_log = _split_log(log)

        if sp_log is None:
            continue

        if sp_log[0] == "INFO":
            report["info"] = report["info"] + 1
        elif sp_log[0] == "WARNING":
            report["warn"] = report["warn"] + 1
        else:
            report["error"] = report["error"] + 1

        report["errors"].append(sp_log[1])

    return report


if __name__ == "__main__":
    report_data = validate_logs(logs)
    print(report_data)
