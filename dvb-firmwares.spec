# TODO
#	resolve cx88 conflicts with linux-firmware
#
Summary:	Firmware files used by DVB modules
Summary(pl.UTF-8):	Pliki firmware'u używane przez sterowniki DVB
Name:		dvb-firmwares
Version:	20110802
Release:	2
License:	Redistributable
Group:		Base/Kernel
Source0:	http://linuxtv.org/downloads/firmware/%{name}-%{version}.tar.bz2
# Source0-md5:	330e19f9444a03f5338bab590ab9d728
Source1:	%{name}-%{version}.txt
# dvb-firmwares-20110802.txt - text version of index.php from the URL
# below. Includes copyright information and distribution conditions
# of the firmware images.
URL:		http://linuxtv.org/downloads/firmware/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes firmware files required for the following TV/DVB
equipment:
- OREN demodulators
- various USB devices
  - Twinhan USB-T VP-7045/VP-7046 (MagicBoxII)
  - AVerMedia
  - various DiBcom USB1.1
  - DiBcom/Artec USB2.0
  - HanfTek UMT-010 USB2.0
  - WideViewer WT-220U PenType DVB-T Receiver
  - Yakumo/Typhoon/Hama USB2.0
- Conexant devices
- Xceive devices
- Dibcom driver for dib0700
- AV7110
- Terratec devices

%description -l pl.UTF-8
Ten pakiet zawiera pliki firmware'u wymagane do działania
następujących urządzeń TV/DVB:
- demodulatory OREN
- różne urządzenia USB
  - Twinhan USB-T VP-7045/VP-7046 (MagicBoxII)
  - AVerMedia
  - różne DiBcom USB1.1
  - DiBcom/Artec USB2.0
  - HanfTek UMT-010 USB2.0
  - WideViewer WT-220U PenType DVB-T Receiver
  - Yakumo/Typhoon/Hama USB2.0
- urządzenia z chipsetem Conexant
- urządzenia z chipsetem Xceive
- urządzeń Dibcom obsługiwanych przez sterownik dib0700
- AV7110
- urządzenia z chipsetem Terratec

%prep
%setup -qc
%{__cp} %{SOURCE1} README

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
%{__cp} -a . $RPM_BUILD_ROOT/lib/firmware
%{__rm} $RPM_BUILD_ROOT/lib/firmware/README
# v4l-cx231xx-avcore-01.fw is included in linux-firmware-20130201-1.noarch
%{__rm} $RPM_BUILD_ROOT/lib/firmware/v4l-cx231xx-avcore-01.fw

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
/lib/firmware/*
