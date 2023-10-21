#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""

import sys
from typing import List, Dict
import ipaddress

files_size: int = 0
status_codes: List[int] = [200, 301, 400, 401, 403, 404, 405, 500]
codes_count: Dict[int, int] = {}
counter: int = 0


def print_info():
    """Printing log info to the stdout"""
    print("File size: {}".format(files_size))
    for code in status_codes:
        if codes_count.get(code, False):
            print("{}: {}".format(code, codes_count[code]))


def parseInt(num: str) -> int:
    """Converts a string to integer is available."""
    result = 0
    try:
        result = int(num)
        return result
    except ValueError:
        return result


if __name__ == "__main__":
    try:
        for log_line in sys.stdin:
            splitted: List[str] = log_line.split()
            if len(splitted) > 4:
                status: int = parseInt(splitted[-2])
                size: int = parseInt(splitted[-1])
                files_size += size
                if status in status_codes:
                    codes_count[status] = codes_count.get(status, 0) + 1
                counter += 1
            if counter % 10 == 0:
                print_info()
    except Exception:
        pass
    finally:
        print_info()
