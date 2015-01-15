Name:      mana
Version:   0.2.1
Release:   10
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
BuildRequires: ocaml-camlp4-devel
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


