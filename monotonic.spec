#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : monotonic
Version  : 0.3
Release  : 4
URL      : https://pypi.python.org/packages/source/m/monotonic/monotonic-0.3.tar.gz
Source0  : https://pypi.python.org/packages/source/m/monotonic/monotonic-0.3.tar.gz
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
%setup -q -n monotonic-0.3

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
