Summary:	The Waf build system
Summary(pl.UTF-8):	System budowania Waf
Name:		waf
Version:	1.0.1
Release:	1
License:	BSD
Group:		Development/Building
Source0:	http://freehackers.org/~tnagy/%{name}-%{version}.tar.bz2
# Source0-md5:	bc33d144ee927caec6279e0bf4b174ab
URL:		http://freehackers.org/~tnagy/bksys.html
Patch0:		%{name}-path.patch
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
%patch0 -p1

%build
./waf-light --make-waf

%install
rm -rf $RPM_BUILD_ROOT
./waf \
	--prefix $RPM_BUILD_ROOT%{_prefix} \
	--destdir $RPM_BUILD_ROOT \
	--install

%py_comp $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}
%py_ocomp $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}
%py_postclean %{_libdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/waf
%dir %{_libdir}/%{name}-%{version}
%dir %{_libdir}/%{name}-%{version}/wafadmin
%{_libdir}/%{name}-%{version}/wafadmin/*.py[co]
%dir %{_libdir}/%{name}-%{version}/wafadmin/Tools
%{_libdir}/%{name}-%{version}/wafadmin/Tools/*.py[co]
