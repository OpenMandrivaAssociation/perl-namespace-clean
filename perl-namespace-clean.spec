%define module   namespace-clean
%define version    0.10
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Keep imports and functions out of your namespace
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/namespace/%{module}-%{version}.tar.gz
BuildRequires: perl(FindBin)
BuildRequires: perl(Scope::Guard)
BuildRequires: perl(Symbol)
BuildRequires: perl(Test::More)
BuildRequires: perl(B::Hooks::EndOfScope)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}
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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
make test

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

