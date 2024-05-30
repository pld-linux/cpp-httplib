Summary:	Header-only cross-platform HTTP/HTTPS library
Summary(pl.UTF-8):	Wieloplatformowa biblioteka HTTP/HTTPS składająca się z jednego nagłówka
Name:		cpp-httplib
Version:	0.15.3
Release:	1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/yhirose/cpp-httplib/releases
Source0:	https://github.com/yhirose/cpp-httplib/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fd24b975844313de2ba3273b9e8add13
URL:		https://github.com/yhirose/cpp-httplib
BuildRequires:	cmake >= 3.14.0
BuildRequires:	libbrotli-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	openssl-devel >= 3.0.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A C++11 single-file header-only cross platform HTTP/HTTPS library.

%description -l pl.UTF-8
Wieloplatformowa biblioteka C++11 do obsługi HTTP/HTTPS, składająca
się z pojedynczego pliku nagłówkowego.

%package devel
Summary:	Header-only cross-platform HTTP/HTTPS library
Summary(pl.UTF-8):	Wieloplatformowa biblioteka HTTP/HTTPS składająca się z jednego nagłówka
Group:		Development/Libraries
Requires:	libbrotli-devel
Requires:	libstdc++-devel >= 6:4.7
Requires:	openssl-devel >= 3.0.0
Requires:	openssl-devel >= 3.0.0
Requires:	zlib-devel

%description devel
A C++11 single-file header-only cross platform HTTP/HTTPS library.

%description devel -l pl.UTF-8
Wieloplatformowa biblioteka C++11 do obsługi HTTP/HTTPS, składająca
się z pojedynczego pliku nagłówkowego.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_includedir}/httplib.h
%{_libdir}/cmake/httplib
