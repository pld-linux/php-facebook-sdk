#
# Conditional build:
%bcond_with	tests		# build with tests

%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	PHP SDK for the Facebook API
Name:		php-facebook-sdk
Version:	3.1.1
Release:	6
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	https://github.com/facebook/facebook-php-sdk/tarball/v%{version}#/%{name}-%{version}.tgz
# Source0-md5:	3e23cbda87e68f95f3b222cbb868e5d1
Patch0:		class-nps.patch
URL:		https://github.com/facebook/facebook-php-sdk
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
%if %{with tests}
BuildRequires:	php-PHPUnit >= 3.5
BuildRequires:	php-curl
BuildRequires:	php-hash
BuildRequires:	php-json
BuildRequires:	php-pecl-xdebug
BuildRequires:	php-session
%endif
Requires:	php(core) >= %{php_min_version}
Requires:	php(curl)
Requires:	php(hash)
Requires:	php(json)
Suggests:	php(session)
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
mv facebook-facebook-php-sdk-*/* .
cp src/facebook.php src/facebook.nps.php
%patch0 -p1

%build
%if %{with tests}
phpunit --colors --coverage-html coverage --verbose --stderr --bootstrap tests/bootstrap.php tests/tests.php
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a src/*facebook*.php $RPM_BUILD_ROOT%{php_data_dir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.md changelog.md
%{php_data_dir}/facebook.php
%{php_data_dir}/facebook.nps.php
%{php_data_dir}/base_facebook.php
%{_examplesdir}/%{name}-%{version}
