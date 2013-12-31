Name:		x11-util-cf-files
Version:	1.0.5
Release:	5
Summary:	Templates for imake
Group:		Development/X11

Source0:	http://xorg.freedesktop.org/releases/individual/util/xorg-cf-files-%{version}.tar.bz2
Patch0:		0001-Add-mdvconfig.patch
License:	MIT
Obsoletes:	xorg-cf-files < 1.0.2
BuildArch:	noarch

%description
Templates for imake.

%prep
%setup -q -n xorg-cf-files-%{version}
%patch0 -p1 -b .mdvconfig

%build
%configure2_5x \
		--with-config-dir=%{_datadir}/X11/config

%make

%install
%makeinstall_std

%files
%dir %{_datadir}/X11/config
%{_datadir}/X11/config/*
