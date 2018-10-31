Summary:	Create a tree of hardlinks
Name:		hardlink
Epoch:		1
Version:	1.3
Release:	2
Group:		System/Base
License:	GPLv2
Url:		https://pagure.io/hardlink
Source0:	https://pagure.io/hardlink/raw/master/f/hardlink.c
Source1:	https://pagure.io/hardlink/raw/master/f/hardlink.1
BuildRequires:	clang
BuildRequires:	pkgconfig(libpcre2-8)
Obsoletes:	kernel-utils

%description
hardlink is used to create a tree of hard links.
It's used by kernel installation to dramatically reduce the
amount of diskspace used by each kernel package installed.

%prep
%setup -q -c -T
install -pm 644 %{SOURCE0} hardlink.c

%build
%{__cc} %{optflags} %{ldflags} hardlink.c -o hardlink -lpcre2-8

%install
install -D -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/hardlink.1
install -D -m 755 hardlink %{buildroot}%{_sbindir}/hardlink

%files
%{_sbindir}/hardlink
%{_mandir}/man1/hardlink.1*
