#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-INET6Glue
Version  : 0.603
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/S/SU/SULLR/Net-INET6Glue-0.603.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SU/SULLR/Net-INET6Glue-0.603.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-inet6glue-perl/libnet-inet6glue-perl_0.603-2.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Net-INET6Glue-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Net::INET6Glue is a hack to make more of Perl IPv6 able.
This is partly done by replacing IO::Socket::INET with IO::Socket::INET6
and by adding IPv6 Protocol functionality to Net::FTP.
Works for Net::SMTP, LWP, Net::FTP and probably others too.

%package dev
Summary: dev components for the perl-Net-INET6Glue package.
Group: Development
Provides: perl-Net-INET6Glue-devel = %{version}-%{release}

%description dev
dev components for the perl-Net-INET6Glue package.


%package license
Summary: license components for the perl-Net-INET6Glue package.
Group: Default

%description license
license components for the perl-Net-INET6Glue package.


%prep
%setup -q -n Net-INET6Glue-0.603
cd ..
%setup -q -T -D -n Net-INET6Glue-0.603 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Net-INET6Glue-0.603/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-INET6Glue
cp COPYRIGHT %{buildroot}/usr/share/package-licenses/perl-Net-INET6Glue/COPYRIGHT
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Net/INET6Glue.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/INET6Glue/FTP.pm
/usr/lib/perl5/vendor_perl/5.28.0/Net/INET6Glue/INET_is_INET6.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::INET6Glue.3
/usr/share/man/man3/Net::INET6Glue::FTP.3
/usr/share/man/man3/Net::INET6Glue::INET_is_INET6.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-INET6Glue/COPYRIGHT
