Summary:	Header-only cross-platform HTTP/HTTPS library
Summary(pl.UTF-8):	Wieloplatformowa biblioteka HTTP/HTTPS składająca się z jednego nagłówka
Name:		cpp-httplib
Version:	0.20.0
Release:	1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/yhirose/cpp-httplib/releases
Source0:	https://github.com/yhirose/cpp-httplib/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5f43728fcccbc2d39238116569b320a0
URL:		https://github.com/yhirose/cpp-httplib
BuildRequires:	cmake >= 3.14.0
BuildRequires:	libbrotli-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	openssl-devel >= 3.0.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# header-only library, but cmake files location is arch-dependent
%define		_enable_debug_packages	0

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
Requires:	zlib-devel
Requires:	zstd-devel

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
