def create_new_discovery() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    try:
        print("\nInitializing new storage unit: new_discovery.txt")
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...")
        print("\nInscribing preservation data...")
        print("[ENTRY 001] New quantum algorithm discovered\n\
[ENTRY 002] Efficiency increased by 347%\n\
[ENTRY 003] Archived by Data Archivist trainee")
        file.write("[ENTRY 001] New quantum algorithm discovered\n\
[ENTRY 002] Efficiency increased by 347%\n\
[ENTRY 003] Archived by Data Archivist trainee")
        file.close()
        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except Exception as err:
        print(err)


if __name__ == "__main__":
    create_new_discovery()
