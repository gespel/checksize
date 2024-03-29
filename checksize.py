import os
import time

def get_size(start_path = '.'):
    num_files = 0
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            num_files += 1
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return (num_files, total_size)

def checkloop():
    while(1):
        num_files, size = get_size()
        print(f"{num_files} files -> {size/1024/1024} MB")
        time.sleep(1)
