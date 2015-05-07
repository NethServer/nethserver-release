%define distroversion 7
%define distrorelease alpha1

Summary: NethServer YUM repo configuration
Name: nethserver-release
Version: 7
Release: 0.1%{?dist}
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
%{__install} -d root/%{_nseventsdir}/%{name}-update

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -not -name '*.orig' -print  | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%config(noreplace) /etc/yum.repos.d/NethServer.repo
%dir %{_nseventsdir}/%{name}-update

%changelog
* Wed May  6 2015 Davide Principi <davide.principi@nethesis.it> - 7-0.1
- First 7-0.1 alpha1 release


