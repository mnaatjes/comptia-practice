---
title: "Setting Up Docker Testing Environments"
tags: ["CompTIA", "A+", "Docker", "Linux", "Windows", "command-line", "infrastructure"]
created_at: "2026-07-17"
last_updated_at: "2026-07-17"
---

## Replicating the Command Line Environments

Instead of dual-booting or configuring complex desktop environments, you can pull official base images to learn standard navigation, permissions, and file systems.

* **Linux Terminal Practice:** Spin up an interactive Ubuntu or Alpine container to safely master `chmod`, `chown`, `ps`, `kill`, `grep`, and basic network utilities like `ifconfig` or `ip`.
* **Windows Command Line:** You can pull the official Microsoft Windows Insider or .NET Core SDK nano-server images to practice the Windows command prompt (`dir`, `ipconfig`, `netstat`, `sfc /scannow`, `chkdsk`) directly in an isolated command-line container.

## Recommended Directory Structure

To support multiple Docker containers for different services, the repository should be structured to isolate each lab environment:

```text
/
├── docs/
│   └── how-to/
│       └── setup_docker_environments.md
├── labs/
│   ├── linux-terminal/
│   │   ├── Dockerfile (optional)
│   │   └── docker-compose.yml
│   └── windows-cli/
│       ├── Dockerfile (optional)
│       └── docker-compose.yml
└── GEMINI.md
```

## Workflows

### 1. Linux Environment (Ubuntu)

To spin up a basic Ubuntu testing container, create `labs/linux-terminal/docker-compose.yml`:

```yaml
version: '3.8'
services:
  ubuntu-lab:
    image: ubuntu:latest
    container_name: comptia-ubuntu-lab
    stdin_open: true # Allows interaction
    tty: true        # Allocates a pseudo-TTY
    command: /bin/bash
```

**Run the container interactively:**
```bash
docker-compose -f labs/linux-terminal/docker-compose.yml up -d
docker exec -it comptia-ubuntu-lab bash
```

### 2. Windows Environment (Server Core / Nano Server)

*Note: Running Windows containers natively requires a Windows host with Docker Desktop configured to run Windows containers.*

To spin up a basic Windows command-line environment, create `labs/windows-cli/docker-compose.yml`:

```yaml
version: '3.8'
services:
  windows-lab:
    image: mcr.microsoft.com/windows/servercore:ltsc2022
    container_name: comptia-windows-lab
    stdin_open: true
    tty: true
    command: cmd.exe
```

**Run the container interactively:**
```bash
docker-compose -f labs/windows-cli/docker-compose.yml up -d
docker exec -it comptia-windows-lab cmd
```
