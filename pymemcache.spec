#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pymemcache
Version  : 1.4.0
Release  : 29
URL      : http://pypi.debian.net/pymemcache/pymemcache-1.4.0.tar.gz
Source0  : http://pypi.debian.net/pymemcache/pymemcache-1.4.0.tar.gz
Summary  : A comprehensive, fast, pure Python memcached client
Group    : Development/Tools
License  : Apache-2.0
Requires: pymemcache-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
pymemcache
==========
.. image:: https://travis-ci.org/pinterest/pymemcache.png
:target: https://travis-ci.org/pinterest/pymemcache

%package python
Summary: python components for the pymemcache package.
Group: Default

%description python
python components for the pymemcache package.


%prep
%setup -q -n pymemcache-1.4.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
