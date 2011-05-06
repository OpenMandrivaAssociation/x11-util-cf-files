Name: x11-util-cf-files
Version: 1.0.4
Release: %mkrel 2
Summary: Templates for imake
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: http://xorg.freedesktop.org/releases/individual/util/xorg-cf-files-%{version}.tar.bz2
Patch0: 0001-Add-mdvconfig.patch
License: MIT
Obsoletes: xorg-cf-files < 1.0.2

%description
Templates for imake

%prep
%setup -q -n xorg-cf-files-%{version}
%patch0 -p1 -b .mdvconfig

%build
%configure2_5x --with-config-dir=%{_datadir}/X11/config
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %_datadir/X11/config
%_datadir/X11/config/*

