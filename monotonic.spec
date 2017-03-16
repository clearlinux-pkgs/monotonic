#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE70ABDAEA89D5A07 (ori@wikimedia.org)
#
Name     : monotonic
Version  : 1.3
Release  : 21
URL      : http://pypi.debian.net/monotonic/monotonic-1.3.tar.gz
Source0  : http://pypi.debian.net/monotonic/monotonic-1.3.tar.gz
Source99 : http://pypi.debian.net/monotonic/monotonic-1.3.tar.gz.asc
Summary  : An implementation of time.monotonic() for Python 2 & < 3.3
Group    : Development/Tools
License  : Apache-2.0
Requires: monotonic-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the monotonic package.
Group: Default

%description python
python components for the monotonic package.


%prep
%setup -q -n monotonic-1.3

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489679488
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489679488
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
