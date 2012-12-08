Name:      mana
Version:   0.2.1
Release:   7
Summary:   Kana-Kanji conversion engine for Japanese
Group:     System/Internationalization
License:   GPL
URL:       http://sourceforge.jp/projects/shinji/
Source0:   http://prdownloads.sourceforge.jp/shinji/19974/%{name}-%{version}.tar.bz2
Patch0:    mana_change_scheme_dir.diff
Patch1:    mana-0.2.1-fix-destdir.patch
Requires:      ocaml
Requires:      camlp4
Requires:      ocaml-findlib
Requires:      gdbm
BuildRequires: automake1.4
BuildRequires: ocaml
BuildRequires: camlp4
BuildRequires: ocaml-findlib
BuildRequires: gdbm
BuildRequires: gdbm-devel

%description
Kana-Kanji conversion engine for Japanese.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
./configure \
    --prefix=%{_prefix} \
    --libexecdir=%{_libdir}

# disable parallel build (broken):
make

%install
%makeinstall_std

# install mana-prelude.scm for uim
install -d %{buildroot}/%{_datadir}/uim/
install -m 644 mana/mana-prelude.scm %{buildroot}/%{_datadir}/uim/
%multiarch_binaries %{buildroot}%{_bindir}/*-config

%files
%doc AUTHORS* ChangeLog* COPYING* NEWS*
%doc README*
%{_bindir}/mana*
%{_datadir}/uim/*.scm
%{_libdir}/mana/*
%{multiarch_bindir}/*-config


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-6mdv2011.0
+ Revision: 661702
- multiarch fixes

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-5mdv2011.0
+ Revision: 523240
- rebuilt for 2010.1

* Sun Sep 27 2009 Olivier Blin <oblin@mandriva.com> 0.2.1-4mdv2010.0
+ Revision: 450124
- don't try to build on arm & mips, there's no ocaml*.opt on theses
  platforms and fixing it to not try to build nativecode is too
  invasive (from Arnaud Patard)

* Sat Jul 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-3mdv2010.0
+ Revision: 399709
- fix build dependencies

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.2.1-2mdv2009.0
+ Revision: 223148
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.2.1-1mdv2008.1
+ Revision: 129658
- kill re-definition of %%buildroot on Pixel's request


* Fri Dec 29 2006 Crispin Boylan <crisb@mandriva.org> 0.2.1-1mdv2007.0
+ Revision: 102575
-new version
- Import mana

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.2.0-2mdk
- fix buildrequires on x86_64

* Wed May 10 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.2.0-1mdk
- add support for multiarch
- disable parallel build (broken)
- first spec for Mandriva (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)

