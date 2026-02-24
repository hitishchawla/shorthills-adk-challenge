from agents import CoordinatorAgent
import json


def main():
    startup_name = input("Enter startup name: ")
    coordinator = CoordinatorAgent()
    report = coordinator.run_analysis(startup_name)

    print("\nFINAL MULTI-AGENT REPORT\n")
    print(json.dumps(report, indent=4))


if __name__ == "__main__":
    main()