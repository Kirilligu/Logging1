import re
def check_log(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    prev_timestamp = None
    for log in logs:
        match = re.search(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', log)
        if match:
            timestamp = match.group(0)
            if prev_timestamp and timestamp < prev_timestamp:
                return False
            prev_timestamp = timestamp

    return True


if __name__ == "__main__":
    publisher_log_file = "publisher.log"
    subscriber_log_file = "subscriber.log"
    user_service_log_file = "user_service.log"
    publisher_logs_ordered = check_log(publisher_log_file)
    subscriber_logs_ordered = check_log(subscriber_log_file)
    user_service_logs_ordered = check_log(user_service_log_file)
    print(f"Publisher logs ordered: {publisher_logs_ordered}")
    print(f"Subscriber logs ordered: {subscriber_logs_ordered}")
    print(f"User-Service logs ordered: {user_service_logs_ordered}")
