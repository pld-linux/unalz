Summary:	Utility for decompressing alzip format files
Summary(pl.UTF-8):	Narzędzie do dekompresji plików w formacie alzip
Name:		unalz
Version:	0.60
Release:	1
License:	BSD
Group:		Applications/Archiving
Source0:	http://www.kipple.pe.kr/win/unalz/%{name}-%{version}.tgz
# Source0-md5:	ccab4fa5686522b1d519724eef6f66cd
URL:		http://www.kipple.pe.kr/win/unalz/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility for decompressing alzip format files.

%description -l pl.UTF-8
Narzędzie do dekompresji plików w formacie alzip.

%prep
%setup -q -n %{name}

# lacking functions
cat >> UnAlz.h <<EOF
extern "C" char *strlcpy(char *dst, const char *src, size_t dst_size);
extern "C" char *strlcat(char *dst, const char *src, size_t dst_size);
EOF
cat >> UnAlz.cpp <<EOF
char *strlcpy(char *dst, const char *src, size_t dst_size)
{
  strncpy(dst, src, dst_size - 1);
  dst[dst_size - 1] = 0;
}
char *strlcat(char *dst, const char *src, size_t dst_size)
{
  strncat(dst, src, dst_size - 1);
  dst[dst_size - 1] = 0;
}
EOF

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
