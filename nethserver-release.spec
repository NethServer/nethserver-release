%define distroversion 6.5
%define distrorelease Final

Summary: NethServer release rebrand
Name: nethserver-release
Version: %{distroversion}
Release: 5%{?dist}
License: GPL
BuildArch: noarch
Source: %{name}-%{version}.tar.gz
URL: %{url_prefix}/%{name}

Requires: centos-release
BuildRequires: perl, nethserver-devtools

%description
Updates /etc/issue and /etc/redhat-release contents

%prep
%setup

%build
perl createlinks 
./setversion '%{version}' '%{distrorelease}'

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -not -name '*.orig' -print  | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT                   > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING"                             >> %{name}-%{version}-%{release}-filelist
echo "%config(noreplace) /etc/yum.repos.d/NethServer.repo" >> %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)

%changelog
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

