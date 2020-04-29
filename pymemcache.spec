#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pymemcache
Version  : 3.1.1
Release  : 51
URL      : https://files.pythonhosted.org/packages/82/c0/abae731d6a23dadf584e95cbaec3eaae125fdcd441489ae3598fcc125c0a/pymemcache-3.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/82/c0/abae731d6a23dadf584e95cbaec3eaae125fdcd441489ae3598fcc125c0a/pymemcache-3.1.1.tar.gz
Summary  : "A comprehensive, fast, pure Python memcached client"
Group    : Development/Tools
License  : Apache-2.0
Requires: pymemcache-license = %{version}-%{release}
Requires: pymemcache-python = %{version}-%{release}
Requires: pymemcache-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
==========

%package license
Summary: license components for the pymemcache package.
Group: Default

%description license
license components for the pymemcache package.


%package python
Summary: python components for the pymemcache package.
Group: Default
Requires: pymemcache-python3 = %{version}-%{release}

%description python
python components for the pymemcache package.


%package python3
Summary: python3 components for the pymemcache package.
Group: Default
Requires: python3-core
Provides: pypi(pymemcache)
Requires: pypi(six)

%description python3
python3 components for the pymemcache package.


%prep
%setup -q -n pymemcache-3.1.1
cd %{_builddir}/pymemcache-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588133221
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pymemcache
cp %{_builddir}/pymemcache-3.1.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pymemcache/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pymemcache/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
