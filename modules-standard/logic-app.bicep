param logicAppName string
param location string
param foundryEndpoint string
param agentId string
@secure()
param foundryApiKey string

resource logicApp 'Microsoft.Logic/workflows@2019-05-01' = {
  name: logicAppName
  location: location
  properties: {
    definition: loadJsonContent('logicapp-definition.json')
    parameters: {
      foundryEndpoint: { value: foundryEndpoint }
      foundryApiKey:   { value: foundryApiKey }
      agentId:         { value: agentId }
    }
  }
}
