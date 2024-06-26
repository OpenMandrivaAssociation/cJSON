%define major 1
%define libname %mklibname %{name}
%define oldlibname %mklibname %{name} 1
%define devname %mklibname %{name} -d

Summary:	Ultralightweight JSON parser in ANSI C
Name:		cjson
Version:	1.7.18
Release:	1
License:	MIT
Group:		System/Libraries
URL:		https://github.com/DaveGamble/cJSON
Source0:	%{url}/archive/refs/tags/v%{version}/cJSON-%{version}.tar.gz
Patch0:		feat-add-cJSON_GetErrorPos.patch

BuildRequires:	cmake

%description
cJSON aims to be the dumbest possible parser
that you can get your job done with. It's a
single file of C, and a single header file.

As a library, cJSON exists to take away as much
legwork as it can, but not get in your way.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
%rename %{oldlibname}
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the %{realname}
runtime libraries.

%package -n %{devname}
Summary:	%{summary}
Group:		%{group}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the %{realname} development
headers and libraries.

%prep
%autosetup -p1 -n cJSON-%{version}

%build
%cmake \
	-DENABLE_CJSON_TEST=OFF \
	-DENABLE_CJSON_UTILS=ON

%make_build

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/lib%{name}*.so.%{major}*

%files -n %{devname}
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}
%{_libdir}/cmake/cJSON
%{_libdir}/pkgconfig/lib%{name}*
