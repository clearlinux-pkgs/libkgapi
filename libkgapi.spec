#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkgapi
Version  : 22.12.2
Release  : 51
URL      : https://download.kde.org/stable/release-service/22.12.2/src/libkgapi-22.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.2/src/libkgapi-22.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.2/src/libkgapi-22.12.2.tar.xz.sig
Summary  : A KDE-based library for accessing various Google services via their public API
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.1 LGPL-3.0
Requires: libkgapi-data = %{version}-%{release}
Requires: libkgapi-lib = %{version}-%{release}
Requires: libkgapi-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : cyrus-sasl-dev
BuildRequires : extra-cmake-modules pkgconfig(libsasl2)
BuildRequires : extra-cmake-modules-data
BuildRequires : kcalendarcore-dev
BuildRequires : kcontacts-dev
BuildRequires : pkgconfig(libsasl2)
BuildRequires : qtwebengine-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

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
%setup -q -n libkgapi-22.12.2
cd %{_builddir}/libkgapi-22.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676862849
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1676862849
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkgapi
cp %{_builddir}/libkgapi-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/libkgapi/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/libkgapi-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkgapi/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libkgapi-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/libkgapi/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/libkgapi-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/libkgapi/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/libkgapi-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/libkgapi/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/libkgapi-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libkgapi/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/libkgapi-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/libkgapi/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/libkgapi-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/libkgapi/5906415d14f11136c25fd1433c5561706103e7cf || :
cp %{_builddir}/libkgapi-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/libkgapi/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/ar/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/bs/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/ca/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/cs/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/da/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/de/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/el/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/es/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/et/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/eu/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/fi/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/fr/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/ga/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/gl/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/hu/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/ia/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/it/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/ja/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/ka/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/kk/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/km/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/ko/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/lt/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/mr/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/nb/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/nds/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/nl/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/nn/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/pl/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/pt/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/ro/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/ru/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/sk/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/sl/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/sr/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/sv/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/tr/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/ug/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/uk/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/libkgapi_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/libkgapi_qt.qm
/usr/share/qlogging-categories5/libkgapi.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim/KGAPI/KGAPI/Account
/usr/include/KPim/KGAPI/KGAPI/AccountInfo
/usr/include/KPim/KGAPI/KGAPI/AccountInfoFetchJob
/usr/include/KPim/KGAPI/KGAPI/AccountManager
/usr/include/KPim/KGAPI/KGAPI/AuthJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/Blog
/usr/include/KPim/KGAPI/KGAPI/Blogger/BlogFetchJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/Comment
/usr/include/KPim/KGAPI/KGAPI/Blogger/CommentApproveJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/CommentDeleteContentJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/CommentDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/CommentFetchJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/Page
/usr/include/KPim/KGAPI/KGAPI/Blogger/PageCreateJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/PageDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/PageFetchJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/PageModifyJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/Post
/usr/include/KPim/KGAPI/KGAPI/Blogger/PostCreateJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/PostDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/PostFetchJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/PostModifyJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/PostPublishJob
/usr/include/KPim/KGAPI/KGAPI/Blogger/PostSearchJob
/usr/include/KPim/KGAPI/KGAPI/Calendar/Calendar
/usr/include/KPim/KGAPI/KGAPI/Calendar/CalendarCreateJob
/usr/include/KPim/KGAPI/KGAPI/Calendar/CalendarDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Calendar/CalendarFetchJob
/usr/include/KPim/KGAPI/KGAPI/Calendar/CalendarModifyJob
/usr/include/KPim/KGAPI/KGAPI/Calendar/Enums
/usr/include/KPim/KGAPI/KGAPI/Calendar/Event
/usr/include/KPim/KGAPI/KGAPI/Calendar/EventCreateJob
/usr/include/KPim/KGAPI/KGAPI/Calendar/EventDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Calendar/EventFetchJob
/usr/include/KPim/KGAPI/KGAPI/Calendar/EventModifyJob
/usr/include/KPim/KGAPI/KGAPI/Calendar/EventMoveJob
/usr/include/KPim/KGAPI/KGAPI/Calendar/FreeBusyQueryJob
/usr/include/KPim/KGAPI/KGAPI/Calendar/Reminder
/usr/include/KPim/KGAPI/KGAPI/Contacts/Contact
/usr/include/KPim/KGAPI/KGAPI/Contacts/ContactCreateJob
/usr/include/KPim/KGAPI/KGAPI/Contacts/ContactDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Contacts/ContactFetchJob
/usr/include/KPim/KGAPI/KGAPI/Contacts/ContactFetchPhotoJob
/usr/include/KPim/KGAPI/KGAPI/Contacts/ContactModifyJob
/usr/include/KPim/KGAPI/KGAPI/Contacts/ContactsGroup
/usr/include/KPim/KGAPI/KGAPI/Contacts/ContactsGroupCreateJob
/usr/include/KPim/KGAPI/KGAPI/Contacts/ContactsGroupDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Contacts/ContactsGroupFetchJob
/usr/include/KPim/KGAPI/KGAPI/Contacts/ContactsGroupModifyJob
/usr/include/KPim/KGAPI/KGAPI/CreateJob
/usr/include/KPim/KGAPI/KGAPI/DeleteJob
/usr/include/KPim/KGAPI/KGAPI/Drive/About
/usr/include/KPim/KGAPI/KGAPI/Drive/AboutFetchJob
/usr/include/KPim/KGAPI/KGAPI/Drive/App
/usr/include/KPim/KGAPI/KGAPI/Drive/AppFetchJob
/usr/include/KPim/KGAPI/KGAPI/Drive/Change
/usr/include/KPim/KGAPI/KGAPI/Drive/ChangeFetchJob
/usr/include/KPim/KGAPI/KGAPI/Drive/ChildReference
/usr/include/KPim/KGAPI/KGAPI/Drive/ChildReferenceCreateJob
/usr/include/KPim/KGAPI/KGAPI/Drive/ChildReferenceDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Drive/ChildReferenceFetchJob
/usr/include/KPim/KGAPI/KGAPI/Drive/Drives
/usr/include/KPim/KGAPI/KGAPI/Drive/DrivesCreateJob
/usr/include/KPim/KGAPI/KGAPI/Drive/DrivesDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Drive/DrivesFetchJob
/usr/include/KPim/KGAPI/KGAPI/Drive/DrivesHideJob
/usr/include/KPim/KGAPI/KGAPI/Drive/DrivesModifyJob
/usr/include/KPim/KGAPI/KGAPI/Drive/DrivesSearchQuery
/usr/include/KPim/KGAPI/KGAPI/Drive/File
/usr/include/KPim/KGAPI/KGAPI/Drive/FileAbstractDataJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileAbstractModifyJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileAbstractResumableJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileAbstractUploadJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileCopyJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileCreateJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileFetchContentJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileFetchJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileModifyJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileResumableCreateJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileResumableModifyJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileSearchQuery
/usr/include/KPim/KGAPI/KGAPI/Drive/FileTouchJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileTrashJob
/usr/include/KPim/KGAPI/KGAPI/Drive/FileUntrashJob
/usr/include/KPim/KGAPI/KGAPI/Drive/ParentReference
/usr/include/KPim/KGAPI/KGAPI/Drive/ParentReferenceCreateJob
/usr/include/KPim/KGAPI/KGAPI/Drive/ParentReferenceDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Drive/ParentReferenceFetchJob
/usr/include/KPim/KGAPI/KGAPI/Drive/Permission
/usr/include/KPim/KGAPI/KGAPI/Drive/PermissionCreateJob
/usr/include/KPim/KGAPI/KGAPI/Drive/PermissionDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Drive/PermissionFetchJob
/usr/include/KPim/KGAPI/KGAPI/Drive/PermissionModifyJob
/usr/include/KPim/KGAPI/KGAPI/Drive/Revision
/usr/include/KPim/KGAPI/KGAPI/Drive/RevisionDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Drive/RevisionFetchJob
/usr/include/KPim/KGAPI/KGAPI/Drive/RevisionModifyJob
/usr/include/KPim/KGAPI/KGAPI/Drive/SearchQuery
/usr/include/KPim/KGAPI/KGAPI/Drive/Teamdrive
/usr/include/KPim/KGAPI/KGAPI/Drive/TeamdriveCreateJob
/usr/include/KPim/KGAPI/KGAPI/Drive/TeamdriveDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Drive/TeamdriveFetchJob
/usr/include/KPim/KGAPI/KGAPI/Drive/TeamdriveModifyJob
/usr/include/KPim/KGAPI/KGAPI/Drive/TeamdriveSearchQuery
/usr/include/KPim/KGAPI/KGAPI/Drive/User
/usr/include/KPim/KGAPI/KGAPI/FetchJob
/usr/include/KPim/KGAPI/KGAPI/Job
/usr/include/KPim/KGAPI/KGAPI/Latitude/Latitude
/usr/include/KPim/KGAPI/KGAPI/Latitude/Location
/usr/include/KPim/KGAPI/KGAPI/Latitude/LocationCreateJob
/usr/include/KPim/KGAPI/KGAPI/Latitude/LocationDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Latitude/LocationFetchHistoryJob
/usr/include/KPim/KGAPI/KGAPI/Latitude/LocationFetchJob
/usr/include/KPim/KGAPI/KGAPI/Maps/StaticMapMarker
/usr/include/KPim/KGAPI/KGAPI/Maps/StaticMapPath
/usr/include/KPim/KGAPI/KGAPI/Maps/StaticMapTileFetchJob
/usr/include/KPim/KGAPI/KGAPI/Maps/StaticMapUrl
/usr/include/KPim/KGAPI/KGAPI/ModifyJob
/usr/include/KPim/KGAPI/KGAPI/Object
/usr/include/KPim/KGAPI/KGAPI/Tasks/Task
/usr/include/KPim/KGAPI/KGAPI/Tasks/TaskCreateJob
/usr/include/KPim/KGAPI/KGAPI/Tasks/TaskDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Tasks/TaskFetchJob
/usr/include/KPim/KGAPI/KGAPI/Tasks/TaskList
/usr/include/KPim/KGAPI/KGAPI/Tasks/TaskListCreateJob
/usr/include/KPim/KGAPI/KGAPI/Tasks/TaskListDeleteJob
/usr/include/KPim/KGAPI/KGAPI/Tasks/TaskListFetchJob
/usr/include/KPim/KGAPI/KGAPI/Tasks/TaskListModifyJob
/usr/include/KPim/KGAPI/KGAPI/Tasks/TaskModifyJob
/usr/include/KPim/KGAPI/KGAPI/Tasks/TaskMoveJob
/usr/include/KPim/KGAPI/KGAPI/Types
/usr/include/KPim/KGAPI/KGAPI/Utils
/usr/include/KPim/KGAPI/kgapi/account.h
/usr/include/KPim/KGAPI/kgapi/accountinfo.h
/usr/include/KPim/KGAPI/kgapi/accountinfofetchjob.h
/usr/include/KPim/KGAPI/kgapi/accountmanager.h
/usr/include/KPim/KGAPI/kgapi/authjob.h
/usr/include/KPim/KGAPI/kgapi/blogger/blog.h
/usr/include/KPim/KGAPI/kgapi/blogger/blogfetchjob.h
/usr/include/KPim/KGAPI/kgapi/blogger/comment.h
/usr/include/KPim/KGAPI/kgapi/blogger/commentapprovejob.h
/usr/include/KPim/KGAPI/kgapi/blogger/commentdeletecontentjob.h
/usr/include/KPim/KGAPI/kgapi/blogger/commentdeletejob.h
/usr/include/KPim/KGAPI/kgapi/blogger/commentfetchjob.h
/usr/include/KPim/KGAPI/kgapi/blogger/kgapiblogger_export.h
/usr/include/KPim/KGAPI/kgapi/blogger/page.h
/usr/include/KPim/KGAPI/kgapi/blogger/pagecreatejob.h
/usr/include/KPim/KGAPI/kgapi/blogger/pagedeletejob.h
/usr/include/KPim/KGAPI/kgapi/blogger/pagefetchjob.h
/usr/include/KPim/KGAPI/kgapi/blogger/pagemodifyjob.h
/usr/include/KPim/KGAPI/kgapi/blogger/post.h
/usr/include/KPim/KGAPI/kgapi/blogger/postcreatejob.h
/usr/include/KPim/KGAPI/kgapi/blogger/postdeletejob.h
/usr/include/KPim/KGAPI/kgapi/blogger/postfetchjob.h
/usr/include/KPim/KGAPI/kgapi/blogger/postmodifyjob.h
/usr/include/KPim/KGAPI/kgapi/blogger/postpublishjob.h
/usr/include/KPim/KGAPI/kgapi/blogger/postsearchjob.h
/usr/include/KPim/KGAPI/kgapi/calendar/calendar.h
/usr/include/KPim/KGAPI/kgapi/calendar/calendarcreatejob.h
/usr/include/KPim/KGAPI/kgapi/calendar/calendardeletejob.h
/usr/include/KPim/KGAPI/kgapi/calendar/calendarfetchjob.h
/usr/include/KPim/KGAPI/kgapi/calendar/calendarmodifyjob.h
/usr/include/KPim/KGAPI/kgapi/calendar/enums.h
/usr/include/KPim/KGAPI/kgapi/calendar/event.h
/usr/include/KPim/KGAPI/kgapi/calendar/eventcreatejob.h
/usr/include/KPim/KGAPI/kgapi/calendar/eventdeletejob.h
/usr/include/KPim/KGAPI/kgapi/calendar/eventfetchjob.h
/usr/include/KPim/KGAPI/kgapi/calendar/eventmodifyjob.h
/usr/include/KPim/KGAPI/kgapi/calendar/eventmovejob.h
/usr/include/KPim/KGAPI/kgapi/calendar/freebusyqueryjob.h
/usr/include/KPim/KGAPI/kgapi/calendar/kgapicalendar_export.h
/usr/include/KPim/KGAPI/kgapi/calendar/reminder.h
/usr/include/KPim/KGAPI/kgapi/contacts/contact.h
/usr/include/KPim/KGAPI/kgapi/contacts/contactcreatejob.h
/usr/include/KPim/KGAPI/kgapi/contacts/contactdeletejob.h
/usr/include/KPim/KGAPI/kgapi/contacts/contactfetchjob.h
/usr/include/KPim/KGAPI/kgapi/contacts/contactfetchphotojob.h
/usr/include/KPim/KGAPI/kgapi/contacts/contactmodifyjob.h
/usr/include/KPim/KGAPI/kgapi/contacts/contactsgroup.h
/usr/include/KPim/KGAPI/kgapi/contacts/contactsgroupcreatejob.h
/usr/include/KPim/KGAPI/kgapi/contacts/contactsgroupdeletejob.h
/usr/include/KPim/KGAPI/kgapi/contacts/contactsgroupfetchjob.h
/usr/include/KPim/KGAPI/kgapi/contacts/contactsgroupmodifyjob.h
/usr/include/KPim/KGAPI/kgapi/contacts/kgapicontacts_export.h
/usr/include/KPim/KGAPI/kgapi/createjob.h
/usr/include/KPim/KGAPI/kgapi/deletejob.h
/usr/include/KPim/KGAPI/kgapi/drive/about.h
/usr/include/KPim/KGAPI/kgapi/drive/aboutfetchjob.h
/usr/include/KPim/KGAPI/kgapi/drive/app.h
/usr/include/KPim/KGAPI/kgapi/drive/appfetchjob.h
/usr/include/KPim/KGAPI/kgapi/drive/change.h
/usr/include/KPim/KGAPI/kgapi/drive/changefetchjob.h
/usr/include/KPim/KGAPI/kgapi/drive/childreference.h
/usr/include/KPim/KGAPI/kgapi/drive/childreferencecreatejob.h
/usr/include/KPim/KGAPI/kgapi/drive/childreferencedeletejob.h
/usr/include/KPim/KGAPI/kgapi/drive/childreferencefetchjob.h
/usr/include/KPim/KGAPI/kgapi/drive/drives.h
/usr/include/KPim/KGAPI/kgapi/drive/drivescreatejob.h
/usr/include/KPim/KGAPI/kgapi/drive/drivesdeletejob.h
/usr/include/KPim/KGAPI/kgapi/drive/drivesfetchjob.h
/usr/include/KPim/KGAPI/kgapi/drive/driveshidejob.h
/usr/include/KPim/KGAPI/kgapi/drive/drivesmodifyjob.h
/usr/include/KPim/KGAPI/kgapi/drive/drivessearchquery.h
/usr/include/KPim/KGAPI/kgapi/drive/file.h
/usr/include/KPim/KGAPI/kgapi/drive/fileabstractdatajob.h
/usr/include/KPim/KGAPI/kgapi/drive/fileabstractmodifyjob.h
/usr/include/KPim/KGAPI/kgapi/drive/fileabstractresumablejob.h
/usr/include/KPim/KGAPI/kgapi/drive/fileabstractuploadjob.h
/usr/include/KPim/KGAPI/kgapi/drive/filecopyjob.h
/usr/include/KPim/KGAPI/kgapi/drive/filecreatejob.h
/usr/include/KPim/KGAPI/kgapi/drive/filedeletejob.h
/usr/include/KPim/KGAPI/kgapi/drive/filefetchcontentjob.h
/usr/include/KPim/KGAPI/kgapi/drive/filefetchjob.h
/usr/include/KPim/KGAPI/kgapi/drive/filemodifyjob.h
/usr/include/KPim/KGAPI/kgapi/drive/fileresumablecreatejob.h
/usr/include/KPim/KGAPI/kgapi/drive/fileresumablemodifyjob.h
/usr/include/KPim/KGAPI/kgapi/drive/filesearchquery.h
/usr/include/KPim/KGAPI/kgapi/drive/filetouchjob.h
/usr/include/KPim/KGAPI/kgapi/drive/filetrashjob.h
/usr/include/KPim/KGAPI/kgapi/drive/fileuntrashjob.h
/usr/include/KPim/KGAPI/kgapi/drive/kgapidrive_export.h
/usr/include/KPim/KGAPI/kgapi/drive/parentreference.h
/usr/include/KPim/KGAPI/kgapi/drive/parentreferencecreatejob.h
/usr/include/KPim/KGAPI/kgapi/drive/parentreferencedeletejob.h
/usr/include/KPim/KGAPI/kgapi/drive/parentreferencefetchjob.h
/usr/include/KPim/KGAPI/kgapi/drive/permission.h
/usr/include/KPim/KGAPI/kgapi/drive/permissioncreatejob.h
/usr/include/KPim/KGAPI/kgapi/drive/permissiondeletejob.h
/usr/include/KPim/KGAPI/kgapi/drive/permissionfetchjob.h
/usr/include/KPim/KGAPI/kgapi/drive/permissionmodifyjob.h
/usr/include/KPim/KGAPI/kgapi/drive/revision.h
/usr/include/KPim/KGAPI/kgapi/drive/revisiondeletejob.h
/usr/include/KPim/KGAPI/kgapi/drive/revisionfetchjob.h
/usr/include/KPim/KGAPI/kgapi/drive/revisionmodifyjob.h
/usr/include/KPim/KGAPI/kgapi/drive/searchquery.h
/usr/include/KPim/KGAPI/kgapi/drive/teamdrive.h
/usr/include/KPim/KGAPI/kgapi/drive/teamdrivecreatejob.h
/usr/include/KPim/KGAPI/kgapi/drive/teamdrivedeletejob.h
/usr/include/KPim/KGAPI/kgapi/drive/teamdrivefetchjob.h
/usr/include/KPim/KGAPI/kgapi/drive/teamdrivemodifyjob.h
/usr/include/KPim/KGAPI/kgapi/drive/teamdrivesearchquery.h
/usr/include/KPim/KGAPI/kgapi/drive/user.h
/usr/include/KPim/KGAPI/kgapi/fetchjob.h
/usr/include/KPim/KGAPI/kgapi/job.h
/usr/include/KPim/KGAPI/kgapi/kgapicore_export.h
/usr/include/KPim/KGAPI/kgapi/latitude/kgapilatitude_export.h
/usr/include/KPim/KGAPI/kgapi/latitude/latitude.h
/usr/include/KPim/KGAPI/kgapi/latitude/location.h
/usr/include/KPim/KGAPI/kgapi/latitude/locationcreatejob.h
/usr/include/KPim/KGAPI/kgapi/latitude/locationdeletejob.h
/usr/include/KPim/KGAPI/kgapi/latitude/locationfetchhistoryjob.h
/usr/include/KPim/KGAPI/kgapi/latitude/locationfetchjob.h
/usr/include/KPim/KGAPI/kgapi/maps/kgapimaps_export.h
/usr/include/KPim/KGAPI/kgapi/maps/staticmapmarker.h
/usr/include/KPim/KGAPI/kgapi/maps/staticmappath.h
/usr/include/KPim/KGAPI/kgapi/maps/staticmaptilefetchjob.h
/usr/include/KPim/KGAPI/kgapi/maps/staticmapurl.h
/usr/include/KPim/KGAPI/kgapi/modifyjob.h
/usr/include/KPim/KGAPI/kgapi/object.h
/usr/include/KPim/KGAPI/kgapi/tasks/kgapitasks_export.h
/usr/include/KPim/KGAPI/kgapi/tasks/task.h
/usr/include/KPim/KGAPI/kgapi/tasks/taskcreatejob.h
/usr/include/KPim/KGAPI/kgapi/tasks/taskdeletejob.h
/usr/include/KPim/KGAPI/kgapi/tasks/taskfetchjob.h
/usr/include/KPim/KGAPI/kgapi/tasks/tasklist.h
/usr/include/KPim/KGAPI/kgapi/tasks/tasklistcreatejob.h
/usr/include/KPim/KGAPI/kgapi/tasks/tasklistdeletejob.h
/usr/include/KPim/KGAPI/kgapi/tasks/tasklistfetchjob.h
/usr/include/KPim/KGAPI/kgapi/tasks/tasklistmodifyjob.h
/usr/include/KPim/KGAPI/kgapi/tasks/taskmodifyjob.h
/usr/include/KPim/KGAPI/kgapi/tasks/taskmovejob.h
/usr/include/KPim/KGAPI/kgapi/types.h
/usr/include/KPim/KGAPI/kgapi/utils.h
/usr/include/KPim/kgapi_version.h
/usr/lib64/cmake/KPimGAPI/KPimGAPIConfig.cmake
/usr/lib64/cmake/KPimGAPI/KPimGAPIConfigVersion.cmake
/usr/lib64/cmake/KPimGAPI/KPimGAPITargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPimGAPI/KPimGAPITargets.cmake
/usr/lib64/libKPimGAPIBlogger.so
/usr/lib64/libKPimGAPICalendar.so
/usr/lib64/libKPimGAPIContacts.so
/usr/lib64/libKPimGAPICore.so
/usr/lib64/libKPimGAPIDrive.so
/usr/lib64/libKPimGAPILatitude.so
/usr/lib64/libKPimGAPIMaps.so
/usr/lib64/libKPimGAPITasks.so
/usr/lib64/qt5/mkspecs/modules/qt_KGAPIBlogger.pri
/usr/lib64/qt5/mkspecs/modules/qt_KGAPICalendar.pri
/usr/lib64/qt5/mkspecs/modules/qt_KGAPIContacts.pri
/usr/lib64/qt5/mkspecs/modules/qt_KGAPICore.pri
/usr/lib64/qt5/mkspecs/modules/qt_KGAPIDrive.pri
/usr/lib64/qt5/mkspecs/modules/qt_KGAPILatitude.pri
/usr/lib64/qt5/mkspecs/modules/qt_KGAPIMaps.pri
/usr/lib64/qt5/mkspecs/modules/qt_KGAPITasks.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKPimGAPIBlogger.so.5
/usr/lib64/libKPimGAPIBlogger.so.5.22.2
/usr/lib64/libKPimGAPICalendar.so.5
/usr/lib64/libKPimGAPICalendar.so.5.22.2
/usr/lib64/libKPimGAPIContacts.so.5
/usr/lib64/libKPimGAPIContacts.so.5.22.2
/usr/lib64/libKPimGAPICore.so.5
/usr/lib64/libKPimGAPICore.so.5.22.2
/usr/lib64/libKPimGAPIDrive.so.5
/usr/lib64/libKPimGAPIDrive.so.5.22.2
/usr/lib64/libKPimGAPILatitude.so.5
/usr/lib64/libKPimGAPILatitude.so.5.22.2
/usr/lib64/libKPimGAPIMaps.so.5
/usr/lib64/libKPimGAPIMaps.so.5.22.2
/usr/lib64/libKPimGAPITasks.so.5
/usr/lib64/libKPimGAPITasks.so.5.22.2
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
/usr/share/package-licenses/libkgapi/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/libkgapi/e458941548e0864907e654fa2e192844ae90fc32
