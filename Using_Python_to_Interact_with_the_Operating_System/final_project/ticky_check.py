#!/usr/bin/env python3
import csv
import operator
import re

from collections import defaultdict

error_counts = defaultdict(int)  # {error_message: count}
per_user = {}  # {import reuser_name: {error_1: count, error_2: count}

# 1: status, 2: message, 3: ticket number 4: user
regex_draft = r"ticky: ([A-Z]*) (.*) (\[#\d{4}] )?\(([\w.]*)\)"  # Try to grab ticket number so not in error message.

#               1: status, 2: message, 3: user
regex = r"ticky: ([A-Z]*) (.*) \(([\w.]*)\)"
ticket_num_regex = r'(\[#\d{4}])'

with open('sample_syslog.log', 'r') as logfile:
    for log_entry in logfile:
        # Get desired data:
        re_search = re.search(regex, log_entry.strip())

        status, message, user_name = re_search.groups()
        # Strip ticket number:
        if re.search(ticket_num_regex, message):
            message = message[:-8]

        if user_name not in per_user:
            per_user[user_name] = {'INFO': 0, 'ERROR': 0}
        else:
            per_user[user_name][status] += 1

        error_counts[message] += 1

# Sort the dicts
sorted_error_counts = sorted(error_counts.items(), key=operator.itemgetter(1), reverse=True)
sorted_per_user_dicts = sorted(per_user.items())

sorted_per_user = [(user[0], user[1]['INFO'], user[1]["ERROR"]) for user in sorted_per_user_dicts]

# Add column headers:
sorted_error_counts_with_headers = [("Error", "Count")] + sorted_error_counts
sorted_per_user_with_headers = [("Username", "INFO", "ERROR")] + sorted_per_user

# print(f'{error_counts=},\n {per_user=}')
# print(f'{sorted_error_counts=},\n {sorted_per_user=}')
#
# print(f'{sorted_error_counts_with_headers=}')
# print(f'{sorted_per_user_with_headers=}')

# Write csv files:
with open('error_message.csv', mode='w') as error_message_file:
    error_message_writer = csv.writer(error_message_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for error_message in sorted_error_counts_with_headers:
        error_message_writer.writerow(error_message)

with open('user_statistics.csv', mode='w') as user_statistics_file:
    user_statistics_writer = csv.writer(user_statistics_file,
                                        delimiter=',')
    for user in sorted_per_user_with_headers:
        user_statistics_writer.writerow(user)
