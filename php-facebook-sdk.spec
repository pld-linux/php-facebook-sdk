#
# Conditional build:
%bcond_with	tests		# build with tests

%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	PHP SDK for the Facebook API
Name:		php-facebook-sdk
Version:	3.0.0
Release:	1
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	http://github.com/facebook/php-sdk/tarball/v%{version}#/%{name}-%{version}.tgz
# Source0-md5:	8bb75cb1c588f66d19df7cb2ea25d1ae
URL:		http://github.com/facebook/php-sdk/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
%if %{with tests}
BuildRequires:	php-PHPUnit >= 3.4
BuildRequires:	php-curl
BuildRequires:	php-hash
BuildRequires:	php-json
BuildRequires:	php-session
%endif
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-curl
Requires:	php-hash
Requires:	php-json
Requires:	php-session
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautopear	pear(base_facebook.php)
%define		_noautoreq	%{?_noautophpreq} %{?_noautopear}

%description
Open Source PHP SDK that allows you to utilize the The Facebook
Platform which is a set of APIs that make your application more
social.

%prep
%setup -qc
mv facebook-php-sdk-*/* .

%build
%if %{with tests}
phpunit --colors --verbose --bootstrap src/facebook.php tests/tests.php
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a src/*facebook.php $RPM_BUILD_ROOT%{php_data_dir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.md changelog.md
%{php_data_dir}/facebook.php
%{php_data_dir}/base_facebook.php
%{_examplesdir}/%{name}-%{version}
