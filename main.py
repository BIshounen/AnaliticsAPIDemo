from integration import Integration
import config
import json

INTEGRATION_MANIFEST_PATH = "manifests/integration_manifest.json"
ENGINE_MANIFEST_PATH = "manifests/engine_manifest.json"
AGENT_MANIFEST_PATH = "manifests/agent_manifest.json"
CREDENTIALS_PATH = ".credentials"

if __name__ == "__main__":
  with (open(INTEGRATION_MANIFEST_PATH, 'r') as f_i,
        open(ENGINE_MANIFEST_PATH, 'r') as f_e,
        open(AGENT_MANIFEST_PATH, 'r') as f_a):
    integration_manifest = json.load(f_i)
    engine_manifest = json.load(f_e)
    agent_manifest = json.load(f_a)

  integration = Integration(server_url=config.server_url,
                            integration_manifest=integration_manifest,
                            engine_manifest=engine_manifest,
                            device_agent_manifest=agent_manifest,
                            credentials_path=CREDENTIALS_PATH,
                            auth_refresh=10
                            )
