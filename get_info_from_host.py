#!/usr/bin/env python3

import time
import os

def main():
    keep_running = "yes"
    
    while True:
        clear_screen()
        time.sleep(2)
        print("Sharing memory and disk usage, I/O and network routes")
        check_memory_usage()
        check_disk_space_usage()
        check_io_disk()
        check_network_routes()
        print("Press CRTL+D to stop")
        time.sleep(20)

def clear_screen():
    os.system('clear')
def check_memory_usage():
    print(os.system('free -m'))
    
def check_disk_space_usage():
    print(os.system('df -h'))

def check_io_disk():
    print(os.system('iostat'))
    
def check_network_routes(): 
    print(os.system('route -n'))

if __name__ == "__main__":
    main() 

