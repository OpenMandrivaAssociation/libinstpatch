%define name    libinstpatch
%define version 1.0.0
%define release %mkrel 1

%define lib_major       0
%define lib_name        %mklibname instpatch %{lib_major} 
%define lib_name_devel  %mklibname instpatch -d

Name:           %{name} 
Summary:        Library for processing Music Instrument patch files
Version:        %{version} 
Release:        %{release}
URL:            http://swami.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/swami/%{name}-%{version}.tar.gz
License:        LGPL
Group:          System/Libraries

BuildRequires:  python-gobject-devel
BuildRequires:  python-devel
BuildRequires:  sndfile-devel
BuildRequires:  gtk-doc
Requires:       python
Requires:       pygtk2.0
BuildRoot:      %_tmppath/%{name}-root

%description
Library for processing digital sample based MIDI instrument "patch" files.
The types of files libInstPatch supports are used for creating
instrument sounds for wavetable synthesis. libInstPatch provides
an object framework (based on GObject) to load patch files into,
which can then be edited, converted, compressed and saved.

#-----------------------------------
%package -n instpatch

Summary:        Utilities related to the libinstpatch library
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n instpatch
Utilities related to the libinstpatch library. LibInstPatch contains
tools for processing digital sample based MIDI instrument "patch" files.
The types of files libInstPatch supports are used for creating
instrument sounds for wavetable synthesis. libInstPatch provides
an object framework (based on GObject) to load patch files into,
which can then be edited, converted, compressed and saved.

%files -n instpatch
%defattr(-,root,root,-)
%{_bindir}/riff_dump
%{python_sitelib}/ipatchmodule.*
%{_datadir}/pygtk/2.0/defs/ipatch*.defs

#-----------------------------------
%package -n %{lib_name}

Summary:        Library for processing music instrument patch files
Group:          System/Libraries
Requires:       python
Requires:       pygtk2.0
Requires:       instpatch = %{version}
Provides:       %{name} = %{version}-%{release}

%description -n %{lib_name}
Library for processing digital sample based MIDI instrument "patch" files.
The types of files libInstPatch supports are used for creating
instrument sounds for wavetable synthesis. libInstPatch provides
an object framework (based on GObject) to load patch files into,
which can then be edited, converted, compressed and saved.

%files -n %{lib_name}
%defattr(-,root,root,-)
%doc AUTHORS README
%{_libdir}/%{name}-1.0.so.*

#-----------------------------------
%package -n %{lib_name_devel}
Summary:        Libinstpatch development headers
Group:          System/Libraries
Requires:       %{name} = %{version}
Provides:       instpatch-devel = %{version}-%{release}

%description -n %{lib_name_devel}
Header files needed to build applications against libinstpatch.

%files -n %{lib_name_devel}
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/%{name}
%dir %{_includedir}/%{name}-1.0/%{name}
%{_includedir}/%{name}-1.0/%{name}/*.h
%{_libdir}/%{name}-1.0.so
%{_libdir}/%{name}-1.0.la
%{_libdir}/pkgconfig/%{name}-1.0.pc

#-----------------------------------
%prep
%setup -q -n %{name}-%{version}

%build
#autogen necessary to avoid unlinked cmath lib
./autogen.sh
%configure --enable-static=no
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%ifarch x86_64
install -d %{buildroot}%{python_sitelib}
mv %{buildroot}%{_prefix}/%_lib/python%{python_version}/site-packages/* %{buildroot}%{python_sitelib}/ 
%endif

%clean
rm -rf %{buildroot}
