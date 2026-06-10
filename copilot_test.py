#!/usr/bin/env python
"""Script to print system uptime."""

import subprocess
import platform


def get_system_uptime():
    """Get and print system uptime."""
    system = platform.system()

    try:
        if system == "Linux":
            # On Linux, use uptime command
            result = subprocess.run(["uptime"], capture_output=True, text=True)
            uptime = result.stdout.strip()
        elif system == "Darwin":
            # On macOS, use uptime command
            result = subprocess.run(["uptime"], capture_output=True, text=True)
            uptime = result.stdout.strip()
        elif system == "Windows":
            # On Windows, use PowerShell to compute uptime from last boot time
            result = subprocess.run(
                ["powershell", "-NoProfile", "-Command",
                 "(Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime"],
                capture_output=True,
                text=True
            )
            uptime = result.stdout.strip()
        else:
            uptime = f"Unknown operating system: {system}"
    except Exception as e:
        uptime = f"Error retrieving uptime: {str(e)}"
    
    print("System Uptime:")
    print(uptime)


if __name__ == "__main__":
    get_system_uptime()
