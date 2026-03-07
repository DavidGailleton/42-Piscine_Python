from importlib.metadata import PackageNotFoundError, version
from numpy import ndarray
from pandas import pandas as pd
import matplotlib.pyplot as plt
from os import mkdir


def check_package(packages: dict[str, str]) -> bool:
    print("Checking dependencies:")
    imported = 0
    for package in packages:
        try:
            print(f"[\u001b[32mOK\u001b[0m] {package}\
 ({version(package)}) - {packages[package]} ready")
            imported += 1
        except PackageNotFoundError:
            print(f"[\u001b[31mKO\u001b[0m] {package} -\
 {packages[package]} not ready")
    return imported == len(packages)


def analyze(data: ndarray) -> None:
    print("Processing 1000 data points...")
    x = data[:, 0]
    y = data[:, 1].astype(float)
    plt.figure(figsize=(8, 8), dpi=1200)
    plt.plot(x, y)
    try:
        mkdir("matrix")
    except Exception:
        pass
    print("Generating visualization...\n")
    plt.savefig("matrix/_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix/_analysis.png}")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    if check_package(
        {
            "pandas": "Data manipulation",
            "numpy": "mathematics manipulation",
            "matplotlib": "Visualization",
        }
    ):
        try:
            print("\nAnalyzing Matrix data...")
            data = pd.read_csv("meteo.csv", parse_dates=["time"]).to_numpy()
            analyze(data)
        except FileNotFoundError:
            print("File not found")
        except Exception as err:
            print(err)
    else:
        print("\nPackages not installed")


if __name__ == "__main__":
    main()
