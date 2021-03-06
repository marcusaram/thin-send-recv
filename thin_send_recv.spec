Name: thin-send-recv
Version: 0.11
Release: 1
Summary: send and receive for LVM thin volumes
License: GPLv3+

Requires: /usr/sbin/lvs
Requires: /usr/sbin/thin_dump
Requires: /usr/sbin/thin_delta
Requires: /bin/sh

Source0: %{name}-%{version}-%{release}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: flex make gcc

%description
thin_send serializes a thin volume into a stream. It is more efficient than
dd by only sending allocated data blocks. (In contrast a stream produced by
dd contains lots of zeroes for all not allocated blocks). thin_recv decodes
that stream and applies it to a thin volume.
Thins_send can also create a stream that contains only the blocks modified
by a snapshot or between two snapshots.

%prep
%setup -q -n %{name}-%{version}-%{release}

%build
make EXTRA_CFLAGS=-g

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/*

%changelog
* Tue Dec 17 2019 Philipp Reisner <phil@bk13-2.linbit> - 
- Initial build.

