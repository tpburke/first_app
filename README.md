# System Uptime Script

A cross-platform Python script that displays system uptime.

## Usage

```bash
python copilot_test.py
```

## Features

- **Cross-Platform**: Works on Linux, macOS, and Windows
- **No Dependencies**: Uses only Python standard library
- **Error Handling**: Displays helpful error messages if something goes wrong

## How It Works

The script detects your OS and uses the appropriate command:
- **Linux/macOS**: `uptime` command
- **Windows**: `wmic` command

## Output Example

```
System Uptime:
 10:37:58 up 5 days,  2:15,  1 user,  load average: 0.12, 0.18, 0.15
```

## Requirements

- Python 3.6+
