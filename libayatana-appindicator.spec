Name:           libayatana-appindicator
Version:        0.5.92
Release:        1%{?dist}
Summary:        Ayatana Application Indicators shared library
License:        GPLv3 or LGPLv3 or LGPLv2.1
URL:            https://github.com/AyatanaIndicators/%{name}

Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-build.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(ayatana-indicator3-0.4)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
Ayatana Indicators shared library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Ayatana Indicators shared library.

This package contains development files for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake \
    -DENABLE_BINDINGS_MONO=OFF \
    -DENABLE_BINDINGS_VALA=OFF
%cmake_build

%install
%cmake_install

%files
%license COPYING*
%doc ChangeLog NEWS README
%{_datadir}/gir-1.0/AyatanaAppIndicator3-0.1.gir
%{_libdir}/%{name}3.so.1
%{_libdir}/%{name}3.so.1.0.0
%{_libdir}/girepository-1.0/AyatanaAppIndicator3-0.1.typelib

%files devel
%{_includedir}/%{name}3-0.1/*
%{_libdir}/%{name}3.so
%{_libdir}/pkgconfig/ayatana-appindicator3-0.1.pc

%changelog
* Fri Sep 15 2023 Simone Caronni <negativo17@gmail.com> - 0.5.92-1
- First build.
