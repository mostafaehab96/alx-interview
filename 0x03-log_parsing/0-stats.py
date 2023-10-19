#!/usr/bin/python3


"""a script that reads stdin line by line and computes metrics"""
import re

pattern = (r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[\d{4}-\d{2}-\d{2} \d{'
           r'2}:\d{2}:\d{2}\.\d{6}\] "GET /projects/260 HTTP/1.1" \d{3} \d+')

files_size = 0
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
codes_count = {}
counter = 0


def print_info():
    """Printing log info to the stdout"""
    print("File size: {}".format(files_size))
    for code in status_codes:
        if codes_count.get(code, False):
            print("{}: {}".format(code, codes_count[code]))


while True:
    try:
        log_line = input()
        counter += 1
        if re.match(pattern, log_line):
            splitted = log_line.split()
            status = int(splitted[7])
            size = int(splitted[8])
            files_size += size
            if status in status_codes:
                codes_count[status] = codes_count.get(status, 0) + 1
        if counter % 10 == 0:
            print_info()
    except KeyboardInterrupt:
        print_info()
