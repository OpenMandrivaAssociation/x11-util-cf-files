Name:		x11-util-cf-files
Version:	1.0.8
Release:	2
Summary:	Templates for imake
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/util/xorg-cf-files-%{version}.tar.xz
Patch0:		0001-Add-mdvconfig.patch
License:	MIT
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	x11-font-util
Obsoletes:	xorg-cf-files < 1.0.2
BuildArch:	noarch

%description
Templates for imake.

%prep
%autosetup -p1 -n xorg-cf-files-%{version}

%build
%configure \
	--with-config-dir=%{_datadir}/X11/config

%make_build

%install
%make_install

%files
%dir %{_datadir}/X11/config
%{_datadir}/X11/config/*
