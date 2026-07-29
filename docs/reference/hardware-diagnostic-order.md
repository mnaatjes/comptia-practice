---
title: "Hardware Diagnostic Execution Order"
tags: ["hardware", "troubleshooting", "diagnostics", "reference"]
created_at: "2026-07-29"
last_updated_at: "2026-07-29"
---

# Hardware Diagnostic Execution Order

This reference guide outlines the prioritized order of operations for diagnosing hardware instability (specifically load-induced crashes or black screens) after completing a BIOS/UEFI update. This follows the methodology of least invasive to most invasive testing.

## Step 1: Visual Inspection (Zero-Power State)
* Perform this immediately while the machine is powered down during the BIOS update process.
* Check the GPU capacitors (especially on older architectures like the RX 580) and ensure the 8-pin PCIe power cable is fully seated without scorch marks or melting.
* Check the motherboard for bulging capacitors or discolored VRM heatsinks.

## Step 2: BIOS Verification (Pre-Boot State)
* After the update completes, boot into the BIOS.
* Verify the new version number is displayed.
* Ensure `fTPM` is enabled (to verify the microcode patch worked).
* Re-enable the RAM's XMP/DOCP profile to restore baseline performance.
* Check the **PC Health Status** tab to ensure baseline voltages (12V, 5V, 3.3V) are stable while idle.

## Step 3: Storage Health Check (Post-Boot State)
* Boot into Windows.
* Run **CrystalDiskInfo** to check S.M.A.R.T. data. 
* Ensure the boot drive is healthy before subjecting the OS to stress tests, preventing file system corruption if the system crashes during testing.

## Step 4: GPU Isolation Test (Targeted Load)
* Run **FurMark** for 15 minutes.
* Because the RX 580 is an aging, power-hungry card, this test isolates it from the CPU. Monitor temperatures closely. 
* If it crashes here, the GPU's thermal paste has failed or its internal power delivery (VRMs) is dying.

## Step 5: PSU Stress Test (Maximum Load)
* If FurMark passes, run the **OCCT Power Test**.
* This runs the CPU and GPU at 100% capacity simultaneously, creating massive transient power spikes. 
* If the system immediately black-screens (generating a Kernel-Power 41 event upon reboot), the Power Supply Unit (PSU) is definitively failing and must be replaced.

## Step 6: CPU/RAM Verification (Low Probability Isolation)
* Run **MemTest86** (via bootable USB) followed by **Prime95** (Blend Test) in Windows.
* Perform these last. While defective RAM or CPU instability causes blue screens or application crashes, it rarely causes a pure "black screen / fans still spinning" symptom.
