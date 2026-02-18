import os
import json
import subprocess
from datetime import datetime
SNAPSHOT_FILE = f"snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return sorted(result.strip().split("\n"))
    except:
        return []
def get_installed_packages():
    if os.path.exists("/usr/bin/dpkg"):
        return run_command("dpkg -l | awk '{print $2}'")
    else:
        return []
def get_running_services():
    if os.path.exists("/bin/systemctl") or os.path.exists("/usr/bin/systemctl"):
        return run_command("systemctl list-units --type=service --state=running --no-legend | awk '{print $1}'")
    return []
def capture_snapshot():
    snapshot = {
        "timestamp": datetime.now().isoformat(),
        "installed_packages": get_installed_packages(),
        "environment_variables": dict(os.environ),
        "active_users": run_command("query user | findstr 'Active'"),
        "running_services": get_running_services()
    }
    with open(SNAPSHOT_FILE, "w") as f:
        json.dump(snapshot, f, indent=4)
    print(f"Snapshot saved as: {SNAPSHOT_FILE}")
if __name__ == "__main__":
    capture_snapshot()
