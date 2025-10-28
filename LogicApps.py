# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.logic import LogicManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.logic.models import Workflow

# - other dependence -
# - end -


def main():

    SUBSCRIPTION_ID = os.environ.get("SUBSCRIPTION_ID", None)
    GROUP_NAME = os.environ.get("GROUP_NAME", None)
    WORKFLOW_NAME = os.environ.get("WORKFLOW_NAME", None)
    location = os.environ.get("LOCATION", None)
    FOUNDRY_ENDPOINT = os.environ.get("PROJECT_ENDPOINT", None)
    FOUNDRY_API_KEY = os.environ.get("FOUNDRY_API_KEY", None)
    AGENT_ID = os.environ.get("AGENT_ID", None)

    # Create client
    resource_client = ResourceManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=SUBSCRIPTION_ID
    )
    logic_client = LogicManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=SUBSCRIPTION_ID
    )
    # - init depended client -
    # - end -

    # Create resource group
    resource_client.resource_groups.create_or_update(
        GROUP_NAME,
        {"location": location}
    )

    # Load the workflow definition from JSON file
    import json

    # Read the workflow definition from the JSON file
    with open('modules-standard/logicapp-definition.json', 'r') as f:
        workflow_definition = json.load(f)

    workflow = Workflow(
        location=location,
        definition=workflow_definition,
        parameters={
            "foundryEndpoint": {"value": FOUNDRY_ENDPOINT},
            "foundryApiKey": {"value": FOUNDRY_API_KEY},
            "agentId": {"value": AGENT_ID}
        }
    )

    logic_client.workflows.create_or_update(
        GROUP_NAME,
        WORKFLOW_NAME,
        workflow
    )

    print("Create logic:\n")

    logic_client.workflows.get(
        GROUP_NAME,
        WORKFLOW_NAME
    )
    print("Get logic:\n")


if __name__ == "__main__":

    main()
