import sys


def communication_system() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    archivist_id = input()
    sys.stdout.write("Input Stream active. Enter status report: ")
    status_report = input()
    sys.stdout.write(
        f"\n[STANDARD] Archive status from {archivist_id}: {status_report}\n"
    )
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
    )
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    communication_system()
