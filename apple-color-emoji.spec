Name:           fonts-apple-color-emoji
Version:        2.0.0
Release:        0.20260722.484daf4e%{?dist}
Summary:        Apple Color Emoji as CBDT/CBLC TTF for Linux

License:        custom
URL:            https://github.com/samuelngs/apple-emoji-ttf
Source0:        https://github.com/samuelngs/apple-emoji-ttf/releases/download/macos-26-20260722-484daf4e/AppleColorEmoji-Linux.ttf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Requires:       fontconfig

%description
Apple Color Emoji as a CBDT/CBLC TTF font for Linux.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/truetype/apple-color-emoji
install -m 0644 %{SOURCE0} \
    %{buildroot}%{_datadir}/fonts/truetype/apple-color-emoji/AppleColorEmoji.ttf

mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d

cat > %{buildroot}%{_sysconfdir}/fonts/conf.d/50-apple-color-emoji.conf <<'EOF'
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <alias>
    <family>emoji</family>
    <prefer>
      <family>Apple Color Emoji</family>
    </prefer>
  </alias>
  <alias>
    <family>serif</family>
    <prefer>
      <family>Apple Color Emoji</family>
    </prefer>
  </alias>
  <alias>
    <family>sans-serif</family>
    <prefer>
      <family>Apple Color Emoji</family>
    </prefer>
  </alias>
  <alias>
    <family>monospace</family>
    <prefer>
      <family>Apple Color Emoji</family>
    </prefer>
  </alias>
</fontconfig>
EOF

%post
/usr/bin/fc-cache -f || :

%postun
if [ $1 -eq 0 ]; then
    /usr/bin/fc-cache -f || :
fi

%files
%{_datadir}/fonts/truetype/apple-color-emoji/AppleColorEmoji.ttf
%config(noreplace) %{_sysconfdir}/fonts/conf.d/50-apple-color-emoji.conf

