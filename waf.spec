Summary:	The Waf build system
Summary(pl.UTF-8):	System budowania Waf
Name:		waf
Version:	1.5.11
Release:	1
License:	BSD
Group:		Development/Building
Source0:	http://waf.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	a140cb85113643f07e3dce2ed39b272d
Patch0:		%{name}-path.patch
URL:		http://code.google.com/p/waf/
BuildRequires:	python >= 2.4
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
%patch0 -p1

%build
./waf-light configure \
	--prefix=%{_prefix}
./waf-light --make-waf

%install
rm -rf $RPM_BUILD_ROOT
echo y | ./waf install \
	--prefix %{_prefix} \
	--destdir $RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{_libdir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_libdir}/%{name}
%py_postclean %{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/waf
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/wafadmin
%{_libdir}/%{name}/wafadmin/*.py[co]
%dir %{_libdir}/%{name}/wafadmin/Tools
%{_libdir}/%{name}/wafadmin/Tools/*.py[co]
