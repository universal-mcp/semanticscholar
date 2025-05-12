
from universal_mcp.servers import SingleMCPServer
from universal_mcp.integrations import ApiKeyIntegration
from universal_mcp.stores import EnvironmentStore

from universal_mcp_semanticscholar.app import SemanticscholarApp

env_store = EnvironmentStore()
integration_instance = ApiKeyIntegration(name="SEMANTICSCHOLAR_API_KEY", store=env_store)
app_instance = SemanticscholarApp(integration=integration_instance)

mcp = SingleMCPServer(
    app_instance=app_instance,
)

if __name__ == "__main__":
    mcp.run()


