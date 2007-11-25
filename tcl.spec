%def_without test
%define major 8.5

Name: tcl
Version: 8.5.0
Release: alt0.4

Summary: A Tool Command Language (TCL) 
License: BSD
Group: Development/Tcl
Url: http://www.tcl.tk/

Source: %name-%version-%release.tar

BuildRequires(pre): rpm-build-tcl
%{?_with_test:BuildConflicts: tcl-vfs}

Requires: lib%name = %version-%release
Requires: tcl8.4

# FIXME tm modules
Provides: tcl(http) = 2.5.3
Provides: tcl(msgcat) = 1.4.2
Provides: tcl(palform) = 1.0.3
Provides: tcl(platform::shell) = 1.1.3
Provides: tcl(tcltest) = 2.3b1

%package -n lib%name
Summary: A Tool Command Language (TCL) - shared library
Group: System/Libraries
Provides: %_tcllibdir
Provides: %_tcldatadir

%package devel
Summary: Header files and C programming manual for TCL
Group: Development/C
Requires: %name = %version-%release
Requires: rpm-build-tcl

%description
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks.  When paired with
the Tk toolkit, Tcl provides the fastest and most powerful way to
create GUI applications that run on PCs, Unix, and the Macintosh.  Tcl
can also be used for a variety of web-related tasks and for creating
powerful command languages for applications.

%description -n lib%name
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks.  When paired with
the Tk toolkit, Tcl provides the fastest and most powerful way to
create GUI applications that run on PCs, Unix, and the Macintosh.  Tcl
can also be used for a variety of web-related tasks and for creating
powerful command languages for applications.

This package includes shared Tcl library only.

%description devel
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks.  When paired with
the Tk toolkit, Tcl provides the fastest and most powerful way to
create GUI applications that run on PCs, Unix, and the Macintosh.  Tcl
can also be used for a variety of web-related tasks and for creating
powerful command languages for applications.

This package includes header files and C programming manuals for Tcl.

%prep
%setup

%build
cd unix
%__autoconf
%configure --disable-rpath --enable-threads
make all %{?_with_test:test}

%install 
%define __tclsh %buildroot%_bindir/.tclsh
%make_install INSTALL_ROOT=%buildroot install -C unix
mkdir -p %buildroot%_tcllibdir %buildroot%_tcldatadir
install -p -m0644 -D tcl.m4 %buildroot%_datadir/aclocal/tea.m4
ln -sf tclsh%major %buildroot%_bindir/tclsh
ln -sf lib%name%major.so %buildroot%_libdir/lib%name.so
ln -s ../unix/tclUnixPort.h %buildroot%_includedir/tcl/generic/tclUnixPort.h
cat <<EOF > %__tclsh
#!/bin/sh
LD_LIBRARY_PATH=%buildroot%_libdir; export LD_LIBRARY_PATH
TCL_LIBRARY=%buildroot%_tcldatadir/%name%major; export TCL_LIBRARY
exec %buildroot%_bindir/tclsh "\$@"
EOF
chmod +x %__tclsh

%post -n lib%{name} -p %post_ldconfig
%postun -n lib%{name} -p %postun_ldconfig

%files
%doc README license* ChangeLog changes
%_bindir/tclsh*
%_tcldatadir/tcl8
%_tcldatadir/%name%major
%exclude %_tcldatadir/%name%major/ldAix
%exclude %_tcldatadir/%name%major/%{name}AppInit.c
%_man1dir/*
%_mandir/mann/*

%files -n lib%name
%dir %_tcllibdir
%dir %_tcldatadir
%_libdir/lib%name%major.so

%files devel
%_includedir/*
%_libdir/lib%name.so
%_libdir/lib%{name}stub%{major}.a
%_libdir/%{name}Config.sh
%_tcldatadir/%name%major/%{name}AppInit.c
%_datadir/aclocal/*.m4
%_man3dir/*

%changelog
* Sun Nov 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt0.4
- garbage in tclConfig.sh fixed

* Fri Nov 23 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt0.3
- 8.5b3 released

* Tue Nov 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt0.2
- 8.5b2 released

* Mon Nov 19 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt0.1
- 8.5b1 released

* Tue Sep 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.16-alt1
- 8.4.16
- added rpm-build-tcl to tcl-devel deps (at@)

* Sat Sep 15 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.15-alt1
- 8.4.15

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 8.4.13-alt1.0
- Automated rebuild.

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.13-alt1
- 8.4.13

* Sun Jan  8 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.12-alt1
- 8.4.12

* Wed Jul 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.11-alt1
- 8.4.11

* Mon Jun 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.10-alt1
- 8.4.10

* Sun Apr  3 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.9-alt1
- 8.4.9

* Sat Dec  4 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.8-alt1
- 8.4.8

* Mon Oct 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.7-alt2
- cvs snapshot @20041014
- rpm macro file moved to rpm-build-tcl package

* Mon Aug  2 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.7-alt1
- 8.4.7

* Mon Mar  8 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.6-alt1
- 8.4.6

* Tue Nov 25 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.5-alt1
- 8.4.5

* Sat Jul 26 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 8.4.4-alt1
- 8.4.4

* Thu May 22 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 8.4.3-alt1
- 8.4.3

* Wed Mar 12 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 8.4.2-alt2
- fixed: #702383

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 8.4.2-alt1
- 8.4.2

* Mon Feb 17 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 8.4.2-alt0.1
- CVS snapshot @ 20030215

* Wed Oct 23 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.4.1-alt1
- 8.4.1

* Wed Sep 25 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.4.0-alt1
- 8.4.0
- new package lib%name appeared
- new layout:
  - libtclXX.so goes back to %_libdir
  - tcl_pkgPath _not_ contains %_tcllibdir nor %_libdir
  - all script stuff goes to %_tcldatadir
- tcl-specific rpm macros added

* Mon Jun 3 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.3.4-alt8
- libpath changed to %_libdir/tcl, tcl_pkgPath contains also %_datadir/tcl
  for pure-tcl extensions
- tcl.m4 installs system-wide, please use them
- now contains private headers in %_includedir/tcl
- adopted patches from RH & SuSE
- src rpm splitted

* Mon Mar 18 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.3.4-alt7
- fixed encoding file for koi8-u

* Tue Mar 05 2002 Stanislav Ievlev <inger@altlinux.ru> 8.3.4-alt6
- removed all -lieee, 'cause
  fist: Programs can work with -lm and without -lieee
  second: Programs cannot link with lieee library

* Fri Dec  7 2001 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.3.4-alt5
- tclx fixes
- fixed tls build with stubs from tcl build dir
- fixed permissions for %_libdir/lib*stub*.a

* Wed Oct 24 2001 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.3.4-alt4
- Tcl/Tk 8.3.4
- SSL support added (tcl-tls)

* Mon Jul 23 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.3.3-alt3
- Removed unnecessary provides and obsoletes.
- Added *_rel macros for subpackages and corrected inter-requires.
- Merged RH patches.

* Sat Jun 16 2001 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.3.3-alt2
- Rearranged files in subpackages: tcl, tcl-devel
- Tk splitted to: tk tk-devel tk-demos
- tclX 8.3.0, splitted to: tclx tclx-devel
- tix 8.1, splitted to: tix tix-devel tix-demos
- itcl 3.2, splitted to: itcl itcl-devel itcl-demos compat-itcl compat-itcl-demos. Huh :)
- tcllib removed to separate package
- Dropped most of changelog entries
- Group fixed

* Tue May 15 2001 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.3.3-alt1
- Tcl/Tk 8.3.3
- tcllib 0.8
- expect 5.32, splitted to subpackages.

* Wed Feb 07 2001 Dmitry V. Levin <ldv@fandra.org> 8.3.2-ipl8mdk
- Moved include files and C programming manual to tcl-devel subpackage.
- Fixed out empty manpages.

* Wed Nov 29 2000 AEN <aen@logic.ru> 8.3.2-ipl7mdk
- build for RE
- ps patch from Viktor Wagner
- bad requires patch

# local variables:
# compile-command: "gear --commit --hasher -- hsh --repo=tcl"
# end:
