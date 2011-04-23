%define upstream_name    Test-Reporter
%define upstream_version 1.57

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Sends test results to cpan-testers@perl.org
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FileHandle)
BuildRequires: perl(Net::SMTP)
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::Local)
BuildRequires: perl(base)
BuildRequires: perl(constant)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Test::Reporter reports the test results of any given distribution to the
CPAN Testers project. Test::Reporter has wide support for various perl5's
and platforms.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

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
%doc Changes LICENSE META.yml README
%{_bindir}/cpantest
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*


