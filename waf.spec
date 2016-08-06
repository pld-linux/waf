Summary:	The Waf build system
Summary(pl.UTF-8):	System budowania Waf
Name:		waf
Version:	1.9.2
Release:	1
# note: waf book is on CC-BY-NC-ND (not included in binary package)
License:	BSD
Group:		Development/Building
Source0:	http://waf.io/%{name}-%{version}.tar.bz2
# Source0-md5:	6a6f36a9a6a5ace8fab3109446c35706
Patch0:		%{name}-path.patch
URL:		http://waf.io/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
Requires:	python(abi) = %{py_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
# check waf-light
extras=
for f in waflib/extras/*.py ; do
	tool=$(basename "$f" .py)
	if [ "$tool" != "__init__" ]; then
		extras="${extras:+$extras,}$tool"
	fi
done
./waf-light --make-waf --strip --tools="$extras"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/waf/waflib/{Tools,extras}

cp -p waflib/*.py $RPM_BUILD_ROOT%{_datadir}/waf/waflib
cp -p waflib/Tools/*.py $RPM_BUILD_ROOT%{_datadir}/waf/waflib/Tools
cp -p waflib/extras/*.py $RPM_BUILD_ROOT%{_datadir}/waf/waflib/extras

install -D -p waf-light $RPM_BUILD_ROOT%{_bindir}/waf

%py_comp $RPM_BUILD_ROOT%{_datadir}/waf/waflib
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/waf/waflib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{_bindir}/waf
%{_datadir}/waf
