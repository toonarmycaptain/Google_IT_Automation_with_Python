#!/usr/bin/env python3
"""Computer health checker"""
import shutil

import psutil

def check_disk_usage(disk: str) -> bool:
    du = shutil.disk_usage(disk)
    free = du.free /du.total * 100
    return free > 20


def check_cpu_usage() -> bool:
    usage = psutil.cpu_percent(1)
    return usage < 75

if __name__ == '__main__':
    if not check_disk_usage('/') or not check_cpu_usage():
        print("ERROR!")
    else:
        print("Everything is OK!")
