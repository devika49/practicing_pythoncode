
#retrieving the system information
#pip install wmi
import wmi
 
c = wmi.WMI()
for os in c.Win64_operatingSystem():
    print(f"os.Name:{os.Name}")
    print(f"Version:{os.Version}")
    print(f"Manufacturer :{os.Manufacturer}")
    print(f"Architecture: {os.OSArchitecture}")

#output
"""os.Name:Microsoft Windows 11 Home Single Language|C:\Windows|\Device\Harddisk0\Partition3
Version:10.0.22631
Manufacturer :Microsoft Corporation
Architecture: 64-bit """