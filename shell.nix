with (import <nixpkgs> {});
mkShell rec {
  buildInputs = [
    (python311.withPackages (pypkgs: with pypkgs; [ pyside6 pip ])) # have add add here to make sure qt subversions line up
    zstd
    zlib
    dbus
    fontconfig
    freetype
    glib
    libGL
    libkrb5
    libpulseaudio
    libva
    libxkbcommon
    openssl
    qt6.full
    stdenv.cc.cc.lib
    wayland
    xorg.libX11
    xorg.libxcb
    xorg.libXi
    xorg.libXrandr
    xorg.xcbutilwm
    xorg.xcbutilimage
    xorg.xcbutilkeysyms
    xorg.xcbutilrenderutil
    xorg.xcbutilerrors
    xorg.libSM
    xorg.libICE
    xcb-util-cursor
  ];

  LD_LIBRARY_PATH = lib.makeLibraryPath buildInputs;

  shellHook = ''
    # Emulate venv by telling pip to use local dir for packets
    export PIP_PREFIX=$(pwd)/pip_packages
    export PYTHONPATH="$PIP_PREFIX/${python311.sitePackages}:$PYTHONPATH"
    export PATH="$PIP_PREFIX/bin:$PATH"
    unset SOURCE_DATE_EPOCH
  '';
}
