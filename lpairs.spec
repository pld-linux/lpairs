Summary:	LPairs - a classic memory game for Linux
Summary(pl.UTF-8):	LPairs - klasyczna gra pamięciowa pod Linuksa
Name:		lpairs
Version:	1.0.4
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
# Source0-md5:	5eb00da9f7fc15dc5ce840c312e76cfa
Patch0:		%{name}-inline.patch
URL:		http://lgames.sourceforge.net/LPairs
BuildRequires:	SDL-devel >= 1.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LPairs - a classic memory game for Linux.

%description -l pl.UTF-8
LPairs - klasyczna gra pamięciowa pod Linuksa.

%prep
%setup -q
%patch0 -p1

%{__perl} -pi -e 's@^inst_dir=\$datadir/games/lpairs$@inst_dir=\$datadir/lpairs@' \
	configure.in

%build
%{__gettextize}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/lpairs
%{_datadir}/%{name}
