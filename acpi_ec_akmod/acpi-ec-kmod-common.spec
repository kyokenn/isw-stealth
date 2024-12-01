%define debug_package %{nil}

Name: acpi-ec-kmod-common

Version:        1.0.4
Release:        1%{?dist}.1
Summary:        Kernel module to access directly to the ACPI EC.

Group:          System Environment/Kernel

License:        GPL-3.0
URL:            https://github.com/saidsay-so/acpi_ec
Source0:        acpi-ec_%{version}.orig.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       kmod-acpi-ec


%description
Kernel module to access directly to the ACPI EC.


%prep
%autosetup -n acpi-ec_%{version}


%setup -q -c -T -a 0


%build


%install


%clean
rm -rf ${RPM_BUILD_ROOT}


%pre


%files
