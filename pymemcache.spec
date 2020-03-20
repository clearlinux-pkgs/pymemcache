#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pymemcache
Version  : 3.0.1
Release  : 49
URL      : https://files.pythonhosted.org/packages/10/e2/8135ad4945b2a84b8f5bfe60d0cc74dd4ffdc7e2e6cee503f4703e95f2cf/pymemcache-3.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/10/e2/8135ad4945b2a84b8f5bfe60d0cc74dd4ffdc7e2e6cee503f4703e95f2cf/pymemcache-3.0.1.tar.gz
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
pymemcache
==========
.. image:: https://img.shields.io/pypi/v/pymemcache.svg
:target: https://pypi.python.org/pypi/pymemcache

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
%setup -q -n pymemcache-3.0.1
cd %{_builddir}/pymemcache-3.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584735734
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pymemcache
cp %{_builddir}/pymemcache-3.0.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pymemcache/2b8b815229aa8a61e483fb4ba0588b8b6c491890
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
