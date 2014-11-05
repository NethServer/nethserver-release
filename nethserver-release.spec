%define distroversion 6.6
%define distrorelease Beta1

Summary: NethServer YUM repo configuration
Name: nethserver-release
Version: %{distroversion}
Release: 0.3.beta1%{?dist}
License: GPL
BuildArch: noarch
Source: %{name}-%{version}.tar.gz
URL: %{url_prefix}/%{name}

Requires: centos-release
BuildRequires: perl, nethserver-devtools

%description
NethServer YUM repository configuration

%prep
%setup

%build
perl createlinks 
echo %{distroversion} > root/etc/e-smith/db/configuration/force/sysconfig/Version
echo %{distrorelease} > root/etc/e-smith/db/configuration/force/sysconfig/Release
echo "NethServer release %{distroversion} (%{distrorelease})" > root/etc/nethserver-release

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -not -name '*.orig' -print  | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT                   > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING"                             >> %{name}-%{version}-%{release}-filelist
echo "%config(noreplace) /etc/yum.repos.d/NethServer.repo" >> %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)

%changelog
* Fri Mar 28 2014 Davide Principi <davide.principi@nethesis.it> - 6.5-6
- Fixed Version Release prop expansion

* Tue Mar 25 2014 Davide Principi <davide.principi@nethesis.it> - 6.5-5
- Final release

* Wed Feb 26 2014 Davide Principi <davide.principi@nethesis.it> - 6.5-4
- rc1 release

* Thu Oct 17 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 6.4-beta2.ns6
- Beta2 release based on CentOS 6.4 

* Thu May 02 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 6.4-beta1.ns6
- First beta release based on CentOS 6.4 

* Mon Mar 18 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 6.4-alpha2.ns6
- First alpha release based on CentOS 6.4 

