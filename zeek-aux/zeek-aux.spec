Name:           zeek-aux
Version:        0.43
Release:        1%{?dist}
Epoch:          1
Summary:        Zeek Auxiliary Programs

License:        BSD
URL:            https://github.com/zeek/zeek-aux
Source0:        https://www.zeek.org/downloads/%{name}-%{version}.tar.gz

Provides:       bro-aux

BuildRequires:  bind-devel
BuildRequires:  libpcap-devel
BuildRequires:  openssl-devel
BuildRequires:  flex
BuildRequires:  cmake
BuildRequires:  gcc-c++
Requires:       libpcap

%description


%prep
%setup -q


%build
mkdir build; cd build
%cmake ..
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc README
%doc CHANGES
%license COPYING
%{_bindir}/adtrace
%{_bindir}/bro-cut
%{_bindir}/zeek-cut
%{_bindir}/rst
%{_mandir}/man1/zeek-cut.1.gz


%changelog
* Thu Aug 22 2019 Bradford Dabbs <brad@dabbs.io> 0.43-1
- Initial RPM creation
