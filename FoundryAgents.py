# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import os
from pathlib import Path
from azure.ai.agents import AgentsClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv, set_key
load_dotenv()


def create_foundry_agent():
    """Create an AI Foundry Agent for Logic App integration."""
    agents_client = AgentsClient(
        endpoint=os.environ["PROJECT_ENDPOINT"],
        credential=DefaultAzureCredential(),
    )

    with agents_client:
        agent = agents_client.create_agent(
            model=os.environ["MODEL_DEPLOYMENT_NAME"],
            name="LogicApp-FoundryAgent",
            instructions=(
                "You are a helpful AI agent that runs on a 24-hour schedule "
                "via Azure Logic Apps. Your role is to perform scheduled "
                "analysis, monitoring, and provide insights on system status. "
                "When triggered, analyze current conditions and provide "
                "actionable recommendations."
            ),
        )

        thread = agents_client.threads.create()
        print(f"Created thread, thread ID: {thread.id}")
        print(f"Created agent, agent ID: {agent.id}")
        return agent.id, thread.id


if __name__ == "__main__":
    # Create the agent and add ID to .env for Logic App configuration
    agent_id, thread_id = create_foundry_agent()
    print("Agent created successfully.")

    env_path = Path(".") / ".env"
    env_path.touch(exist_ok=True)

    set_key(env_path, "AGENT_ID", f"{agent_id}")
    set_key(env_path, "THREAD_ID", f"{thread_id}")
    print(f"Agent ID has been added to env file: {agent_id}")
    print(f"Thread ID has been added to env file: {thread_id}")
