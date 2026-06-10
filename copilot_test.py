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
            # On Windows, use wmic command with shell=True
            try:
                result = subprocess.run(
                    ["wmic", "os", "get", "lastbootuptime"],
                    capture_output=True,
                    text=True,
                    shell=True
                )
                uptime = result.stdout.strip()
            except:
                # Fallback: use systeminfo command
                result = subprocess.run(
                    ["systeminfo"],
                    capture_output=True,
                    text=True,
                    shell=True
                )
                uptime = result.strip()
        else:
            uptime = f"Unknown operating system: {system}"
    except Exception as e:
        uptime = f"Error retrieving uptime: {str(e)}"
    
    print("System Uptime:")
    print(uptime)


if __name__ == "__main__":
    get_system_uptime()
