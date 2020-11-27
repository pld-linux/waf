Summary:	The Waf build system
Summary(pl.UTF-8):	System budowania Waf
Name:		waf
Version:	2.0.21
Release:	1
# note: waf book is on CC-BY-NC-ND (not included in binary package)
License:	BSD
Group:		Development/Building
Source0:	https://waf.io/%{name}-%{version}.tar.bz2
# Source0-md5:	20e89032bf6da95ee8d38c87b4a1236a
Patch0:		%{name}-path.patch
URL:		https://waf.io/
BuildRequires:	python3
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.507
Requires:	python(abi) = %{py3_ver}
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

%{__sed} -i -e '1s,/usr/bin/.*python,%{__python3},' waf-light waflib/Context.py waflib/processor.py waflib/extras/javatest.py

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
install -d $RPM_BUILD_ROOT%{_datadir}/waf3/waflib/{Tools,extras}

cp -p waflib/*.py $RPM_BUILD_ROOT%{_datadir}/waf3/waflib
cp -p waflib/Tools/*.py $RPM_BUILD_ROOT%{_datadir}/waf3/waflib/Tools
cp -p waflib/extras/*.py $RPM_BUILD_ROOT%{_datadir}/waf3/waflib/extras

install -D -p waf-light $RPM_BUILD_ROOT%{_bindir}/waf

%py3_comp $RPM_BUILD_ROOT%{_datadir}/waf3/waflib
%py3_ocomp $RPM_BUILD_ROOT%{_datadir}/waf3/waflib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{_bindir}/waf
%{_datadir}/waf3
