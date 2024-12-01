obj-m+=acpi_ec.o
KERNELDIR?=/lib/modules/$(shell uname -r)/build
DRIVERDIR?=$(shell pwd)

VERSION=1.0.4
SRC=\
	Makefile \
	acpi-ec-kmod-common.spec \
	acpi-ec-kmod.spec \
	../acpi_ec/README.md \
	../acpi_ec/dkms.conf \
	../acpi_ec/src/acpi_ec.c
SRCDIR=acpi-ec_$(VERSION)
ARCHIVE=$(SRCDIR).orig.tar.xz

all:
	echo "No need to build kernel modules now."
	echo "Kernel modules are built at packages installation time using DKMS or AKMOD."

# invoked by debian/rules
install:
	mkdir -p $(DESTDIR)/usr/src/acpi-ec-$(VERSION)
	cp -fv ../acpi_ec/src/acpi_ec.c Makefile $(DESTDIR)/usr/src/acpi-ec-$(VERSION)/

# invoked by dkms
kernel_modules:
	$(MAKE) -C $(KERNELDIR) M=$(DRIVERDIR) modules

kernel_modules_install:
	$(MAKE) -C $(KERNELDIR) M=$(DRIVERDIR) modules_install

kernel_clean:
	$(MAKE) -C $(KERNELDIR) M=$(DRIVERDIR) clean

# build source archive, needed by rpm and deb
../$(ARCHIVE): $(SRC)
	mkdir -p $(SRCDIR)
	cp -fv $^ $(SRCDIR)/
	tar Jcvf $@ $(SRCDIR)
	rm -Rf $(SRCDIR)

# copies specs to rpmbuild's specs path
~/rpmbuild/SPECS/%.spec: %.spec
	mkdir -p ~/rpmbuild/SPECS
	cp -fv $^ $@

# copies archive from parent directory to rpmbuild's sources path
~/rpmbuild/SOURCES/%.tar.xz: ../%.tar.xz
	mkdir -p ~/rpmbuild/SOURCES
	cp -fv $^ $@

rpm: \
	~/rpmbuild/SOURCES/$(ARCHIVE) \
	~/rpmbuild/SPECS/acpi-ec-kmod.spec \
	~/rpmbuild/SPECS/acpi-ec-kmod-common.spec
	rpmbuild -bb acpi-ec-kmod.spec
	rpmbuild -bb acpi-ec-kmod-common.spec

builddep: \
	dnf install kmodtool

deb: ../$(ARCHIVE)
	debuild -uc -us
