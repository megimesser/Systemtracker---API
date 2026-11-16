import platform

os_info = platform.freedesktop_os_release()

print(os_info["NAME"])
print(os_info["VERSION"])
print(os_info["ID"])
print(os_info["ID_LIKE"])