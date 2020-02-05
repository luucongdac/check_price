#! /bin/bash
# Arthor: taiit
# Date: 31-Dec-2019
# Summary:
#   + This script install usefull packages for msys2 env
#   + You should install mys2 first, home page: http://www.msys2.org/
#   + Default msys2 install location: /c/msys2/
#   + Inside msys2 prompt, run setup_msys2.sh

msys2_pakage="vim tmux git svn mercurial cvs base-devel wget p7zip perl \
        ruby python3 mingw-w64-i686-toolchain mingw-w64-x86_64-toolchain"


#pacman -Sy
#pacman —needed -S bash pacman pacman-mirrors msys2-runtime
#pacman -Su
echo "pacman -S ${msys2_pakage}"




