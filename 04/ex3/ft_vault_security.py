def vault_security_system() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        print("Initiating secure vault access...")
        with open("classified_data.txt", "r") as source_file, open(
            "archive_data.txt", "w"
        ) as dest_file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(source_file.read())
            print("\nSECURE PRESERVATION:")
            dest_file.write("[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion")
    except Exception as err:
        print(err)
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    vault_security_system()
