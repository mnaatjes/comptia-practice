---
title: "Troubleshoot System Hard Lock"
tags: ["hardware", "troubleshooting", "hard-lock", "comptia"]
created_at: "2026-07-29"
last_updated_at: "2026-07-29"
---

# Troubleshoot System Hard Lock

## Diagnostic
Complete system hard-lock (System Freeze).

## Theory
This is no longer exclusively a GPU issue. If the motherboard fails to respond to a sustained (10+ seconds) press of the physical power button, the system has locked up at the lowest hardware level (ACPI state failure). This indicates a severe fault, often caused by a failing Power Supply Unit (PSU), a catastrophic motherboard error, severe overheating (CPU/VRM), or faulty RAM causing a critical system halt.

## Remediation

### Step 1: Force Power Cut
* Flip the physical switch on the back of the Power Supply Unit (PSU) to the "Off" (O) position.
* If the PSU lacks a switch, physically unplug the power cable from the wall or the back of the machine.

### Step 2: Drain Residual Power (Power Cycling)
* With the system completely unplugged/switched off, press and hold the front power button for 30 seconds. This drains residual charge from the motherboard capacitors.

### Step 3: Component Isolation (Breadboarding concept)
Before attempting to turn it back on, reduce the system to its absolute minimum required components to POST:
1. Unplug all USB devices except the keyboard.
2. Remove the discrete GPU entirely (if your CPU supports integrated graphics).
3. Remove all but one stick of RAM (place it in the primary slot, usually the second slot from the CPU).
4. Reconnect power and attempt to boot. If it boots successfully, add components back one at a time to identify the exact point of failure.
