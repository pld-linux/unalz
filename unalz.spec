Summary:	Utility for decompressing alzip format files
Summary(pl):	Narzêdzie do dekompresji plików w formacie alzip
Name:		unalz
Version:	0.31
Release:	1
License:	BSD
Group:		Applications/Archiving
Source0:	http://www.kipple.pe.kr/win/unalz/%{name}-%{version}.tgz
# Source0-md5:	a39f14acfdb11fca8fb19fc22b132ea1
URL:		http://www.kipple.pe.kr/win/unalz/
BuildRequires:	libstdc++-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility for decompressing alzip format files.

%description -l pl
Narzêdzie do dekompresji plików w formacie alzip.

%prep
%setup -q

sed -i -e 's/ -liconv//' Makefile

%build
%{__make} posix \
	CC="%{__cc}" \
	CPP="%{__cxx}" \
	CFLAGS="%{rpmcflags} -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" \
	CXXFLAGS="%{rpmcflags} -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"

%install
rm -rf $RPM_BUILD_ROOT

install -D unalz $RPM_BUILD_ROOT%{_bindir}/unalz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/*
