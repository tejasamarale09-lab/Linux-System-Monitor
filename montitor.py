import os
import subprocess
import time

def clear_screen():
    os.system("clear")

def show_processes():
    try:
        print("\n--- Top Processes (by Memory) ---\n")
        subprocess.run("ps aux --sort=-%mem | head", shell=True)
    except Exception as e:
        print("Error showing processes:", e)
def kill_process():
    try:
        pid = input("Enter PID to kill: ")

        if not pid.isdigit():
            print("Invalid PID. Must be a number.")
            return

        confirm = input("Are you sure you want to kill this process? (y/n): ")
        if confirm.lower() != 'y':
            print("Cancelled.")
            return

        subprocess.run(["kill", pid])
        print("Process termination attempted.")

    except Exception as e:
        print("Error killing process:", e)

def show_memory():
    try:
        print("\n--- Memory Usage ---\n")
        subprocess.run(["free", "-h"])
    except Exception as e:
        print("Error showing memory:", e)

def show_cpu():
    try:
        print("\n--- CPU Usage ---\n")
        subprocess.run("top -bn1 | grep 'Cpu'", shell=True)
    except Exception as e:
        print("Error showing CPU:", e)

def auto_refresh():
    try:
        while True:
            clear_screen()
            print("=== AUTO REFRESH MODE (Ctrl+C to exit) ===\n")

            subprocess.run(["free", "-h"])
            subprocess.run("top -bn1 | grep 'Cpu'", shell=True)

            time.sleep(3)

    except KeyboardInterrupt:
        print("\nExited auto refresh mode.")
    except Exception as e:
        print("Error in auto refresh:", e)

def main():
    while True:
        clear_screen()
        print("===== Linux System Monitor =====")
        print("1. Show Running Processes")
        print("2. Kill Process")
        print("3. Show Memory Usage")
        print("4. Show CPU Usage")
        print("5. Auto Refresh Mode")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_processes()
        elif choice == "2":
            kill_process()
        elif choice == "3":
            show_memory()
        elif choice == "4":
            show_cpu()
        elif choice == "5":
            auto_refresh()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()



    
