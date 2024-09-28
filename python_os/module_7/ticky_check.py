import re 
import operator
import csv

error = {}
user = {}

with open("syslog.log", "r") as file:
    for line in file.readlines():
        try:
            result = re.search(r"(INFO|ERROR) (.*) \((\w+)\)", line)
            log_type = result[1]
            log_detail = result[2]
            username = result[3]
            if log_type == "ERROR":
                error[log_detail] = error.get(log_detail, 0) + 1
            if not username in user:
                user[username] = {
                    "INFO" : 0,
                    "ERROR" : 0
                }
            user[username][log_type] += 1
        except Exception as e:
            pass


sorted_error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)

error_data = [{"Error": key, "Count": value} for key, value in sorted_error]

sorted_user = sorted(user.items(), key=operator.itemgetter(0))

user_data = [{"Username": username, "INFO": stats["INFO"], "ERROR": stats["ERROR"]} for username, stats in sorted_user]

with open("error_message.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Error", "Count"])
    writer.writeheader()
    writer.writerows(error_data)

with open("user_statistics.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Username", "INFO", "ERROR"])
    writer.writeheader()
    writer.writerows(user_data)


# print(error)
# print(user)
        