#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : diff-match-patch
Version  : 20200713
Release  : 7
URL      : https://files.pythonhosted.org/packages/f0/1e/48ba888757d3f63ff35536e3e73e05c8a20d701e2b4fcbe4b17c29a2408d/diff-match-patch-20200713.tar.gz
Source0  : https://files.pythonhosted.org/packages/f0/1e/48ba888757d3f63ff35536e3e73e05c8a20d701e2b4fcbe4b17c29a2408d/diff-match-patch-20200713.tar.gz
Summary  : Repackaging of Google's Diff Match and Patch libraries. Offers robust algorithms to perform the operations required for synchronizing plain text.
Group    : Development/Tools
License  : Apache-2.0
Requires: diff-match-patch-license = %{version}-%{release}
Requires: diff-match-patch-python = %{version}-%{release}
Requires: diff-match-patch-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : setuptools

%description
Google's [Diff Match and Patch][DMP] library, packaged for modern Python.

%package license
Summary: license components for the diff-match-patch package.
Group: Default

%description license
license components for the diff-match-patch package.


%package python
Summary: python components for the diff-match-patch package.
Group: Default
Requires: diff-match-patch-python3 = %{version}-%{release}

%description python
python components for the diff-match-patch package.


%package python3
Summary: python3 components for the diff-match-patch package.
Group: Default
Requires: python3-core
Provides: pypi(diff_match_patch)

%description python3
python3 components for the diff-match-patch package.


%prep
%setup -q -n diff-match-patch-20200713
cd %{_builddir}/diff-match-patch-20200713

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594673714
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/diff-match-patch
cp %{_builddir}/diff-match-patch-20200713/LICENSE %{buildroot}/usr/share/package-licenses/diff-match-patch/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/diff-match-patch/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
