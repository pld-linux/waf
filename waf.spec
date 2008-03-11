Summary:	The Waf build system
Summary(pl.UTF-8):	System budowania Waf
Name:		waf
Version:	1.3.2
Release:	1
License:	BSD
Group:		Development/Building
Source0:	http://waf.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	9caca69cb435911c9ed6ff0519ce19ae
URL:		http://code.google.com/p/waf/
BuildRequires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir	%{_prefix}/lib

%description
Waf is a general-purpose build system which was modelled from Scons.
Though it comes last in the arena of the build systems, we believe
that Waf is a vastly superior alternative to its competitors
(Autotools, Scons, Cmake, Ant, etc) for building software,

%description -l pl.UTF-8
Waf to system budowania ogólnego przeznaczenia opracowany na podstawie
Scons. Mimo że pojawił się jako ostatni na arenie systemów budowania,
autorzy wierzą, że przewyższa alternatywne narzędzia (Autotools,
Scons, Cmake, Ant itp.).

%prep
%setup -q

%build
./waf-light --make-waf

%install
rm -rf $RPM_BUILD_ROOT
./waf install \
	--prefix %{_prefix} \
	--destdir $RPM_BUILD_ROOT \

%py_comp $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}-*
%py_ocomp $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}-*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/waf
%dir %{_libdir}/%{name}-%{version}-*
%dir %{_libdir}/%{name}-%{version}-*/wafadmin
%{_libdir}/%{name}-%{version}-*/wafadmin/*.py[co]
%dir %{_libdir}/%{name}-%{version}-*/wafadmin/Tools
%{_libdir}/%{name}-%{version}-*/wafadmin/Tools/*.py[co]
