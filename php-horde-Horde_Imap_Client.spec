# TODO
# - system locale dir
%define		status		stable
%define		pearname	Horde_Imap_Client
Summary:	%{pearname} - Horde IMAP abstraction interface
Name:		php-horde-Horde_Imap_Client
Version:	1.5.10
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	f26f23111ab0f42bcb17afc098300893
URL:		https://github.com/horde/horde/tree/master/framework/Imap_Client/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(hash)
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Mime < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-horde-Horde_Cache
Suggests:	php-horde-Horde_Secret
Suggests:	php-horde-Horde_Stream_Filter
Suggests:	php-imap
Suggests:	php-json
Suggests:	php-mbstring
Suggests:	php-pear-Auth_SASL
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an abstracted API interface to various IMAP4rev1
(RFC 3501) backend drivers.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%{__rm} $RPM_BUILD_ROOT%{php_pear_dir}/data/Horde_Imap_Client/locale/%{pearname}.pot
%{__rm} $RPM_BUILD_ROOT%{php_pear_dir}/data/Horde_Imap_Client/locale/*/LC_MESSAGES/%{pearname}.po

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Horde/Imap
%{php_pear_dir}/Horde/Imap/Client.php
%{php_pear_dir}/Horde/Imap/Client
%{php_pear_dir}/data/Horde_Imap_Client
