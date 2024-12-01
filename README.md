ISW Stealth
===========

[![Logo](https://github.com/kyokenn/isw-stealth/blob/master/image/isw.svg)](https://github.com/kyokenn/isw-stealth/blob/master/image/isw.svg)

Ice-Sealed Wyvern. It is meant to alter fan profiles of MSI laptops.

A fork of [ISW](https://github.com/YoyPa/isw) and [ISW-Modern](https://github.com/FaridZelli/ISW-Modern)


Installation
------------

Clone the git repository (including **acpi_ec** submodule):
```
git clone --recurse-submodules https://github.com/kyokenn/isw-stealth.git
cd isw-stealth
```

Install **acpi_ec** kernel module. This module provides file /dev/ec for reading and writing
laptop hardware configuration.

**RPM based distros with AKMOD:**

* Build RPM files:
```
cd acpi_ec_akmod
make rpm
```

* Install RPM files using package manager.

**DEB based distros with AKMOD:**

* Build DEB files:
```
cd acpi_ec_akmod
make deb
```

* Install DEB files using package manager.


**Other distros with DKMS:**

Follow the instructions on [acpi_ec](https://github.com/saidsay-so/acpi_ec)


Usage
-----

```
sudo ./isw -f path_to_config_file.conf <options>
```

List of supported laptops
-------------------------

You can search the configuration files for the supported laptops [here](https://github.com/kyokenn/isw-stealth/blob/master/etc)

You can dump your ACPI EC data on Linux using:
```
sudo hexdump -C /dev/ec
```

You can debug your ACPI EC data on Windows with MSI Control Center and [ec_probe](https://github.com/hirschmann/nbfc)


FAQ
---

* **Q:** Why ISW-Stealth?  
**A:** I originally used ISW on my MSI Stealth 14, hence the name.

* **Q:** Can I enable Secure Boot?  
**A:** No. You have to use unsigned out of tree kernel module **acpi_ec**.

* **Q:** Is this a revival of ISW?  
**A:** No. But anyone can use it freely if find it useful.

* **Q:** Is the original project dead?  
**A:** Yes. Both ISW and ISW-Modern are not maintained at this moment.

* **Q:** My laptop exploded!  
**A:** **WARNING!** **You could break your laptop by directly writing to the ACPI EC!**


Useful resources
----------------

* https://github.com/YoyPa/isw
* https://github.com/FaridZelli/ISW-Modern
* https://github.com/musikid/acpi_ec
* https://github.com/hirschmann/nbfc
* https://github.com/nbfc-linux/nbfc-linux
