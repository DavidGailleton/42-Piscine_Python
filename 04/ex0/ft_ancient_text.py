def read_ancient_text() -> None:
    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        vault = open("ancient_fragment.txt", "r")
        print("Connection establish...")
        print("\nRECOVERED DATA:")
        print(vault.read())
        vault.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    read_ancient_text()
