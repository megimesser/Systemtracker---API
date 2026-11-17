import platform


def os_informationen() -> dict:
    system = platform.system()          # "Linux", "Darwin" (macOS), "Windows"
    if system != "Linux":
        return {"system": system, "id": system.lower(), "family": system.lower()}

    try:
        info = platform.freedesktop_os_release()
    except OSError:
        return {"system": system, "id": "unknown", "family": "unknown"}

    distro_id = info.get("ID", "unknown")
    id_like = info.get("ID_LIKE", "").split()
    return {
        "system": system,
        "name": info.get("NAME", "unknown"),
        "version": info.get("VERSION", "unknown"),
        "id": distro_id,
        "family": id_like[0] if id_like else distro_id,   # "debian", "rhel", ...
    }


if __name__ == "__main__":
    print(os_informationen())