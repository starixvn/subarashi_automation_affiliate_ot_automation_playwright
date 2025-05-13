# Secrets Directory

This directory is for storing secret files that should not be committed to Git.

## Contents

This directory should contain sensitive configuration files such as:

- `client_secret.json`: Google API credentials
- Database credentials
- API keys
- Private keys
- Certificates
- Any other secrets or sensitive information

## Usage

To use secrets in your code, place them in this directory and reference them using relative paths:

```python
import json
from pathlib import Path

# Load Google client secret
client_secret_path = Path(__file__).parent.parent / 'config' / 'secrets' / 'client_secret.json'
with open(client_secret_path) as f:
    client_secret = json.load(f)
```

## Security

This directory is included in `.gitignore` to prevent accidentally committing secrets.

For local development, you should manually add the required secret files to this directory.

For CI/CD environments, secrets should be injected using environment variables or secure secret management services. 