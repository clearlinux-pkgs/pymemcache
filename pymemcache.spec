#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pymemcache
Version  : 2.0.0
Release  : 34
URL      : https://files.pythonhosted.org/packages/2e/be/cecec907200c42078aa584406f7d05082a4855dc1d2d7d8099afb0a14065/pymemcache-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/2e/be/cecec907200c42078aa584406f7d05082a4855dc1d2d7d8099afb0a14065/pymemcache-2.0.0.tar.gz
Summary  : A comprehensive, fast, pure Python memcached client
Group    : Development/Tools
License  : Apache-2.0
Requires: pymemcache-python3
Requires: pymemcache-license
Requires: pymemcache-python
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
Requires: pymemcache-python3

%description python
python components for the pymemcache package.


%package python3
Summary: python3 components for the pymemcache package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pymemcache package.


%prep
%setup -q -n pymemcache-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536975422
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pymemcache
cp LICENSE.txt %{buildroot}/usr/share/doc/pymemcache/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/pymemcache/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
