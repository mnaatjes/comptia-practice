---
title: "B550 Workstation Documentation Index"
tags: ["readme", "index", "b550", "dual-boot", "rebuild"]
created_at: "2026-08-09"
last_updated_at: "2026-08-09"
---

# B550 Workstation Documentation Index

This directory contains the reference documentation, diagnostic reports, and step-by-step procedures for the hardware repair and dual-boot rebuild of the B550 Workstation. 

## Order of Execution

When the replacement Corsair PSU is installed and the system is ready to be rebuilt, execute the procedures in the following chronological order:

### Phase 1: Context & Pre-Wipe Preparation
Review the hardware status and secure all necessary local data before executing the system wipe.
1. **[Hardware Status & Diagnostics](./troubleshooting-status.md):** Review the current hardware state and the established diagnostic baseline.
2. **[RMA Report Context](./corsair-rma-report.md):** Details the catastrophic failure behavior that necessitated the PSU replacement.
3. **[Game Save & Credential Backup](./game-save-backup-migration.md):** Execute these procedures to secure Steam cloud syncs, extract local save data, and verify Proton compatibility for the Linux migration.

### Phase 2: Windows Reinstallation
Establish the primary Windows environment on the isolated M.2 SATA drive.
4. **[Windows 11 Reinstallation Guide](./windows-os-reinstallation-guide.md):** Follow these steps to configure the BIOS (CSM, Secure Boot, AHCI), extract hardware IDs, and perform a clean Windows 11 installation exclusively on the SATA M.2 drive.

### Phase 3: Linux Dual-Boot Deployment
Deploy the primary daily-driver OS on the high-performance NVMe drive.
5. **[Dual-Boot Implementation Plan](./dual-boot-implementation-plan.md):** Execute the Linux Mint installation on the 2TB NVMe drive, establishing the physical segregation between the Windows and Linux environments.

### Phase 4: Post-Install Infrastructure
Configure local services and credential management on the new Linux Mint host.
6. **[Vaultwarden Implementation Guide](./vaultwarden-implementation-guide.md):** Deploy a self-hosted Vaultwarden Docker container for local credential management and optionally integrate the vault with Ansible.
