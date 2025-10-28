# AI Foundry Agents + Logic Apps Integration

This project creates an integration between Azure AI Foundry Agents and Azure Logic Apps to automatically trigger AI agent runs every 24 hours.

## Architecture

The solution consists of:

1. **AI Foundry Agent**: A conversational AI agent deployed in Azure AI Foundry
2. **Azure Logic App**: A workflow that triggers every 24 hours to create agent runs
3. **Integration Scripts**: Python scripts to deploy and manage the components

## Files Structure

- `FoundryAgents.py`: Creates and manages AI Foundry agents
- `LogicApps.py`: Deploys Azure Logic Apps with workflow definitions
- `deploy_integration.py`: Main integration script that ties everything together
- `modules-standard/logicapp-definition.json`: Logic App workflow definition with 24-hour recurrence trigger
- `modules-standard/logic-app.bicep`: Bicep template for Logic App deployment

## Features

### Scheduled Agent Runs
- **Trigger**: Recurrence trigger set to run every 24 hours
- **Action**: Creates a new AI Foundry agent run via HTTP API calls
- **Monitoring**: Includes a follow-up action to check run status

### Agent Configuration
- **Instructions**: The agent is configured to perform scheduled analysis and monitoring
- **Metadata**: Each run includes timestamp and trigger source information
- **Flexibility**: Agent instructions can be customized for specific use cases

## Setup Instructions

### Prerequisites

1. Azure subscription with the following services enabled:
   - Azure AI Foundry
   - Azure Logic Apps
   - Azure Resource Manager

2. Required permissions:
   - Contributor access to resource group
   - AI Foundry workspace access
   - Logic Apps management permissions

### Environment Variables

Set the following environment variables before running:

```bash
# Azure subscription and resource details
SUBSCRIPTION_ID=your-subscription-id
GROUP_NAME=your-resource-group-name
WORKFLOW_NAME=your-logic-app-name
LOCATION=your-azure-region

# AI Foundry configuration
PROJECT_ENDPOINT=https://your-ai-foundry-endpoint
MODEL_DEPLOYMENT_NAME=your-model-deployment-name
FOUNDRY_API_KEY=your-foundry-api-key
```

### Deployment

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Deploy the complete integration**:
   ```bash
   python deploy_integration.py
   ```

   This will:
   - Create an AI Foundry agent
   - Deploy the Logic App with 24-hour recurrence trigger
   - Configure all necessary parameters and connections

3. **Deploy components separately** (optional):
   ```bash
   # Create agent only
   python FoundryAgents.py
   
   # Deploy Logic App only (after setting AGENT_ID environment variable)
   python LogicApps.py
   ```

## Logic App Workflow Details

### Trigger
- **Type**: Recurrence
- **Frequency**: Daily (every 24 hours)
- **Start Time**: Configurable (defaults to deployment time)

### Actions

1. **CreateFoundryAgentRun**: 
   - Makes HTTP POST request to AI Foundry API
   - Creates a new agent run with scheduled instructions
   - Includes metadata about the trigger source and timestamp

2. **GetRunStatus**:
   - Makes HTTP GET request to check run status
   - Runs after successful agent run creation
   - Provides monitoring and logging capabilities

### Parameters
- `foundryEndpoint`: AI Foundry API endpoint
- `foundryApiKey`: Authentication key for AI Foundry (secure parameter)
- `agentId`: ID of the AI agent to run

## Customization

### Agent Instructions
Modify the `instructions` parameter in `FoundryAgents.py` to customize what the agent does during scheduled runs:

```python
instructions=(
    "Your custom instructions for the scheduled agent runs. "
    "This could include specific analysis tasks, monitoring duties, "
    "or any other automated activities you want performed daily."
)
```

### Schedule Frequency
To change the trigger frequency, modify the `recurrence` section in `modules-standard/logicapp-definition.json`:

```json
"recurrence": {
    "frequency": "Hour",  // or "Day", "Week", "Month"
    "interval": 12        // Run every 12 hours instead of 24
}
```

### Additional Actions
Add more actions to the Logic App workflow by extending the `actions` section in the JSON definition. Examples:
- Send email notifications
- Log to Azure Monitor
- Trigger other workflows
- Store results in databases

## Monitoring and Troubleshooting

### Logic App Monitoring
- View run history in Azure Portal
- Check trigger and action execution details
- Monitor for failures and performance issues

### Agent Run Monitoring
- Use AI Foundry studio to view agent conversations
- Check run logs and outputs
- Monitor API usage and quotas

### Common Issues
1. **Authentication failures**: Verify API keys and permissions
2. **Agent not found**: Check agent ID configuration
3. **Trigger not firing**: Verify recurrence settings and Logic App status

## Security Considerations

- API keys are stored as secure parameters in Logic Apps
- Use Azure Key Vault for enhanced secret management
- Implement proper RBAC for resource access
- Monitor API usage and implement rate limiting if needed

## Cost Optimization

- Logic Apps pricing is based on trigger and action executions
- AI Foundry pricing depends on model usage and API calls
- Consider using consumption-based pricing for infrequent runs
- Monitor usage patterns and optimize accordingly