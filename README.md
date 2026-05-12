# astrbot_sandbox_shipyard_neo

<div align="center">

English ｜ <a href="./README_cn.md">简体中文</a>

</div>

`astrbot_sandbox_shipyard_neo` is the Shipyard Neo sandbox driver plugin for AstrBot, and the recommended remote sandbox option. It targets Bay / Shipyard Neo deployments and adds browser automation plus Neo Skill lifecycle tools on top of shell, Python, and file operations.

## Key Features

1. 🛡️ Provides the `shipyard_neo` sandbox driver for AstrBot.
2. 💻 Supports shell, Python, file operations, and browser capabilities.
3. 🌐 Registers browser automation tools automatically.
4. 🧩 Registers Neo Skill lifecycle tools automatically.
5. 📦 Syncs local AstrBot Skills when the sandbox boots.
6. 🔑 Supports automatic Bay credential discovery from `credentials.json`.

## Quick Start

### Install the Plugin

Clone the plugin into AstrBot's plugin directory:

```bash
git clone https://github.com/zouyonghe/astrbot_sandbox_shipyard_neo.git data/plugins/astrbot_sandbox_shipyard_neo
```

Then restart AstrBot, or reload plugins from the plugin management page.

### Enable the Shipyard Neo Sandbox Driver

In the AstrBot dashboard, enable sandbox mode and select the `shipyard_neo` driver.

Configuration path:

- `provider_settings.computer_use_runtime`: `sandbox`
- `provider_settings.sandbox.booter`: `shipyard_neo`

## Configuration

| Key | Description |
| --- | --- |
| `shipyard_neo_endpoint` | Bay / Shipyard Neo API endpoint. Defaults to `http://127.0.0.1:8114`. Use a service name when AstrBot and Bay share a Docker network. |
| `shipyard_neo_access_token` | Bay API key. If empty, local auto-start generates one and external endpoints try auto-discovery. |
| `shipyard_neo_profile` | Sandbox profile. Keep `python-default` or leave it empty to let Bay auto-select the best profile, or fill in a profile id returned by Bay. |
| `shipyard_neo_ttl` | Sandbox TTL in seconds. |

If AstrBot and Bay run in the same Docker Compose network, set `shipyard_neo_endpoint` to the Bay service name and make sure AstrBot can reach that network.

Credential auto-discovery checks:

- `$BAY_DATA_DIR/credentials.json`
- `./credentials.json`

## Best For

- Use this plugin when you need browser automation inside the sandbox.
- It also exposes Neo Skill lifecycle tools such as payload, candidate, release, rollback, and sync operations.
- Browser capability depends on the selected profile. A profile without browser support will not provide full browser behavior even though the plugin is installed.
- Managed sandbox cleanup uses `delete_sandbox=True` during teardown.

## Requirements and Limitations

- AstrBot must support external sandbox driver plugins.
- The Python dependency from `requirements.txt`: `shipyard-neo-sdk`.
- A working Bay / Shipyard Neo service is required.
- A valid Bay API key is required unless it can be auto-discovered.
- This plugin depends on a working Bay / Shipyard Neo deployment.
- Browser behavior depends on the selected profile and upstream runtime support.
- If you only need shell or file operations, classic Shipyard or BoxLite is usually lighter.

## Troubleshooting

- If local auto-start does not produce a working endpoint, make sure Docker is available and the default endpoint is still `http://127.0.0.1:8114`.
- If profile selection is unclear, keep `shipyard_neo_profile` as `python-default` and let Bay choose the best available profile.
