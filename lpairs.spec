Summary:	LPairs - a classic memory game for Linux
Summary(pl):	LPairs - klasyczna gra pamiêciowa pod Linuksa
Name:		lpairs
Version:	1.0.1
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	6d78aa89fe6667fdd25b8cfbb40dad8c
URL:		http://lgames.sourceforge.net/
BuildRequires:	SDL-devel >= 1.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LPairs - a classic memory game for Linux.

%description -l pl
LPairs - klasyczna gra pamiêciowa pod Linuksa.

%prep
%setup -q

%{__perl} -pi -e 's@^inst_dir=\$datadir/games/lpairs$@inst_dir=\$datadir/lpairs@' \
	configure.in

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
