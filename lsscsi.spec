Summary:        List SCSI devices (or hosts) and associated information
Name:           lsscsi
Version:        0.27
Release:        3%{?dist}
License:        GPLv2+
Group:          Applications/System
Source0:        http://sg.danny.cz/scsi/%{name}-%{version}.tgz
URL:            http://sg.danny.cz/scsi/lsscsi.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Uses information provided by the sysfs pseudo file system in Linux kernel
2.6 series to list SCSI devices or all SCSI hosts. Includes a "classic"
option to mimic the output of "cat /proc/scsi/scsi" that has been widely
used prior to the lk 2.6 series.

Author:
--------
    Doug Gilbert <dgilbert(at)interlog(dot)com>


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc ChangeLog INSTALL README CREDITS AUTHORS COPYING
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man8/*


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.27-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.27-2
- Mass rebuild 2013-12-27

* Fri May 17 2013 Dan Horák <dan[at]danny.cz> - 0.27-1
- update to 0.27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Dan Horák <dan[at]danny.cz> - 0.26-1
- update to 0.26

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Dan Horák <dan[at]danny.cz> - 0.25-1
- update to 0.25

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May  6 2010 Dan Horák <dan[at]danny.cz> - 0.23-2
- fix path separator for FC devices (#589327)
- fix for kernels with unified string representation of NULL (#589860)

* Sun Dec  6 2009 Dan Horák <dan[at]danny.cz> - 0.23-1
- update to 0.23

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  2 2009 Dan Horák <dan[at]danny.cz> - 0.22-1
- update to 0.22

* Tue Nov  4 2008 Dan Horák <dan[at]danny.cz> - 0.21-2
- add disttag

* Tue Nov  4 2008 Dan Horák <dan[at]danny.cz> - 0.21-1
- update to 0.21
- update urls

* Thu May 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.17-6
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.17-5
- Autorebuild for GCC 4.3

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.17-4
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 - Chip Coldwell <coldwell@redhat.com> 0.17-3
- bump the EVR for FC6 rebuild
* Mon Jul 17 2006 - Chip Coldwell <coldwell@redhat.com> 0.17-2
- modify spec file to meet Fedora Project packaging guidelines
* Mon Feb 06 2006 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.17-1
- fix disappearance of block device names in lk 2.6.16-rc1
* Fri Dec 30 2005 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.16-1
- wlun naming, osst and changer devices
* Tue Jul 19 2005 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.15-1
- does not use libsysfs, add filter argument, /dev scanning
* Fri Aug 20 2004 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.13-1
- add 'timeout'
* Sun May 9 2004 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.12-1
- rework for lk 2.6.6, device state, host name, '-d' for major+minor
* Fri Jan 09 2004 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.11-1
- rework for lk 2.6.1
* Tue May 06 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.10-1
- adjust HBA listing for lk > 2.5.69
* Fri Apr 04 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.09-1
- fix up sorting, GPL + copyright notice
* Sun Mar 2 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.08-1
- start to add host listing support (lk >= 2.5.63)
* Fri Feb 14 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.07-1
- queue_depth name change in sysfs (lk 2.5.60)
* Mon Jan 20 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.06-1
- osst device file names fix
* Sat Jan 18 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.05-1
- output st and osst device file names (rather than "-")
* Thu Jan 14 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.04-1
- fix multiple listings of st devices (needed for lk 2.5.57)
* Thu Jan 09 2003 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.03-1
- add --generic option (list sg devices), scsi_level output
* Wed Dec 18 2002 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.02-1
- add more options including classic mode
* Fri Dec 13 2002 - Doug Gilbert <dgilbert(at)interlog(dot)com> 0.01-1
- original
