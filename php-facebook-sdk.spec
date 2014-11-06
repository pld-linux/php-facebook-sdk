#
# Conditional build:
%bcond_without	tests		# build with tests

%if "%(cat /etc/resolv.conf >/dev/null 2>/dev/null; echo $?)" != "0"
%undefine	with_tests
%endif

%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	PHP SDK for the Facebook API
Name:		php-facebook-sdk
Version:	3.2.3
Release:	1
License:	Apache v2.0
Group:		Development/Languages/PHP
Source0:	https://github.com/facebookarchive/facebook-php-sdk/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fc8edc0afea0cbe8e64b539f491f5a19
Patch0:		class-nps.patch
URL:		https://github.com/facebookarchive/facebook-php-sdk
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
%if %{with tests}
BuildRequires:	%{php_name}-curl
BuildRequires:	%{php_name}-hash
BuildRequires:	%{php_name}-json
BuildRequires:	%{php_name}-pecl-xdebug
BuildRequires:	%{php_name}-session
BuildRequires:	php-PHPUnit >= 3.5
%endif
Requires:	php(core) >= %{php_min_version}
Requires:	php(curl)
Requires:	php(hash)
Requires:	php(json)
Suggests:	php(session)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear base_facebook.php

%description
Open Source PHP SDK that allows you to utilize the The Facebook
Platform which is a set of APIs that make your application more
social.

%prep
%setup -qn facebook-php-sdk-%{version}
cp -p src/facebook.php src/facebook.nps.php
%patch0 -p1

%build
%if %{with tests}
phpunit \
	-d session.save_handler="files" \
	-d session.save_path="$(pwd)" \
	-d include_path=".:$(pwd):%{php_pear_dir}" \
	--colors \
	--coverage-html coverage \
	--verbose \
	--stderr \
	--bootstrap tests/bootstrap.php \
	tests/tests.php
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
