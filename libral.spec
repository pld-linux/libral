Summary:	Rubrica Addressbook Library
Summary(pl):	Biblioteka do ksi±¿ki adresowej Rubrica
Name:		libral
Version:	0.50
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.berlios.de/libral/%{name}-%{version}.tar.gz
# Source0-md5:	def06a6451d37fe5dea460781b9a3b31
Patch0:		%{name}-includedir.patch
URL:		http://developer.berlios.de/projects/libral/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.9
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibRAL is an address book engine. It allows you to create your
address books and to add personal and company cards to them.

%description -l pl
LibRAL jest silnikiem do ksi±¿ki adresowej. Pozwala stworzyæ
ksi±¿kê adresow± i dodawaæ do niej osobiste oraz firmowe kartki.

%package devel
Summary:	Header files for libral
Summary(pl):	Pliki nag³ówkowe do libral
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for libral library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libral.

%package static
Summary:	Static libral library
Summary(pl):	Statyczna biblioteka libral
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcddb library.

%description static -l pl
Statyczna biblioteka libral.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}

%configure \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libral
%{_libdir}/libral.la
%{_pkgconfigdir}/libral.pc
%{_gtkdocdir}/libRAL

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
