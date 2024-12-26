#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkgapi
Version  : 24.12.0
Release  : 77
URL      : https://download.kde.org/stable/release-service/24.12.0/src/libkgapi-24.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.0/src/libkgapi-24.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.0/src/libkgapi-24.12.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : A KDE-based library for accessing various Google services via their public API
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.1 LGPL-3.0
Requires: libkgapi-data = %{version}-%{release}
Requires: libkgapi-lib = %{version}-%{release}
Requires: libkgapi-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : cyrus-sasl-dev
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kcalendarcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kwallet-dev
BuildRequires : pkgconfig(libsasl2)
BuildRequires : qt6base-dev
BuildRequires : qt6webengine-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# LibKGAPI
LibKGAPI (previously called LibKGoogle) is a C++ library that implements APIs for
various Google services.

%package data
Summary: data components for the libkgapi package.
Group: Data

%description data
data components for the libkgapi package.


%package dev
Summary: dev components for the libkgapi package.
Group: Development
Requires: libkgapi-lib = %{version}-%{release}
Requires: libkgapi-data = %{version}-%{release}
Provides: libkgapi-devel = %{version}-%{release}
Requires: libkgapi = %{version}-%{release}

%description dev
dev components for the libkgapi package.


%package lib
Summary: lib components for the libkgapi package.
Group: Libraries
Requires: libkgapi-data = %{version}-%{release}
Requires: libkgapi-license = %{version}-%{release}

%description lib
lib components for the libkgapi package.


%package license
Summary: license components for the libkgapi package.
Group: Default

%description license
license components for the libkgapi package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n libkgapi-24.12.0
cd %{_builddir}/libkgapi-24.12.0
pushd ..
cp -a libkgapi-24.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735172752
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735172752
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkgapi
cp %{_builddir}/libkgapi-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkgapi/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libkgapi-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libkgapi/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/libkgapi-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/libkgapi/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/libkgapi-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/libkgapi/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/libkgapi-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libkgapi/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/libkgapi-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libkgapi/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/libkgapi-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/libkgapi/5906415d14f11136c25fd1433c5561706103e7cf || :
cp %{_builddir}/libkgapi-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/libkgapi/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/ar/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/ast/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/bs/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/da/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/de/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/el/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/es/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/et/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/ga/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/he/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/hu/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/it/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/kk/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/km/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/lv/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/mr/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/nb/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/nds/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/ro/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/sr/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/ta/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/ug/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/libkgapi6_qt.qm
/usr/share/qlogging-categories6/libkgapi.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/KGAPI/KGAPI/Account
/usr/include/KPim6/KGAPI/KGAPI/AccountInfo
/usr/include/KPim6/KGAPI/KGAPI/AccountInfoFetchJob
/usr/include/KPim6/KGAPI/KGAPI/AccountManager
/usr/include/KPim6/KGAPI/KGAPI/AuthJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/Blog
/usr/include/KPim6/KGAPI/KGAPI/Blogger/BlogFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/Comment
/usr/include/KPim6/KGAPI/KGAPI/Blogger/CommentApproveJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/CommentDeleteContentJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/CommentDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/CommentFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/Page
/usr/include/KPim6/KGAPI/KGAPI/Blogger/PageCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/PageDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/PageFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/PageModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/Post
/usr/include/KPim6/KGAPI/KGAPI/Blogger/PostCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/PostDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/PostFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/PostModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/PostPublishJob
/usr/include/KPim6/KGAPI/KGAPI/Blogger/PostSearchJob
/usr/include/KPim6/KGAPI/KGAPI/Calendar/Calendar
/usr/include/KPim6/KGAPI/KGAPI/Calendar/CalendarCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Calendar/CalendarDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Calendar/CalendarFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Calendar/CalendarModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Calendar/Enums
/usr/include/KPim6/KGAPI/KGAPI/Calendar/Event
/usr/include/KPim6/KGAPI/KGAPI/Calendar/EventCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Calendar/EventDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Calendar/EventFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Calendar/EventModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Calendar/EventMoveJob
/usr/include/KPim6/KGAPI/KGAPI/Calendar/FreeBusyQueryJob
/usr/include/KPim6/KGAPI/KGAPI/Calendar/Reminder
/usr/include/KPim6/KGAPI/KGAPI/CreateJob
/usr/include/KPim6/KGAPI/KGAPI/DeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/About
/usr/include/KPim6/KGAPI/KGAPI/Drive/AboutFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/App
/usr/include/KPim6/KGAPI/KGAPI/Drive/AppFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/Change
/usr/include/KPim6/KGAPI/KGAPI/Drive/ChangeFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/ChildReference
/usr/include/KPim6/KGAPI/KGAPI/Drive/ChildReferenceCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/ChildReferenceDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/ChildReferenceFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/Drives
/usr/include/KPim6/KGAPI/KGAPI/Drive/DrivesCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/DrivesDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/DrivesFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/DrivesHideJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/DrivesModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/DrivesSearchQuery
/usr/include/KPim6/KGAPI/KGAPI/Drive/File
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileAbstractDataJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileAbstractModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileAbstractResumableJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileAbstractUploadJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileCopyJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileFetchContentJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileResumableCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileResumableModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileSearchQuery
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileTouchJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileTrashJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/FileUntrashJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/ParentReference
/usr/include/KPim6/KGAPI/KGAPI/Drive/ParentReferenceCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/ParentReferenceDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/ParentReferenceFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/Permission
/usr/include/KPim6/KGAPI/KGAPI/Drive/PermissionCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/PermissionDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/PermissionFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/PermissionModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/Revision
/usr/include/KPim6/KGAPI/KGAPI/Drive/RevisionDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/RevisionFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/RevisionModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/SearchQuery
/usr/include/KPim6/KGAPI/KGAPI/Drive/Teamdrive
/usr/include/KPim6/KGAPI/KGAPI/Drive/TeamdriveCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/TeamdriveDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/TeamdriveFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/TeamdriveModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Drive/TeamdriveSearchQuery
/usr/include/KPim6/KGAPI/KGAPI/Drive/User
/usr/include/KPim6/KGAPI/KGAPI/FetchJob
/usr/include/KPim6/KGAPI/KGAPI/Job
/usr/include/KPim6/KGAPI/KGAPI/Latitude/Latitude
/usr/include/KPim6/KGAPI/KGAPI/Latitude/Location
/usr/include/KPim6/KGAPI/KGAPI/Latitude/LocationCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Latitude/LocationDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Latitude/LocationFetchHistoryJob
/usr/include/KPim6/KGAPI/KGAPI/Latitude/LocationFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Maps/StaticMapMarker
/usr/include/KPim6/KGAPI/KGAPI/Maps/StaticMapPath
/usr/include/KPim6/KGAPI/KGAPI/Maps/StaticMapTileFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Maps/StaticMapUrl
/usr/include/KPim6/KGAPI/KGAPI/ModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Object
/usr/include/KPim6/KGAPI/KGAPI/People/Address
/usr/include/KPim6/KGAPI/KGAPI/People/AgeRangeType
/usr/include/KPim6/KGAPI/KGAPI/People/Biography
/usr/include/KPim6/KGAPI/KGAPI/People/Birthday
/usr/include/KPim6/KGAPI/KGAPI/People/BraggingRights
/usr/include/KPim6/KGAPI/KGAPI/People/CalendarUrl
/usr/include/KPim6/KGAPI/KGAPI/People/ClientData
/usr/include/KPim6/KGAPI/KGAPI/People/ContactGroup
/usr/include/KPim6/KGAPI/KGAPI/People/ContactGroupCreateJob
/usr/include/KPim6/KGAPI/KGAPI/People/ContactGroupDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/People/ContactGroupFetchJob
/usr/include/KPim6/KGAPI/KGAPI/People/ContactGroupMembership
/usr/include/KPim6/KGAPI/KGAPI/People/ContactGroupMetadata
/usr/include/KPim6/KGAPI/KGAPI/People/ContactGroupModifyJob
/usr/include/KPim6/KGAPI/KGAPI/People/CoverPhoto
/usr/include/KPim6/KGAPI/KGAPI/People/DomainMembership
/usr/include/KPim6/KGAPI/KGAPI/People/EmailAddress
/usr/include/KPim6/KGAPI/KGAPI/People/Event
/usr/include/KPim6/KGAPI/KGAPI/People/ExternalId
/usr/include/KPim6/KGAPI/KGAPI/People/FieldMetadata
/usr/include/KPim6/KGAPI/KGAPI/People/FileAs
/usr/include/KPim6/KGAPI/KGAPI/People/Gender
/usr/include/KPim6/KGAPI/KGAPI/People/GroupClientData
/usr/include/KPim6/KGAPI/KGAPI/People/IMClient
/usr/include/KPim6/KGAPI/KGAPI/People/Interest
/usr/include/KPim6/KGAPI/KGAPI/People/Location
/usr/include/KPim6/KGAPI/KGAPI/People/Membership
/usr/include/KPim6/KGAPI/KGAPI/People/MiscKeyword
/usr/include/KPim6/KGAPI/KGAPI/People/Name
/usr/include/KPim6/KGAPI/KGAPI/People/Nickname
/usr/include/KPim6/KGAPI/KGAPI/People/Occupation
/usr/include/KPim6/KGAPI/KGAPI/People/Organization
/usr/include/KPim6/KGAPI/KGAPI/People/Person
/usr/include/KPim6/KGAPI/KGAPI/People/PersonCreateJob
/usr/include/KPim6/KGAPI/KGAPI/People/PersonDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/People/PersonFetchJob
/usr/include/KPim6/KGAPI/KGAPI/People/PersonLocale
/usr/include/KPim6/KGAPI/KGAPI/People/PersonMetadata
/usr/include/KPim6/KGAPI/KGAPI/People/PersonModifyJob
/usr/include/KPim6/KGAPI/KGAPI/People/PersonPhotoDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/People/PersonPhotoUpdateJob
/usr/include/KPim6/KGAPI/KGAPI/People/PhoneNumber
/usr/include/KPim6/KGAPI/KGAPI/People/Photo
/usr/include/KPim6/KGAPI/KGAPI/People/ProfileMetadata
/usr/include/KPim6/KGAPI/KGAPI/People/Relation
/usr/include/KPim6/KGAPI/KGAPI/People/RelationshipInterest
/usr/include/KPim6/KGAPI/KGAPI/People/RelationshipStatus
/usr/include/KPim6/KGAPI/KGAPI/People/Residence
/usr/include/KPim6/KGAPI/KGAPI/People/SIPAddress
/usr/include/KPim6/KGAPI/KGAPI/People/Skill
/usr/include/KPim6/KGAPI/KGAPI/People/Source
/usr/include/KPim6/KGAPI/KGAPI/People/Tagline
/usr/include/KPim6/KGAPI/KGAPI/People/Url
/usr/include/KPim6/KGAPI/KGAPI/People/UserDefined
/usr/include/KPim6/KGAPI/KGAPI/Tasks/Task
/usr/include/KPim6/KGAPI/KGAPI/Tasks/TaskCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Tasks/TaskDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Tasks/TaskFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Tasks/TaskList
/usr/include/KPim6/KGAPI/KGAPI/Tasks/TaskListCreateJob
/usr/include/KPim6/KGAPI/KGAPI/Tasks/TaskListDeleteJob
/usr/include/KPim6/KGAPI/KGAPI/Tasks/TaskListFetchJob
/usr/include/KPim6/KGAPI/KGAPI/Tasks/TaskListModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Tasks/TaskModifyJob
/usr/include/KPim6/KGAPI/KGAPI/Tasks/TaskMoveJob
/usr/include/KPim6/KGAPI/KGAPI/Types
/usr/include/KPim6/KGAPI/KGAPI/Utils
/usr/include/KPim6/KGAPI/kgapi/account.h
/usr/include/KPim6/KGAPI/kgapi/accountinfo.h
/usr/include/KPim6/KGAPI/kgapi/accountinfofetchjob.h
/usr/include/KPim6/KGAPI/kgapi/accountmanager.h
/usr/include/KPim6/KGAPI/kgapi/authjob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/blog.h
/usr/include/KPim6/KGAPI/kgapi/blogger/blogfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/comment.h
/usr/include/KPim6/KGAPI/kgapi/blogger/commentapprovejob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/commentdeletecontentjob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/commentdeletejob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/commentfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/kgapiblogger_export.h
/usr/include/KPim6/KGAPI/kgapi/blogger/page.h
/usr/include/KPim6/KGAPI/kgapi/blogger/pagecreatejob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/pagedeletejob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/pagefetchjob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/pagemodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/post.h
/usr/include/KPim6/KGAPI/kgapi/blogger/postcreatejob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/postdeletejob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/postfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/postmodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/postpublishjob.h
/usr/include/KPim6/KGAPI/kgapi/blogger/postsearchjob.h
/usr/include/KPim6/KGAPI/kgapi/calendar/calendar.h
/usr/include/KPim6/KGAPI/kgapi/calendar/calendarcreatejob.h
/usr/include/KPim6/KGAPI/kgapi/calendar/calendardeletejob.h
/usr/include/KPim6/KGAPI/kgapi/calendar/calendarfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/calendar/calendarmodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/calendar/enums.h
/usr/include/KPim6/KGAPI/kgapi/calendar/event.h
/usr/include/KPim6/KGAPI/kgapi/calendar/eventcreatejob.h
/usr/include/KPim6/KGAPI/kgapi/calendar/eventdeletejob.h
/usr/include/KPim6/KGAPI/kgapi/calendar/eventfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/calendar/eventmodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/calendar/eventmovejob.h
/usr/include/KPim6/KGAPI/kgapi/calendar/freebusyqueryjob.h
/usr/include/KPim6/KGAPI/kgapi/calendar/kgapicalendar_export.h
/usr/include/KPim6/KGAPI/kgapi/calendar/reminder.h
/usr/include/KPim6/KGAPI/kgapi/createjob.h
/usr/include/KPim6/KGAPI/kgapi/deletejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/about.h
/usr/include/KPim6/KGAPI/kgapi/drive/aboutfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/app.h
/usr/include/KPim6/KGAPI/kgapi/drive/appfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/change.h
/usr/include/KPim6/KGAPI/kgapi/drive/changefetchjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/childreference.h
/usr/include/KPim6/KGAPI/kgapi/drive/childreferencecreatejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/childreferencedeletejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/childreferencefetchjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/drives.h
/usr/include/KPim6/KGAPI/kgapi/drive/drivescreatejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/drivesdeletejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/drivesfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/driveshidejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/drivesmodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/drivessearchquery.h
/usr/include/KPim6/KGAPI/kgapi/drive/file.h
/usr/include/KPim6/KGAPI/kgapi/drive/fileabstractdatajob.h
/usr/include/KPim6/KGAPI/kgapi/drive/fileabstractmodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/fileabstractresumablejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/fileabstractuploadjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/filecopyjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/filecreatejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/filedeletejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/filefetchcontentjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/filefetchjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/filemodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/fileresumablecreatejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/fileresumablemodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/filesearchquery.h
/usr/include/KPim6/KGAPI/kgapi/drive/filetouchjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/filetrashjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/fileuntrashjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/kgapidrive_export.h
/usr/include/KPim6/KGAPI/kgapi/drive/parentreference.h
/usr/include/KPim6/KGAPI/kgapi/drive/parentreferencecreatejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/parentreferencedeletejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/parentreferencefetchjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/permission.h
/usr/include/KPim6/KGAPI/kgapi/drive/permissioncreatejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/permissiondeletejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/permissionfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/permissionmodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/revision.h
/usr/include/KPim6/KGAPI/kgapi/drive/revisiondeletejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/revisionfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/revisionmodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/searchquery.h
/usr/include/KPim6/KGAPI/kgapi/drive/teamdrive.h
/usr/include/KPim6/KGAPI/kgapi/drive/teamdrivecreatejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/teamdrivedeletejob.h
/usr/include/KPim6/KGAPI/kgapi/drive/teamdrivefetchjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/teamdrivemodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/drive/teamdrivesearchquery.h
/usr/include/KPim6/KGAPI/kgapi/drive/user.h
/usr/include/KPim6/KGAPI/kgapi/fetchjob.h
/usr/include/KPim6/KGAPI/kgapi/job.h
/usr/include/KPim6/KGAPI/kgapi/kgapicore_export.h
/usr/include/KPim6/KGAPI/kgapi/latitude/kgapilatitude_export.h
/usr/include/KPim6/KGAPI/kgapi/latitude/latitude.h
/usr/include/KPim6/KGAPI/kgapi/latitude/location.h
/usr/include/KPim6/KGAPI/kgapi/latitude/locationcreatejob.h
/usr/include/KPim6/KGAPI/kgapi/latitude/locationdeletejob.h
/usr/include/KPim6/KGAPI/kgapi/latitude/locationfetchhistoryjob.h
/usr/include/KPim6/KGAPI/kgapi/latitude/locationfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/maps/kgapimaps_export.h
/usr/include/KPim6/KGAPI/kgapi/maps/staticmapmarker.h
/usr/include/KPim6/KGAPI/kgapi/maps/staticmappath.h
/usr/include/KPim6/KGAPI/kgapi/maps/staticmaptilefetchjob.h
/usr/include/KPim6/KGAPI/kgapi/maps/staticmapurl.h
/usr/include/KPim6/KGAPI/kgapi/modifyjob.h
/usr/include/KPim6/KGAPI/kgapi/object.h
/usr/include/KPim6/KGAPI/kgapi/people/address.h
/usr/include/KPim6/KGAPI/kgapi/people/agerangetype.h
/usr/include/KPim6/KGAPI/kgapi/people/biography.h
/usr/include/KPim6/KGAPI/kgapi/people/birthday.h
/usr/include/KPim6/KGAPI/kgapi/people/braggingrights.h
/usr/include/KPim6/KGAPI/kgapi/people/calendarurl.h
/usr/include/KPim6/KGAPI/kgapi/people/clientdata.h
/usr/include/KPim6/KGAPI/kgapi/people/contactgroup.h
/usr/include/KPim6/KGAPI/kgapi/people/contactgroupcreatejob.h
/usr/include/KPim6/KGAPI/kgapi/people/contactgroupdeletejob.h
/usr/include/KPim6/KGAPI/kgapi/people/contactgroupfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/people/contactgroupmembership.h
/usr/include/KPim6/KGAPI/kgapi/people/contactgroupmetadata.h
/usr/include/KPim6/KGAPI/kgapi/people/contactgroupmodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/people/coverphoto.h
/usr/include/KPim6/KGAPI/kgapi/people/domainmembership.h
/usr/include/KPim6/KGAPI/kgapi/people/emailaddress.h
/usr/include/KPim6/KGAPI/kgapi/people/event.h
/usr/include/KPim6/KGAPI/kgapi/people/externalid.h
/usr/include/KPim6/KGAPI/kgapi/people/fieldmetadata.h
/usr/include/KPim6/KGAPI/kgapi/people/fileas.h
/usr/include/KPim6/KGAPI/kgapi/people/gender.h
/usr/include/KPim6/KGAPI/kgapi/people/groupclientdata.h
/usr/include/KPim6/KGAPI/kgapi/people/imclient.h
/usr/include/KPim6/KGAPI/kgapi/people/interest.h
/usr/include/KPim6/KGAPI/kgapi/people/kgapipeople_export.h
/usr/include/KPim6/KGAPI/kgapi/people/location.h
/usr/include/KPim6/KGAPI/kgapi/people/membership.h
/usr/include/KPim6/KGAPI/kgapi/people/misckeyword.h
/usr/include/KPim6/KGAPI/kgapi/people/name.h
/usr/include/KPim6/KGAPI/kgapi/people/nickname.h
/usr/include/KPim6/KGAPI/kgapi/people/occupation.h
/usr/include/KPim6/KGAPI/kgapi/people/organization.h
/usr/include/KPim6/KGAPI/kgapi/people/person.h
/usr/include/KPim6/KGAPI/kgapi/people/personcreatejob.h
/usr/include/KPim6/KGAPI/kgapi/people/persondeletejob.h
/usr/include/KPim6/KGAPI/kgapi/people/personfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/people/personlocale.h
/usr/include/KPim6/KGAPI/kgapi/people/personmetadata.h
/usr/include/KPim6/KGAPI/kgapi/people/personmodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/people/personphotodeletejob.h
/usr/include/KPim6/KGAPI/kgapi/people/personphotoupdatejob.h
/usr/include/KPim6/KGAPI/kgapi/people/phonenumber.h
/usr/include/KPim6/KGAPI/kgapi/people/photo.h
/usr/include/KPim6/KGAPI/kgapi/people/profilemetadata.h
/usr/include/KPim6/KGAPI/kgapi/people/relation.h
/usr/include/KPim6/KGAPI/kgapi/people/relationshipinterest.h
/usr/include/KPim6/KGAPI/kgapi/people/relationshipstatus.h
/usr/include/KPim6/KGAPI/kgapi/people/residence.h
/usr/include/KPim6/KGAPI/kgapi/people/sipaddress.h
/usr/include/KPim6/KGAPI/kgapi/people/skill.h
/usr/include/KPim6/KGAPI/kgapi/people/source.h
/usr/include/KPim6/KGAPI/kgapi/people/tagline.h
/usr/include/KPim6/KGAPI/kgapi/people/url.h
/usr/include/KPim6/KGAPI/kgapi/people/userdefined.h
/usr/include/KPim6/KGAPI/kgapi/tasks/kgapitasks_export.h
/usr/include/KPim6/KGAPI/kgapi/tasks/task.h
/usr/include/KPim6/KGAPI/kgapi/tasks/taskcreatejob.h
/usr/include/KPim6/KGAPI/kgapi/tasks/taskdeletejob.h
/usr/include/KPim6/KGAPI/kgapi/tasks/taskfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/tasks/tasklist.h
/usr/include/KPim6/KGAPI/kgapi/tasks/tasklistcreatejob.h
/usr/include/KPim6/KGAPI/kgapi/tasks/tasklistdeletejob.h
/usr/include/KPim6/KGAPI/kgapi/tasks/tasklistfetchjob.h
/usr/include/KPim6/KGAPI/kgapi/tasks/tasklistmodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/tasks/taskmodifyjob.h
/usr/include/KPim6/KGAPI/kgapi/tasks/taskmovejob.h
/usr/include/KPim6/KGAPI/kgapi/types.h
/usr/include/KPim6/KGAPI/kgapi/utils.h
/usr/include/KPim6/KGAPI/kgapi_version.h
/usr/lib64/cmake/KPim6GAPI/KPim6GAPIConfig.cmake
/usr/lib64/cmake/KPim6GAPI/KPim6GAPIConfigVersion.cmake
/usr/lib64/cmake/KPim6GAPI/KPim6GAPITargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6GAPI/KPim6GAPITargets.cmake
/usr/lib64/libKPim6GAPIBlogger.so
/usr/lib64/libKPim6GAPICalendar.so
/usr/lib64/libKPim6GAPICore.so
/usr/lib64/libKPim6GAPIDrive.so
/usr/lib64/libKPim6GAPILatitude.so
/usr/lib64/libKPim6GAPIMaps.so
/usr/lib64/libKPim6GAPIPeople.so
/usr/lib64/libKPim6GAPITasks.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6GAPIBlogger.so.6.3.0
/V3/usr/lib64/libKPim6GAPICalendar.so.6.3.0
/V3/usr/lib64/libKPim6GAPICore.so.6.3.0
/V3/usr/lib64/libKPim6GAPIDrive.so.6.3.0
/V3/usr/lib64/libKPim6GAPILatitude.so.6.3.0
/V3/usr/lib64/libKPim6GAPIMaps.so.6.3.0
/V3/usr/lib64/libKPim6GAPIPeople.so.6.3.0
/V3/usr/lib64/libKPim6GAPITasks.so.6.3.0
/V3/usr/lib64/sasl2/libkdexoauth2.so.3.0.0
/usr/lib64/libKPim6GAPIBlogger.so.6
/usr/lib64/libKPim6GAPIBlogger.so.6.3.0
/usr/lib64/libKPim6GAPICalendar.so.6
/usr/lib64/libKPim6GAPICalendar.so.6.3.0
/usr/lib64/libKPim6GAPICore.so.6
/usr/lib64/libKPim6GAPICore.so.6.3.0
/usr/lib64/libKPim6GAPIDrive.so.6
/usr/lib64/libKPim6GAPIDrive.so.6.3.0
/usr/lib64/libKPim6GAPILatitude.so.6
/usr/lib64/libKPim6GAPILatitude.so.6.3.0
/usr/lib64/libKPim6GAPIMaps.so.6
/usr/lib64/libKPim6GAPIMaps.so.6.3.0
/usr/lib64/libKPim6GAPIPeople.so.6
/usr/lib64/libKPim6GAPIPeople.so.6.3.0
/usr/lib64/libKPim6GAPITasks.so.6
/usr/lib64/libKPim6GAPITasks.so.6.3.0
/usr/lib64/sasl2/libkdexoauth2.so
/usr/lib64/sasl2/libkdexoauth2.so.3
/usr/lib64/sasl2/libkdexoauth2.so.3.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkgapi/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/libkgapi/5906415d14f11136c25fd1433c5561706103e7cf
/usr/share/package-licenses/libkgapi/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/libkgapi/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/libkgapi/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/libkgapi/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/libkgapi/e458941548e0864907e654fa2e192844ae90fc32
