# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import os
from azure.ai.agents import AgentsClient
from azure.identity import DefaultAzureCredential


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
        print(f"Created agent, agent ID: {agent.id}")
        return agent.id


def create_agent_run(agent_id, instructions=None):
    """Create a new run for the specified agent."""
    agents_client = AgentsClient(
        endpoint=os.environ["PROJECT_ENDPOINT"],
        credential=DefaultAzureCredential(),
    )

    with agents_client:
        if instructions is None:
            instructions = (
                "Perform your scheduled analysis and provide a summary "
                "of current system status and any recommendations."
            )

        run = agents_client.create_run(
            agent_id=agent_id,
            instructions=instructions
        )
        print(f"Created agent run, run ID: {run.id}")
        return run.id


if __name__ == "__main__":
    # Create the agent and display the ID for Logic App configuration
    agent_id = create_foundry_agent()
    print("Agent created successfully.")
    print(f"Use this ID in your Logic App: {agent_id}")
