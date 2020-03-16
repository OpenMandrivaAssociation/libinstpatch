%define name    libinstpatch
%define version 1.1.2
%define release 1

%define lib_major 0
%define lib_api 1.1
%define lib_name        %mklibname instpatch %{lib_api} %{lib_major}
%define lib_name_devel  %mklibname instpatch -d

Name:           %{name}
Summary:        Library for processing Music Instrument patch files
Version:        %{version}
Release:        %{release}
URL:            http://swami.sourceforge.net
Source0:        http://prdownloads.sourceforge.net/swami/%{name}-%{version}.tar.gz
License:        LGPL
Group:          System/Libraries

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  intltool
BuildRequires:  python-gobject3-devel
BuildRequires:  pygtk2.0-devel
BuildRequires:  sndfile-devel
BuildRequires:  audiofile-devel
BuildRequires:  gtk-doc
BuildRequires:	cmake
#Requires:       python
Requires:       pygtk2.0

BuildRoot:      %_tmppath/%{name}-root

%description
Library for processing digital sample based MIDI instrument "patch" files.
The types of files libInstPatch supports are used for creating
instrument sounds for wavetable synthesis. libInstPatch provides
an object framework (based on GObject) to load patch files into,
which can then be edited, converted, compressed and saved.

#-----------------------------------
%package -n %{lib_name}

Summary:        Library for processing music instrument patch files
Group:          System/Libraries
##Requires:       python
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
%doc AUTHORS 
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
#%doc %{_datadir}/gtk-doc/html/%{name}
%dir %{_includedir}/%{name}-2/%{name}
%{_includedir}/%{name}-2/%{name}/*.h
%{_libdir}/%{name}-1.0.so
%{_libdir}/pkgconfig/%{name}-1.0.pc

#-----------------------------------
%prep
%setup -q -n %{name}-%{version}

%build

%cmake

%make_build

%install
rm -rf %{buildroot}
%make_install -C build

#%ifarch x86_64
#install -d %{buildroot}%{python_sitelib}
#mv %{buildroot}%{_prefix}/%_lib/python%{python_version}/site-packages/* %{buildroot}%{python_sitelib}/
#%endif

%clean
rm -rf %{buildroot}


%changelog
* Mon Nov 01 2010 Frank Kober <emuse@mandriva.org> 1.0.0-3mdv2011.0
+ Revision: 591481
- add audiofile-devel BR to provide correct CFLAGS (tnx ahmad again :) )

* Sun Oct 31 2010 Frank Kober <emuse@mandriva.org> 1.0.0-2mdv2011.0
+ Revision: 591246
+ rebuild (emptylog)

* Sun Oct 31 2010 Frank Kober <emuse@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 590973
- use different solution than autoreconf
- fix license, fix group
- fix python site-package path
- import libinstpatch

