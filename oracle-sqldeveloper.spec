Summary:	Oracle SQL Developer
Name:		oracle-sqldeveloper
Version:	4.0.2.15.21
Release:	1
License:	OTN (proprietary, non-distributable)
Group:		Applications/Databases
Source0:	http://download.oracle.com/otn/java/sqldeveloper/sqldeveloper-%{version}-1.noarch.rpm
# NoSource0-md5:	04b21ac56a475c9c0773531808e51d4d
URL:		http://www.oracle.com/technetwork/developer-tools/sql-developer/
BuildRequires:	rpm-utils
Patch0:		desktop.patch
Patch1:		java-home.patch
Requires:	desktop-file-utils
Requires:	jpackage-utils
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}

%description
Oracle SQL Developer is a new, free graphical tool that enhances
productivity and simplifies database development tasks. With SQL
Developer, you can browse database objects, run SQL statements and SQL
scripts, and edit and debug PL/SQL statements. You can also run any
number of provided reports, as well as create and save your own.

%prep
%setup -qcT
SOURCE=%{SOURCE0}
V=$(rpm -qp --nodigest --nosignature --qf '%{V}' $SOURCE)
if [ version:$V != version:%{version} ]; then
%{_appdir}/sqldeveloper/exit 1
fi
rpm2cpio $SOURCE | cpio -i -d

mv opt/sqldeveloper .
mv sqldeveloper/*.{html,png,desktop,sh} .
rm sqldeveloper/*.{exe,bat}
rm sqldeveloper/ide/bin/*.exe
rm sqldeveloper/sqldeveloper/bin/*.{bat,exe}
rm sqldeveloper/sqldeveloper/bin/*-Darwin.conf
rm sqldeveloper/sqldeveloper/bin/SQLDeveloperIcons.icns
rm sqldeveloper/view-source-paths.lis

%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -l readme.html $RPM_BUILD_ROOT/cp-test && l=l && rm -f $RPM_BUILD_ROOT/cp-test
cp -a$l sqldeveloper/* $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_bindir}}
cp -p sqldeveloper.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p icon.png $RPM_BUILD_ROOT%{_desktopdir}/sqldeveloper.png
ln -s %{_appdir}/sqldeveloper/bin/sqldeveloper $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sqldeveloper
%{_desktopdir}/sqldeveloper.desktop
%{_desktopdir}/sqldeveloper.png
%dir %{_appdir}
%{_appdir}/ant
%{_appdir}/configuration
%{_appdir}/dataminer
%{_appdir}/dropins
%{_appdir}/dvt
%{_appdir}/equinox
%{_appdir}/external
%{_appdir}/ide
%{_appdir}/javavm
%{_appdir}/jdbc
%{_appdir}/jdev
%{_appdir}/jlib
%{_appdir}/jviews
%{_appdir}/modules
%{_appdir}/netbeans
%{_appdir}/rdbms
%{_appdir}/sleepycat
%{_appdir}/sqlcli
%{_appdir}/sqlj
%{_appdir}/svnkit

%dir %{_appdir}/sqldeveloper
%{_appdir}/sqldeveloper/demo
%{_appdir}/sqldeveloper/doc
%{_appdir}/sqldeveloper/extensions
%{_appdir}/sqldeveloper/lib
%dir %{_appdir}/sqldeveloper/bin
%{_appdir}/sqldeveloper/bin/*.conf
%{_appdir}/sqldeveloper/bin/sdcli
%{_appdir}/sqldeveloper/bin/sdcli.boot
%{_appdir}/sqldeveloper/bin/splash.gif
%{_appdir}/sqldeveloper/bin/splash.png
%attr(755,root,root) %{_appdir}/sqldeveloper/bin/sqldeveloper
%{_appdir}/sqldeveloper/bin/sqldeveloper.boot
%{_appdir}/sqldeveloper/bin/version.properties
