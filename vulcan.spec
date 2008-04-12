Summary:	A chess variant
Summary(pl.UTF-8):	Odmiana szachów
Name:		vulcan
Version:	0.92
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.fzort.org/mpr/projects/vulcan/%{name}-%{version}.tar.gz
# Source0-md5:	6010626b4c38f0c3eb166b80f8e1bc26
Patch0:		%{name}-Makefile.patch
URL:		http://www.fzort.org/mpr/projects/vulcan/
BuildRequires:	OpenGL-devel
BuildRequires:	libpng-devel
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

%build
%{__make} \
	CC="%{__cc}" \
	LD=%{__cc} \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags} -L./lib3d"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TECH
%attr(755,root,root) %{_bindir}/vulcan
%{_datadir}/%{name}
