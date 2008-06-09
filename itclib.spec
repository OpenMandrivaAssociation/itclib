%define	name		itclib
%define	version		1.1.2
%define	release		 %mkrel 10
%define	lib_name_orig	lib%{name}
%define	lib_major	0
%define	lib_name	%mklibname %{name} %{lib_major}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.derkarl.org/itc/%{name}-%{version}.tar.bz2
Patch0:		%{name}-1.1.2-gcc3.3-fix.patch.bz2
License:	LGPL
Group:		System/Libraries
URL:		http://www.derkarl.org/itc/
Summary:	Powerful C++ thread library
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	flex

%description
Inter-Thread Communication (ITC) aims to make it exceedingly easy to 
call functions in other threads. The lexer does all the work, so just 
run the lexer on your headers, then call the stub functions. In addition, 
it also provides a complete threading API, with the four threading 
primitives and a high speed threadsafe FIFO class.

%package -n	%{lib_name}
Summary:	Powerful C++ thread library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	%{lib_name_orig}2
Obsoletes:      %{lib_name_orig}2

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with itclib.

%package -n	%{lib_name}-devel
Summary:	Headers to develop itc-based applications
Group:		Development/C++
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{lib_name_orig}2-devel
Obsoletes:	%{lib_name_orig}2-devel

%description -n	%{lib_name}-devel
These are the header files, and itc preprocessor for developing
itc-based applications. 

%package -n	%{lib_name}-static-devel
Summary:	Static libraries to statically link itc-based applications
Group:		Development/C++
Requires:	%{lib_name}-devel = %{version}
Provides:	%{lib_name_orig}-static-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n	%{lib_name}-static-devel
These are static libraries needed to build statically linked
itc-based programs.

%prep
%setup -q
%patch0 -p1 -b .orig

%build
CXXFLAGS="$RPM_OPT_FLAGS -fpermissive" \
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
 
%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{lib_name}
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README
%{_libdir}/lib*.so.*


%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_bindir}/itcproc
%{_includedir}/itclib/
%{_libdir}/lib*.so

%files -n %{lib_name}-static-devel
%defattr(-,root,root)
%{_libdir}/lib*.a
%{_libdir}/lib*.la

