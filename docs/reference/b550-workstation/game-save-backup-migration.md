---
title: "Game Save Backup and Migration Strategy"
tags: ["backup", "gaming", "steam", "migration", "linux", "proton"]
created_at: "2026-08-09"
last_updated_at: "2026-08-09"
---

# Game Save Backup and Migration Strategy

This reference outlines the comprehensive backup procedure for game saves and credentials across a multi-drive Windows setup prior to a total data wipe, preparing for a Linux Mint (Proton) gaming migration.

## Procedure 1: Verify Steam Cloud Sync
The vast majority of Steam titles automatically synchronize saves and account credentials to Steam Cloud, rendering manual backups redundant for those specific titles.

1. Open Steam on your current Windows installation.
2. Navigate to your **Library**, click the **List View** icon, and ensure the **Cloud Status** column is visible.
3. Confirm that all critical games show the "Up to date" cloud icon.
4. *Alternative:* Log into `store.steampowered.com/account/remotestorage` via a web browser to manually verify the physical presence of your cloud save files on Valve's servers.

## Procedure 2: Extract Local Save Data (Non-Cloud Games)
For games that do not support Steam Cloud, manually back up the following directories from your OS drive to an external USB drive. Game installation files on secondary drives do not need to be backed up; only the lightweight save files are required.

1. `C:\Users\[Username]\Documents\My Games\` (Common location for Bethesda and EA titles).
2. `C:\Users\[Username]\Documents\` (Look for folders bearing the publisher or game name).
3. `C:\Users\[Username]\Saved Games\` (Standard Windows save repository).
4. `C:\Users\[Username]\AppData\Local\`, `AppData\LocalLow\`, and `AppData\Roaming\` (Requires enabling "Show Hidden Files" in Windows Explorer. Look for developer names like *CD Projekt Red* or *Larian Studios*).
5. *Optional Automation:* Download and run **GameSave Manager** (a free utility) to automatically scan, package, and export all detected local save files into a single backup archive.

## Procedure 3: Credential Backup
1. If you use a third-party launcher integrated with Steam (e.g., EA App, Ubisoft Connect, Rockstar Games Launcher), ensure those account credentials are saved in your external password manager.
2. Export any saved passwords from your web browser to a CSV file or password manager vault before wiping the OS drive.

## Procedure 4: Assess Linux Mint (Proton) Compatibility
Transitioning to Linux Mint means games will run via the Proton compatibility layer.

1. Navigate to **ProtonDB.com** on any device.
2. Link your Steam account or manually search your primary multiplayer and single-player games.
3. Review the tier rating (Platinum, Gold, Silver, Bronze, Borked):
   * **Platinum/Gold:** Will run flawlessly on Linux Mint via Steam out-of-the-box.
   * **Borked:** Typically multiplayer games with kernel-level anti-cheat (e.g., Destiny 2, Valorant). These will *not* run on Linux and must be relegated to your isolated Windows 11 dual-boot drive.
