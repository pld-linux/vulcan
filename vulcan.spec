Summary:	A chess variant
Summary(pl.UTF-8):	Odmiana szachów
Name:		vulcan
Version:	0.5.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.fzort.org/mpr/projects/vulcan/%{name}-%{version}.tar.gz
# Source0-md5:	b5c5f0729038285012fb22a390d76458
Patch0:		%{name}-datadir.patch
URL:		http://www.fzort.org/mpr/projects/vulcan/
BuildRequires:	OpenGL-devel
BuildRequires:	libpng-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vulcan lets you play against the computer a chess variant inspired by
a certain well-known science fiction TV series.

%description -l pl.UTF-8
vulcan pozwala grać przeciwko komputerowi w odmianę szachów
zainspirowaną dobrze znanymi serialami science fiction.

%prep
%setup -q
%patch0 -p1
%{__sed} -i 's@data/@%{_datadir}/%{name}/@' {ui.c,render.c,data/font/*.fontdef}

%build
%{__make} \
	CC="%{__cc}" \
	LD=%{__cc} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install vulcan $RPM_BUILD_ROOT%{_bindir}
cp -r data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TECH
%attr(755,root,root) %{_bindir}/vulcan
%{_datadir}/%{name}
