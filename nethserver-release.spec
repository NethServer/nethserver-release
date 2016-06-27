%define distroversion 6.8
%define distrorelease Final

Summary: NethServer YUM repo configuration
Name: nethserver-release
Version: 6.8
Release: 1%{?dist}
License: GPL
BuildArch: noarch
Source: %{name}-%{version}.tar.gz
URL: %{url_prefix}/%{name}

BuildRequires: perl, nethserver-devtools

%description
NethServer YUM repository configuration

%prep
%setup

%build
perl createlinks
echo %{distroversion} > root/etc/yum/vars/distroversion
echo %{distroversion} > root/etc/e-smith/db/configuration/force/sysconfig/Version
echo %{distrorelease} > root/etc/e-smith/db/configuration/force/sysconfig/Release
echo "NethServer release %{distroversion} (%{distrorelease})" > root/etc/%{name}

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -not -name '*.orig' -print  | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT                   > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING"                             >> %{name}-%{version}-%{release}-filelist
echo "%config(noreplace) /etc/yum.repos.d/NethServer.repo" >> %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)

%changelog
* Mon Jun 27 2016 Davide Principi <davide.principi@nethesis.it> - 6.8-2
- nethserver-release installation fails on clean CentOS - Bug #3410 [NethServer]

* Tue Jun 14 2016 Davide Principi <davide.principi@nethesis.it> - 6.8-1
- NethServer 6.8 Final release

* Thu May 26 2016 Davide Principi <davide.principi@nethesis.it> - 6.8-0.1
- NethServer 6.8 beta1 release

* Thu Oct 15 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 6.7-0.4-1
- Requires nethserver-firewall-base

* Thu Oct 15 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 6.7-0.3-1
- NethServer Release 6.7 final

* Wed Mar 18 2015 Davide Principi <davide.principi@nethesis.it> - 6.6-2
- Fixed nethserver-install script

* Mon Mar 16 2015 Davide Principi <davide.principi@nethesis.it> - 6.6-1
- NethServer 6.6 final release.

* Thu Mar 05 2015 Davide Principi <davide.principi@nethesis.it> - 6.6-0.9-rc1
- YUM package groups moved to nethserver-updates

* Wed Mar  4 2015 Davide Principi <davide.principi@nethesis.it> - 6.6-0.8.rc1
- Changed mirror URLs. Added $distroversion YUM variable/placeholder. 
- New repository URLs pointing to mirrorlist.nethserver.org

* Mon Feb  2 2015 Davide Principi <davide.principi@nethesis.it> - 6.6-0.6
- Fixed release number 6.6 in nethserver-install

