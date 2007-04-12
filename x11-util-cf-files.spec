Name: x11-util-cf-files
Version: 1.0.2
Release: %mkrel 3
Summary: Templates for imake 
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/util/xorg-cf-files-%{version}.tar.bz2
Patch0: xorg-cf-files-1.0.2-mdvconfig.patch
License: MIT
Packager: Gustavo Pichorim Boiko <boiko@mandriva.com>
BuildRoot: %{_tmppath}/%{name}-root
Obsoletes: xorg-cf-files < 1.0.2

%description
Templates for imake

%prep
%setup -q -n xorg-cf-files-%{version}
%patch0 -p1 -b .mdvconfig

%build
%configure2_5x	--with-config-dir=%{_datadir}/X11/config \
		--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

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


