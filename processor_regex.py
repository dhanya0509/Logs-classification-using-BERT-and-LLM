import re
def classify_with_regex(log_message):
    regex_patterns = {
        r"(?i)User User\d+ logged (in|out).": "User Action",
        r"(?i)Backup (started|ended) at .*": "System Notification",
        r"(?i)Backup completed successfully.": "System Notification",
        r"(?i)System updated to version .*": "System Notification",
        r"(?i)File .* uploaded successfully by user .*": "System Notification",
        r"(?i)Disk cleanup completed successfully.": "System Notification",
        r"(?i)System reboot initiated by user .*": "System Notification",
        r"(?i)Account with ID .* created by .*": "User Action"
    }
    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
    return None

if __name__ == "__main__":
    print(classify_with_regex("Backup completed successfully."))
    print(classify_with_regex("Account with ID 1234 created by User1."))
    print(classify_with_regex("Hey Bro, chill ya!"))