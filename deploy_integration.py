# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import os
from FoundryAgents import create_foundry_agent
from LogicApps import main as deploy_logic_app


def main():
    """Deploy the complete integration: AI Foundry Agent + Logic App."""

    # Step 1: Create the AI Foundry Agent
    print("Step 1: Creating AI Foundry Agent...")
    agent_id = create_foundry_agent()

    # Step 2: Set the agent ID as environment variable for Logic App
    os.environ["AGENT_ID"] = agent_id
    print(f"Agent ID set: {agent_id}")

    # Step 3: Deploy the Logic App
    print("Step 2: Deploying Logic App with scheduled trigger...")
    deploy_logic_app()

    print("Integration deployment completed!")
    print("\nSummary:")
    print(f"- AI Foundry Agent ID: {agent_id}")
    print(f"- Logic App Name: {os.environ.get('WORKFLOW_NAME', 'N/A')}")
    print("- Schedule: Every 24 hours")
    print("- The Logic App will automatically create agent runs every day")


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
