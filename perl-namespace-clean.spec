%define upstream_name    namespace-clean
%define upstream_version 0.24

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	Keep imports and functions out of your namespace
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/namespace/namespace-clean-%{upstream_version}.tar.gz

BuildRequires:	perl(B::Hooks::EndOfScope)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Package::Stash)
BuildRequires:	perl(Scope::Guard)
BuildRequires:	perl(Sub::Identify)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Implementation)
BuildRequires:	perl-devel

BuildArch:	noarch

Provides:	perl(namespace::clean)

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

# %check
# %make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.200.0-2mdv2011.0
+ Revision: 657864
- rebuild for updated spec-helper

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.200.0-1
+ Revision: 634015
- new version

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2011.0
+ Revision: 551923
- adding missing buildrequires:
- update to 0.18

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.1
+ Revision: 526462
- update to 0.14

* Mon Jan 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.1
+ Revision: 492956
- update to 0.13

* Thu Jan 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 491211
- adding missing buildrequires:
- update to 0.12

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 404047
- rebuild using %%perl_convert_version

* Wed Mar 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.1
+ Revision: 348397
- update to new version 0.11

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2009.1
+ Revision: 343835
- new version

* Thu Dec 04 2008 Jérôme Quelin <jquelin@mandriva.org> 0.09-2mdv2009.1
+ Revision: 309964
- force provides, since it's all lowercase and mandriva's perl extractor
  filters those out

* Thu Oct 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.1
+ Revision: 296825
- new version

* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2009.0
+ Revision: 236343
- import perl-namespace-clean


* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2009.0
- initial mdv release, generated with cpan2dist

