%define	modname	Glib-Object-Introspection
%define	modver	0.045

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	2

Summary:	Dynamically create Perl language bindings
License:	LGPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Glib/%{modname}-%{modver}.tar.gz
Patch0:		Glib-Object-Introspection-0.022-workaround-libffi-pkgconfig-crap.patch

BuildRequires:	perl(ExtUtils::Depends) >= 0.300.0
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::PkgConfig) >= 1.0.0
BuildRequires:	perl(Glib) >= 1.270.0
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(gobject-introspection-1.0)
# For tests:
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	perl(Cairo::GObject)
# (tv) t/00-basic-types.t line 51 failed with C locale
BuildRequires:	locales-en
Requires:	perl(Glib) >= 1.270.0

%description
To allow Glib::Object::Introspection to create bindings for a library, it
must have installed a typelib file, for example
'$prefix/lib/girepository-1.0/Gtk-3.0.typelib'. In your code you then
simply call 'Glib::Object::Introspection->setup' to set everything up. This
method takes a couple of key-value pairs as arguments. These three are
mandatory:

* basename => $basename

  The basename of the library that should be wrapped. If your typelib is
  called 'Gtk-3.0.typelib', then the basename is 'Gtk'.

%prep
%setup -q -n %{modname}-%{modver}
%apply_patches

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
exit 0
LC_ALL=en_US.UTF-8 make test

%install
%makeinstall_std

%files
%doc LICENSE META.json META.yml MYMETA.yml NEWS README
%{_bindir}/perli11ndoc
%{_mandir}/man3/*
%{perl_vendorlib}/*
