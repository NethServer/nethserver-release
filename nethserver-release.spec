Summary: NethServer release file
Name: nethserver-release
%define version 10
%define release TP01
%define displayversion %{version}
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: System Environment/Base
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: centos-release
Requires: nethserver-base
BuildRequires: perl, nethserver-devtools

%description
NethServer release file

%changelog
* Wed Oct 12 2011 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> 10.TP01.nh
- First Techincal Preview

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/etc
echo "NethServer release %{displayversion}" >\
 $RPM_BUILD_ROOT/etc/nethserver-release
mkdir -p $RPM_BUILD_ROOT/etc/e-smith/db/configuration/force/sysconfig
echo "%{displayversion}" \
   > $RPM_BUILD_ROOT/etc/e-smith/db/configuration/force/sysconfig/ReleaseVersion
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    > %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
