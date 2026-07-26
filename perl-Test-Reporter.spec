%define upstream_name    Test-Reporter
Name:		perl-%{upstream_name}
Version:	1.62
Release:	2

Summary:	Sends test results to cpan-testers@perl.org
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/cpan-testers/Test-Reporter
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-Reporter-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FileHandle)
BuildRequires:	perl(Net::SMTP)
BuildRequires:	perl(Sys::Hostname)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::Local)
BuildRequires:	perl(base)
BuildRequires:	perl(constant)
BuildArch:	noarch

%description
Test::Reporter reports the test results of any given distribution to the
CPAN Testers project. Test::Reporter has wide support for various perl5's
and platforms.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
# %{_bindir}/cpantest
# %{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.570.0-2mdv2011.0
+ Revision: 657846
- rebuild for updated spec-helper

* Fri Dec 24 2010 Shlomi Fish <shlomif@mandriva.org> 1.570.0-1mdv2011.0
+ Revision: 624631
- import perl-Test-Reporter



