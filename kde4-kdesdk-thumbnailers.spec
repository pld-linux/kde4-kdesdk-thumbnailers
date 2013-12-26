#
# TODO:
# - add man files
#
%define		orgname		kdesdk-thumbnailers
%define		_state		stable
%define		qtver		4.8.1

Summary:	Thumbnailers
Name:		kde4-%{orgname}
Version:	4.12.0
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	635a7d75a327d25bdf1715c92dc401ff
URL:		http://www.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScriptTools-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	db-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-mime-info
Obsoletes:	kde4-kdesdk-strigi-analyzer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thumbnailers.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/pothumbnail.so
%{_datadir}/config.kcfg/pocreatorsettings.kcfg
%{_datadir}/kde4/services/pothumbnail.desktop
