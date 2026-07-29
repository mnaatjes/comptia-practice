---
title: "How to Install Linux Mint on the Dell Optiplex (from a Debian Host)"
tags: ["linux", "mint", "installation", "optiplex", "debian", "usb"]
created_at: "2026-07-29"
last_updated_at: "2026-07-29"
---

# How to Install Linux Mint on the Dell Optiplex

This guide covers how to wipe the existing Proxmox installation on the Dell Optiplex 5050 and replace it with Linux Mint (Cinnamon Edition). Because the installation media is being created from a Debian 13 laptop, Windows-only tools like Rufus cannot be used.

## Phase 1: Download the Operating System
1. On your Debian Surface laptop, open a web browser.
2. Navigate to the official Linux Mint website (linuxmint.com).
3. Click **Download** and select the **Cinnamon Edition** (this is the flagship, Windows-style interface).
4. Choose a download mirror close to your location and save the `.iso` file to your `Downloads` folder.

## Phase 2: Create the Bootable USB (Debian Host)
Because Rufus is not available on Linux, you have two primary methods to flash the ISO to your 8GB+ USB drive.

### Method A: BalenaEtcher (GUI - Recommended)
1. Navigate to `etcher.balena.io` and download the Linux `.AppImage` file.
2. Once downloaded, open your terminal and grant it execution permissions:
   `chmod +x ~/Downloads/balenaEtcher-*.AppImage`
3. Run the application:
   `~/Downloads/balenaEtcher-*.AppImage`
4. Insert your USB drive (Warning: All data will be erased).
5. In Etcher, click **Flash from file** and select the Linux Mint `.iso`.
6. Click **Select target** and choose your USB drive.
7. Click **Flash!** and enter your `sudo` password when prompted.

### Method B: The `dd` Terminal Command (Advanced)
If you prefer the raw Linux terminal, you can flash the drive natively.
1. Insert the USB drive.
2. Run `lsblk` in the terminal to identify your USB drive's designation (e.g., `/dev/sdb` or `/dev/sdc`). **Verify this carefully.**
3. Run the flash command (Replace `sdX` with your USB drive letter):
   `sudo dd if=~/Downloads/linuxmint-21.3-cinnamon-64bit.iso of=/dev/sdX bs=4M status=progress`
4. Run `sync` to ensure all data is written, then remove the USB.

## Phase 3: Hardware Installation on the Optiplex
1. Power down the Dell Optiplex 5050.
2. Insert the newly flashed Linux Mint USB into a rear USB port.
3. Power on the Optiplex and immediately begin tapping **F12** to enter the Dell One-Time Boot Menu.
4. Select your USB flash drive from the UEFI boot list.

## Phase 4: OS Installation
1. The USB will boot into a "Live Environment." This is a fully functioning preview of the OS running off the USB.
2. Double-click the **Install Linux Mint** CD icon on the desktop.
3. Follow the setup wizard (Language, Keyboard Layout).
4. **Network:** Connect to Wi-Fi or ensure Ethernet is plugged in so third-party drivers can download.
5. **Multimedia Codecs:** Check the box to "Install multimedia codecs" (crucial for video playback).
6. **Installation Type:** Select **Erase disk and install Linux Mint**. (This will permanently delete the old Proxmox hypervisor).
7. Create your username and password.
8. Click **Install Now**. When it finishes, reboot the machine and remove the USB drive.
