Summary:	Create a tree of hardlinks
Name:		hardlink
Version:	1.0
Release:	%mkrel 11
Epoch:		1
Group:		System/Base 
URL:		http://pkgs.fedoraproject.org/gitweb/?p=hardlink.git
License:	GPL+
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
gcc $RPM_OPT_FLAGS hardlink.c -o hardlink

%install
rm -rf %{buildroot}
install -D -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/hardlink.1
install -D -m 755 hardlink %{buildroot}%{_sbindir}/hardlink

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/hardlink
%{_mandir}/man1/hardlink.1*



