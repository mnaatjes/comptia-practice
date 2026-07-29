---
title: "Windows 11 OS Reinstallation & Hardware Licensing Guide"
tags: ["windows", "reinstallation", "hardware", "licensing", "dual-boot"]
created_at: "2026-07-29"
last_updated_at: "2026-07-29"
---

# Windows 11 Reinstallation & Licensing Guide

## Phase 1: Pre-Wipe Data Extraction (Once New PSU is Installed)
Before wiping your bloated Windows 11 installation, boot into the current OS one last time to manually extract and save your cryptographic hardware identifiers and license keys to a USB drive or cloud storage.

1. **Open an Elevated Terminal:** Right-click the Start Menu and select **Windows Terminal (Admin)** or **Command Prompt (Admin)**.
2. **Extract Motherboard UUID:**
   * Run: `wmic csproduct get UUID`
   * *Purpose:* This is the exact cryptographic fingerprint of your GIGABYTE motherboard that Microsoft uses to identify your machine on their servers.
3. **Extract Windows Product Key:**
   * Run: `wmic path softwarelicensingservice get OA3xOriginalProductKey`
   * *Note:* If this returns blank (common for digital upgrades), extract the active registry key by running:
     `powershell "(Get-WmiObject -query 'select * from SoftwareLicensingService').OA3xOriginalProductKey"`
4. **Save Data:** Copy the outputs of both commands into a Notepad file (`hardware-keys.txt`) and save it to an external flash drive or cloud service.

## Phase 2: Building the Installation Media
1. **Prepare USB:** Insert an 8GB+ USB flash drive into the computer (this will erase all data currently on the USB).
2. **Download Tool:** Navigate to the official Microsoft website and download the **Windows 11 Media Creation Tool**.
3. **Flash the Drive:** Run the `.exe` file. Select "Create installation media (USB flash drive, DVD, or ISO file) for another PC."
4. **Target the USB:** Select your inserted USB drive. The tool will format the drive, download the pristine OS image directly from Microsoft, and make the drive bootable.

## Phase 3: The Clean Installation & Dual-Boot Architecture
Your goal is to isolate Windows 11 completely to the 1TB M.2 drive, leaving the 2TB M.2 drive entirely unpartitioned and untouched for a future, physically segregated Linux (Debian) installation.

1. **Boot from USB:** Restart the computer and tap `F12` (Gigabyte Boot Menu) to boot directly from the Windows 11 USB.
2. **The Product Key Screen:** When prompted for a product key, click **"I don't have a product key"** at the bottom of the window.
3. **Drive Wiping (Crucial Step):** 
   * When asked "Where do you want to install Windows?", you will see a list of partitions. 
   * Identify your 1TB drive (usually Drive 0 or Drive 1). 
   * Select and **Delete** every single partition associated with that 1TB drive (e.g., System, Reserved, Primary, Recovery) until it consolidates into a single line labeled **"Drive X Unallocated Space"** (approx. 930GB).
4. **Installation:** Select that Unallocated Space and click Next. Windows will automatically format the drive and install the OS strictly within the physical boundaries of the 1TB M.2 drive.
5. **Preserving Linux Space:** Do *not* touch or format the 2TB M.2 drive during this process. Leave it alone so the future Linux installer can claim it natively.

## Phase 4: HWID Activation & Troubleshooting
1. **Automatic HWID Activation:** Once Windows 11 boots to the desktop, connect to the internet. Windows will silently send your motherboard's UUID to the Microsoft Azure activation servers. Microsoft will recognize the hardware fingerprint from your previous installation and automatically activate Windows with a Digital License.
2. **Troubleshooting Activation Failure:** 
   * If Windows fails to activate automatically after 24 hours, navigate to **Settings > System > Activation**.
   * Click **Troubleshoot**. 
   * Select **"I changed hardware on this device recently"** (even though you only changed the PSU). 
   * This forces the system to log into your Microsoft Account, pull your digital entitlement, and re-apply it to the motherboard UUID. If this fails, you possess the `hardware-keys.txt` backup from Phase 1 to manually force activation via Microsoft Phone Support.
