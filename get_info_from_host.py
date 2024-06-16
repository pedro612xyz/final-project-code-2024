#!/usr/bin/env python3


def main():
    keep_running = input("Enter yes to keep monitoring the system or no to stop it: ")
    
    while keep_running == "yes":
        check_memory_usage()
        check_disk_space_usage()
        check_io_disk()
        check_network_routes()
        keep_running = input("Enter yes to keep monitoring the system or no to stop it: ")

def check_memory_usage():
    print("memory")
    
def check_disk_space_usage():
    print("disk")

def check_io_disk():
    print("io")
    
def check_network_routes():
    print("routes")

if __name__ == "__main__":
    main()  # Indented block here to call the main() function

