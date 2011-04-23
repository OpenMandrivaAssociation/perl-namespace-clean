%define upstream_name    namespace-clean
%define upstream_version 0.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Keep imports and functions out of your namespace
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/namespace/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(B::Hooks::EndOfScope)
BuildRequires: perl(FindBin)
BuildRequires: perl(Package::Stash)
BuildRequires: perl(Scope::Guard)
BuildRequires: perl(Sub::Identify)
BuildRequires: perl(Sub::Name)
BuildRequires: perl(Symbol)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Provides:   perl(namespace::clean)

%description
When you define a function, or import one, into a Perl package, it will
naturally also be available as a method. This does not per se cause
problems, but it can complicate subclassing and, for example, plugin
classes that are included via multiple inheritance by loading them as
base classes.

The 'namespace::clean' pragma will remove all previously declared or
imported symbols at the end of the current package's compile cycle.
Functions called in the package itself will still be bound by their
name, but they won't show up as methods on your class or instances.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
