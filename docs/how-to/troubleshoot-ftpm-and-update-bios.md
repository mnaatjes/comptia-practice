---
title: "Troubleshoot fTPM and Update BIOS"
tags: ["hardware", "troubleshooting", "bios", "ftpm", "gigabyte"]
created_at: "2026-07-29"
last_updated_at: "2026-07-29"
---

# Troubleshoot AMD fTPM and Update BIOS (GIGABYTE B550)

## Diagnostic
System experiences severe stuttering, audio glitching, or hard-crashes (black screens) under load, accompanied by TPM-WMI errors (Event ID 1040/1801) in the Windows Event Viewer.

## Theory
AMD Ryzen processors paired with AM4 motherboards (B550/X570) have a known microcode flaw involving the firmware Trusted Platform Module (fTPM). When Windows accesses encryption keys, the CPU-to-motherboard SPI flash communication hangs, causing system instability. Disabling fTPM isolates the issue; updating the BIOS permanently resolves it via an AGESA V2 microcode patch.

## Remediation 1: Disable fTPM (Diagnostic Workaround)
*Warning: Disabling fTPM will break Windows 11 BitLocker and Windows Hello (PIN login). Ensure you have your passwords available.*

1. Restart the computer.
2. Tap the `DEL` key repeatedly during startup to enter the BIOS/UEFI.
3. Navigate to **Settings** > **Miscellaneous**.
4. Locate **AMD CPU fTPM** and change the value to **Disabled**.
5. Press `F10` to Save and Exit.
6. Test the system under load. If it remains stable, proceed to Remediation 2.

## Remediation 2: Update BIOS (Permanent Fix)

### Step 1: Download the BIOS
1. Navigate to the official Gigabyte support page: `https://www.gigabyte.com/Motherboard/B550-GAMING-X-rev-10/support#support-dl-bios` *(Note: Verify your exact motherboard revision printed on the bottom left corner of the physical board, e.g., Rev 1.0 vs V2).*
2. Download the latest non-beta BIOS version (look for notes mentioning "Update AMD AGESA V2" or "fTPM stuttering fix").

### Step 2: Prepare the USB Drive
1. Insert a USB flash drive into your working Windows machine.
2. Open Windows File Explorer, right-click the USB drive, and select **Format**.
3. Set the File System exactly to **FAT32** (BIOS cannot read NTFS or exFAT).
4. Click **Start** to format (this erases all data on the drive).

### Step 3: Extract and Copy Files
1. Extract the downloaded ZIP file containing the BIOS.
2. Locate the primary BIOS file (it will typically be named something like `B550GAMINGX.F15`).
3. Copy this specific file to the root directory of your FAT32 USB drive.

### Step 4: Execute Q-Flash Update
1. Leave the USB drive plugged into the motherboard (preferably a black USB 2.0 port on the rear I/O).
2. Restart the computer and tap `DEL` to enter the BIOS.
3. Press `F8` or click the **Q-Flash** button (usually at the bottom of the screen).
4. Select **Update BIOS**.
5. Select your USB flash drive and choose the BIOS file you copied (`B550GAMINGX.F15`).
6. Press `Enter` to start the update. **DO NOT turn off the computer or remove the USB drive during this process.**
7. The system will automatically reboot multiple times when finished. Re-enter the BIOS to verify the new version and re-enable fTPM and your RAM XMP profiles.
