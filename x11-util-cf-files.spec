Name:		x11-util-cf-files
Version:	1.0.5
Release:	4
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

%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2011.0
+ Revision: 671230
- mass rebuild

* Thu Jan 06 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.4-1mdv2011.0
+ Revision: 629005
- New version: 1.0.4
- Rediff and gitify mdvconfig patch

* Fri Dec 10 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 620446
- Use configure2_5x
- Rebuild for 2011.0

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.3-1mdv2010.1
+ Revision: 464158
- New version: 1.0.3
  Updated "mdvconfig" patch

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-6mdv2009.0
+ Revision: 266065
- rebuild early 2009.0 package (before pixel changes)

* Fri May 30 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-5mdv2009.0
+ Revision: 213515
- Define ProjectRoot, defined to /usr/X11R6 in xprint_host.cf if not
  yet defined, and MotifDir, defines to /usr/X11R6 in X11.tmpl if not
  yet defined, to /usr (actually $prefix).

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.2-4mdv2008.1
+ Revision: 99353
- general spec cleanup


* Thu Dec 14 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.0.2-3mdv2007.0
+ Revision: 96969
- empty
- Move man pages to /usr/share/man
  Move config files to /usr/share/X11/config

* Fri Aug 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.2-2mdv2007.0
+ Revision: 51668
- Obsoletes xorg-cf-files (thanks Charles A Edwards for pointing that)

* Wed Aug 02 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.2-1mdv2007.0
+ Revision: 42923
- new upstream release(1.0.2):
  * rman is not built by modular tree.
  * DefaultRGBDatabase is now in share/X11
  * Generate site.def from site.def.in to set ProjectRoot to $prefix (#22652)
- rebuild to fix cooker uploading
- ops, fixing a typo
- renamed package to x11-util-cf-files\n- added description text
- Renaming the package to be consistent with other packages' names

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Laurent Montel <lmontel@mandriva.com>
    - Add

