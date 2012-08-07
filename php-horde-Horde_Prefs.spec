# TODO
# - system locale dir
# - fix missing pear(Horde/Kolab.php)
%define		status		stable
%define		pearname	Horde_Prefs
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde Preferences API
Name:		php-horde-Horde_Prefs
Version:	1.1.8
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	81245a89d767e4486e17219f2e01c032
URL:		https://github.com/horde/horde/tree/master/framework/Prefs/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(json)
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Mime < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-horde-Horde_Autoloader
Suggests:	php-horde-Horde_Db
Suggests:	php-horde-Horde_Image
Suggests:	php-horde-Horde_Imsp
Suggests:	php-horde-Horde_Kolab_Storage
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Db.*) pear(Horde/Image.*) pear(Horde/Imsp.*) pear(Horde/Kolab.php)

%description
The Horde_Prefs package provides a common abstracted interface into
the various preferences storage mediums. It also includes all of the
functions for retrieving, storing, and checking preference values.

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
%{php_pear_dir}/Horde/Prefs.php
%{php_pear_dir}/Horde/Prefs
%{php_pear_dir}/data/Horde_Prefs
