# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import os
import subprocess
import sys
from dotenv import load_dotenv
load_dotenv()


def main():
    """Deploy the complete integration by running both Python scripts."""

    # Step 1: Run FoundryAgents.py
    print("Step 1: Running FoundryAgents.py...")
    try:
        result = subprocess.run(
            [sys.executable, "FoundryAgents.py"],
            check=True, capture_output=True, text=True
        )
        print("FoundryAgents.py output:")
        print(result.stdout)
        if result.stderr:
            print("FoundryAgents.py stderr:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error running FoundryAgents.py: {e}")
        print(f"Return code: {e.returncode}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        return

    # Step 2: Run LogicApps.py
    print("\nStep 2: Running LogicApps.py...")
    try:
        result = subprocess.run(
            [sys.executable, "LogicApps.py"],
            check=True, capture_output=True, text=True
        )
        print("LogicApps.py output:")
        print(result.stdout)
        if result.stderr:
            print("LogicApps.py stderr:")
            print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error running LogicApps.py: {e}")
        print(f"Return code: {e.returncode}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        return

    print("\nIntegration deployment completed!")


if __name__ == "__main__":
    # Verify required environment variables
    required_vars = [
        "SUBSCRIPTION_ID", "GROUP_NAME", "WORKFLOW_NAME", "LOCATION",
        "PROJECT_ENDPOINT", "MODEL_DEPLOYMENT_NAME", "FOUNDRY_API_KEY"
    ]

    missing_vars = [var for var in required_vars if not os.environ.get(var)]

    if missing_vars:
        print("Error: Missing required environment variables:")
        for var in missing_vars:
            print(f"  - {var}")
        print("\nPlease set these environment variables before running.")
        exit(1)

    main()
