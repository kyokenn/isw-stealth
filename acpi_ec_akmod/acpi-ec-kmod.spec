# based on template from https://rpmfusion.org/Packaging/KernelModules/Kmods2
# (un)define the next line to either build for the newest or all current kernels
#define buildforkernels newest
#define buildforkernels current
%define buildforkernels akmod

%define debug_package %{nil}

# name should have a -kmod suffix
Name: acpi-ec-kmod

Version:        1.0.4
Release:        1%{?dist}.1
Summary:        Kernel module to access directly to the ACPI EC

Group:          System Environment/Kernel

License:        GPL-3.0
URL:            https://github.com/saidsay-so/acpi_ec
Source0:        acpi-ec_%{version}.orig.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  %{_bindir}/kmodtool


# Verify that the package build for all architectures.
# In most time you should remove the Exclusive/ExcludeArch directives
# and fix the code (if needed).
# ExclusiveArch:  i686 x86_64 ppc64 ppc64le armv7hl aarch64
# ExcludeArch: i686 x86_64 ppc64 ppc64le armv7hl aarch64

# get the proper build-sysbuild package from the repo, which
# tracks in all the kernel-devel packages
BuildRequires:  %{_bindir}/kmodtool

#%{!?kernels:BuildRequires: buildsys-build-rpmfusion-kerneldevpkgs-%{?buildforkernels:%{buildforkernels}}%{!?buildforkernels:current}-%{_target_cpu} }


# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }


%description
Kernel module to access directly to the ACPI EC


%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}
# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu}  --repo %{repo} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null


%setup -q -c -T -a 0


%build
for kernel_version in %{?kernel_versions}; do
    make %{?_smp_mflags} -C "${kernel_version##*___}" M=${PWD}/acpi-ec_%{version} modules
done


%install
rm -rf ${RPM_BUILD_ROOT}
for kernel_version in %{?kernel_versions}; do
    mkdir -p ${RPM_BUILD_ROOT}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}
    cp -v acpi-ec_%{version}/*.ko ${RPM_BUILD_ROOT}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}
done
%{?akmod_install}


%clean
rm -rf ${RPM_BUILD_ROOT}