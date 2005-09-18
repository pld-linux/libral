Summary:	Rubrica Addressbook Library
Summary(pl):	Biblioteka do ksi±¿ki adresowej Rubrica
Name:		libral
Version:	0.50
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://download.berlios.de/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	def06a6451d37fe5dea460781b9a3b31
URL:		http://developer.berlios.de/projects/libral
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	libtool
BuildRequires:	libxml2-devel
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibRAL is an address book engine. It allows you to create your
address books and to add personal and company cards to them.

%description -l pl
LibRAL jest silnikiem do ksi±¿ki adresowej. Pozwala tobie stworzyæ
ksi±¿kê adresow± aby dodawaæ do niej osobiste i firmowe kartki.

%package devel
Summary:	Header files for libral
Summary(pl):	Pliki nag³ówkowe do libral
Group:	X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for libral library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libral.

%package static
Summary:	Static libral library
Summary(pl):	Statyczna biblioteka libral
Group:	Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcddb library.

%description static -l pl
Statyczna biblioteka libral.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/{gtk-doc,doc/}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libral-%{version}/libral/*.h
%{_libdir}/libral.la
%{_pkgconfigdir}/libral.pc
%{_gtkdocdir}/libRAL

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
