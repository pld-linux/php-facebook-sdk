%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	PHP SDK for the Facebook API
Name:		php-facebook-sdk
Version:	2.0.2
Release:	0.8
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	http://github.com/facebook/php-sdk/tarball/v%{version}
# Source0-md5:	5f8e8c32ae8b4458db65754bc38770d2
URL:		http://github.com/facebook/php-sdk/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-curl
Requires:	php-date
Requires:	php-json
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	%{?_noautophpreq} %{?_noautopeardep}

%description
Facebook Athenaeum provides libraries an easy to implement Facebook
application to extend library resources to students in Facebook. The
application is easily customized for your institution and includes an
integrated RSS reader, search tools, and a friend locator that allows
Facebook users to record their location in the library so their
friends can find them.

%prep
%setup -qc
mv facebook-php-sdk-*/* .
mv readme.md README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a src/facebook.php $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/facebook.php
