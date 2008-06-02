Summary:	Utility for decompressing alzip format files
Summary(pl.UTF-8):	Narzędzie do dekompresji plików w formacie alzip
Name:		unalz
Version:	0.62
Release:	1
License:	BSD
Group:		Applications/Archiving
Source0:	http://www.kipple.pe.kr/win/unalz/%{name}-%{version}.tgz
# Source0-md5:	564bf1dc61bb443faf7e8be1d1b5efc8
URL:		http://www.kipple.pe.kr/win/unalz/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility for decompressing alzip format files.

%description -l pl.UTF-8
Narzędzie do dekompresji plików w formacie alzip.

%prep
%setup -q -n %{name}

%build
%{__make} linux-utf8 \
	CC="%{__cc}" \
	CPP="%{__cxx}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" \
	CXXFLAGS="%{rpmcxxflags} -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"

%install
rm -rf $RPM_BUILD_ROOT

install -D unalz $RPM_BUILD_ROOT%{_bindir}/unalz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/*
