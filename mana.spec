%define	version  0.2.1
%define	release  %mkrel 4

Name:      mana
Version:   %{version}
Release:   %{release}
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
BuildRoot: %{_tmppath}/%{name}-%{version}
ExcludeArch: %arm %mips

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
rm -rf %{buildroot}
%makeinstall_std

# install mana-prelude.scm for uim
install -d %{buildroot}/%{_datadir}/uim/
install -m 644 mana/mana-prelude.scm %{buildroot}/%{_datadir}/uim/
%multiarch_binaries %{buildroot}%{_bindir}/*-config

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc AUTHORS* ChangeLog* COPYING* NEWS*
%doc README*
%{_bindir}/*
%{_datadir}/uim/*.scm
%{_libdir}/mana/*
%multiarch %multiarch_bindir/*-config


