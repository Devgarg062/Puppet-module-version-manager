import os
import shutil
import json
import sys

REPO_PATH = "modules_repo"
INSTALL_PATH = "installed_modules"
VERSION_FILE = "versions.json"


def load_versions():
    if not os.path.exists(VERSION_FILE):
        return {}
    with open(VERSION_FILE, "r") as f:
        return json.load(f)


def save_versions(data):
    with open(VERSION_FILE, "w") as f:
        json.dump(data, f, indent=4)


def list_versions(module_name):
    path = os.path.join(REPO_PATH, module_name)
    if not os.path.exists(path):
        print("❌ Module not found")
        return
    print("Available versions:")
    for version in os.listdir(path):
        print(version)


def install(module_name, version):
    source = os.path.join(REPO_PATH, module_name, version)
    destination = os.path.join(INSTALL_PATH, module_name)

    if not os.path.exists(source):
        print("❌ Version not found")
        return

    if os.path.exists(destination):
        shutil.rmtree(destination)

    shutil.copytree(source, destination)

    versions = load_versions()
    versions[module_name] = version
    save_versions(versions)

    print(f"✅ Installed {module_name} version {version}")


def remove(module_name):
    path = os.path.join(INSTALL_PATH, module_name)

    if not os.path.exists(path):
        print("❌ Module not installed")
        return

    shutil.rmtree(path)

    versions = load_versions()
    versions.pop(module_name, None)
    save_versions(versions)

    print(f"✅ Removed {module_name}")


def current():
    versions = load_versions()
    if not versions:
        print("No modules installed")
    else:
        print("Installed modules:")
        for mod, ver in versions.items():
            print(f"{mod} : {ver}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Commands: list | install | remove | current")
        sys.exit()

    command = sys.argv[1]

    if command == "list":
        list_versions(sys.argv[2])

    elif command == "install":
        install(sys.argv[2], sys.argv[3])

    elif command == "remove":
        remove(sys.argv[2])

    elif command == "current":
        current()

    else:
        print("Unknown command")