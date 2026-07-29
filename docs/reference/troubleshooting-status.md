---
title: "Troubleshooting Status"
tags: ["hardware", "troubleshooting", "status"]
created_at: "2026-07-29"
last_updated_at: "2026-07-29"
---

# Hardware Troubleshooting Status

## Session Information
* **Conversation UUID:** `74e6b949-9063-4e3e-8294-29ff3319257b`
* **Target Machine:** Windows 11 Desktop (GIGABYTE B550 Gaming X Rev 1.0, AM4 CPU, RX 580 GPU)
* **Primary Symptom:** System hard-crashes (black screen, no signal, fans remain spinning) under gaming load, and eventually under zero load in BIOS/Safe Mode.

## Completed Diagnostics
1. **Case Power Button:** Bypassed (confirmed faulty, using screwdriver to jump pins).
2. **Event Logs (Software):** Extracted `windows_system_log.evtx`. Identified `Kernel-Power 41` (hard power loss) and `TPM-WMI` errors. Zero "Display" driver crash events found.
3. **Firmware Update (BIOS):** 
   * Motherboard bricked during standard update (3 short beeps / Base 64K RAM failure).
   * Successfully recovered via hardware-level **Q-Flash Plus** using USB on rear I/O.
   * Motherboard is now successfully running the non-beta `F18` BIOS, definitively eliminating the AMD fTPM microcode bug as a variable.
4. **Current Status:** Following the successful BIOS update, the machine still crashed (black screen) immediately upon idling in Windows, confirming a severe physical hardware fault.

## Pending Action (Next Steps)
* **GPU Isolation Test (Physical Swap):** The user must physically remove the RX 580 and install the known-working **HD 7870**.
* **Expected Outcome:**
  * If the system boots into Windows and runs perfectly with the HD 7870, the **RX 580 is physically dead** (VRMs or core).
  * If the system continues to black-screen with the HD 7870 installed, the **Power Supply Unit (PSU) is dead** (failing to provide stable 12V current) and must be replaced.
