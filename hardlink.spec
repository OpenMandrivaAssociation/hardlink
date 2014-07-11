Summary:	Create a tree of hardlinks
Name:		hardlink
Epoch:		1
Version:	1.0
Release:	19
Group:		System/Base 
License:	GPLv2
Url:		http://cvsweb.openwall.com/cgi/cvsweb.cgi/Owl/packages/hardlink/
Source0:	hardlink.c
Source1:	hardlink.1
Obsoletes:	kernel-utils

%description
hardlink is used to create a tree of hard links.
It's used by kernel installation to dramatically reduce the
amount of diskspace used by each kernel package installed.

%prep
%setup -q -c -T
install -pm 644 %{SOURCE0} hardlink.c

%build
gcc %{optflags} hardlink.c -o hardlink

%install
install -D -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/hardlink.1
install -D -m 755 hardlink %{buildroot}%{_sbindir}/hardlink

%files
%{_sbindir}/hardlink
%{_mandir}/man1/hardlink.1*

