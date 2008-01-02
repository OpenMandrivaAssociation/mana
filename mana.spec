%define	version  0.2.1
%define	release  %mkrel 1

Name:      mana
Summary:   Kana-Kanji conversion engine for Japanese
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPL
URL:       http://sourceforge.jp/projects/shinji/
Source0:   http://prdownloads.sourceforge.jp/shinji/19974/%{name}-%{version}.tar.bz2
Patch0:    mana_change_scheme_dir.diff
Patch1:    mana_fix_destdir.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:      ocaml camlp4 ocamlfind-mini
Requires:      gdbm
BuildRequires: automake1.4
BuildRequires: ocaml camlp4 ocamlfind-mini
BuildRequires: gdbm gdbm-devel

%description
Kana-Kanji conversion engine for Japanese.


%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
./configure \
      --prefix=/usr \
      --libexecdir=/%{_libdir}

# disable parallel build (broken):
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# install mana-prelude.scm for uim
install -d %{buildroot}/%{_datadir}/uim/
install -m 644 mana/mana-prelude.scm %{buildroot}/%{_datadir}/uim/
%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/*-config

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS* ChangeLog* COPYING* NEWS*
%doc README*
%{_bindir}/*
%{_datadir}/uim/*.scm
%{_libdir}/mana/*
%multiarch %multiarch_bindir/*-config


