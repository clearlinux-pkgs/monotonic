#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE70ABDAEA89D5A07 (ori@wikimedia.org)
#
Name     : monotonic
Version  : 1.5
Release  : 24
URL      : https://files.pythonhosted.org/packages/19/c1/27f722aaaaf98786a1b338b78cf60960d9fe4849825b071f4e300da29589/monotonic-1.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/19/c1/27f722aaaaf98786a1b338b78cf60960d9fe4849825b071f4e300da29589/monotonic-1.5.tar.gz
Source99 : https://files.pythonhosted.org/packages/19/c1/27f722aaaaf98786a1b338b78cf60960d9fe4849825b071f4e300da29589/monotonic-1.5.tar.gz.asc
Summary  : An implementation of time.monotonic() for Python 2 & < 3.3
Group    : Development/Tools
License  : Apache-2.0
Requires: monotonic-python3
Requires: monotonic-license
Requires: monotonic-python
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
monotonic
        ~~~~~~~~~
        
        This module provides a ``monotonic()`` function which returns the
        value (in fractional seconds) of a clock which never goes backwards.
        
        On Python 3.3 or newer, ``monotonic`` will be an alias of
        ``time.monotonic`` from the standard library. On older versions,

%package license
Summary: license components for the monotonic package.
Group: Default

%description license
license components for the monotonic package.


%package python
Summary: python components for the monotonic package.
Group: Default
Requires: monotonic-python3

%description python
python components for the monotonic package.


%package python3
Summary: python3 components for the monotonic package.
Group: Default
Requires: python3-core

%description python3
python3 components for the monotonic package.


%prep
%setup -q -n monotonic-1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532241564
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/monotonic
cp LICENSE %{buildroot}/usr/share/doc/monotonic/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/monotonic/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
