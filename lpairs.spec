Summary:	LPairs - a classic memory game for Linux
Summary(pl):	LPairs - klasyczna gra pamiêciowa pod Linuksa
Name:		lpairs
Version:	1.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/lgames/%{name}-%{version}.tar.gz
URL:		http://lgames.sourceforge.net/
BuildRequires:	SDL-devel >= 1.0.0
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LPairs - a classic memory game for Linux.

%description -l pl
LPairs - klasyczna gra pamiêciowa pod Linuksa.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/%{name}
