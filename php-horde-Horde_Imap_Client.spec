%define		status		stable
%define		pearname	Horde_Imap_Client
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde IMAP abstraction interface
Name:		php-horde-Horde_Imap_Client
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	124109775f7974d5631b3966badebb11
URL:		http://pear.horde.org/package/Horde_Imap_Client/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-hash
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Mime < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear
Suggests:	php-horde-Horde_Cache
Suggests:	php-horde-Horde_Secret
Suggests:	php-horde-Horde_Stream_Filter
Suggests:	php-imap
Suggests:	php-json
Suggests:	php-mbstring
Suggests:	php-pear-Auth_SASL
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Cache.*) pear(Horde/Secret.*) pear(Horde/Stream/Filter.*) pear(Auth/SASL.*)

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
