def file_error_tester() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt") as file:
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    print()
    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("/bin/zsh", "w") as file:
            print("STATUS: Normal operations resumed")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    print()
    try:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt") as file:
            print(f"SUCCESS: Archive recovered - ``{file.read()}''")
        print("STATUS: Normal operations resumed")
    except Exception as err:
        print(err)
        print("STATUS: Crisis handled, security maintained")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    file_error_tester()
