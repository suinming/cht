# i3 window manager

## cmd

- execute app => $mod + d
- full screen => $mode + f
- reload config file => $mod + shift + c
- quit the window => $mode + shift + q
- log out => $mode + shift + e

=======================================================================

# nvm

## update default node version globallly

- [nvm doc](https://github.com/nvm-sh/nvm#installing-and-updating)
- `nvm alias default 18.16.1`

=======================================================================

# neovim

[nvim build doc](https://github.com/neovim/neovim/blob/master/BUILD.md)

## install nvim from source(make sure you got all the require dependencies)

1. clone the neovim repo(if you do not have the repo) `git clone --depth=1 link`
2. fetch the specific version `git fetch origin tag v0.xx.xx --no-tags`
3. make `cd neovim && make CMAKE_BUILD_TYPE=RelWithDebInfo`
4. install neovim `sudo make install`

=======================================================================

# trash-cli

trash-put (alias is tp) => trash files and directories.
trash-empty (alias is tm) => empty the trashcan(s).
trash-list (alias is tl) => list trashed files.
trash-restore => restore a trashed file.
trash-rm => remove individual files from the trashcan.

=======================================================================

# keepassXC

[tutorial video](https://www.youtube.com/watch?v=jL7gfM27EUA)

## install

1. keepassXC

- KeePassXC (PC): https://keepassxc.org
- KeePassDX (Android): https://www.keepassdx.com/

2. syncthing

- PC: https://syncthing.net/
- Android: https://play.google.com/store/apps/de...
  it will start at http://localhost:8384/

3. browser integration

- Chrome: https://chrome.google.com/webstore/de...
- Firefox: https://addons.mozilla.org/en-US/fire...

**目前gmail ncku的密碼強度很低，但因為kobo閱讀器綁定相同帳號因此暫時不改（等目前有作筆記的書閱讀完成再修改）**

=======================================================================

# 中文輸入法

[fcitx5 chewing](https://ivonblog.com/posts/ubuntu-fcitx5/)
[fcitx5 安裝無蝦米](https://samwhelp.github.io/note-about-ubuntu/read/subject/im/fcitx5/howto/install-fcitx5-table-boshiamy.html)

可能需要的操作:

1. 安裝完fcitx5 與輸入法後，可能要**重新開機**
2. 在setting>region&language（地區與語言）> mangage installed languages > keyboard input method system > change to fcitx4 (not ibus)
3. 將 booshiamy and chewing 加入到input，切記不要用查找的，他們會在列表的最下方，用滾輪拉到底就可以

=======================================================================

# rofi

[rofi doc](https://github.com/adi1090x/rofi)

## install

1. install(`sudo apt install rofi`) rofi
2. set up rofi config file(==read the doc[the fk doc](https://github.com/adi1090x/rofi) carefully==)
   - you have to clone the repo on github to get the style of menu
   - just set up the i3 it will work(==it's written in rofi doc==)

## detect appimage file

1. add the config in .local/share/applications as following

```shell
[Desktop Entry]
Exec=/opt/appImageName
Type=Application
Icon='your path to the icon img'
Categories=Development
Name=appName
```

=======================================================================

# icon not show in terminal

## EVERY IMPORTANT, quit and reopen the terminal to refresh the setting

[tutorial video](https://www.youtube.com/watch?v=mQdB_kHyZn8)

1. alacritty
   In alacritty, the most important thing is to set the font family in the .config/alacritty/alacritty.yml file

```yml
font:
  normal:
    family: "SpaceMono Nerd Font"
  size: 16
```

2. kitty
   In kitty, the like alacritty need to set the font family in the .config/kitty/kitty.conf file

```conf
font_family      SpaceMono Nerd Font
bold_font        auto
italic_font      auto
bold_italic_font auto

font_size 16.0

```

=======================================================================

# calibre library

1. wireless transfer book to kobo ereader
   - [video](https://www.youtube.com/watch?v=2emONkbCWUA&list=WL&index=47)
   - wireless device connection in calibre library 
     - in calibre libray app, go to top bar and click connect/share, select `wireless device connection`  
     - in kobo ereader, go to top bar and click on setting, click the first option `Calibre`, click the first option `Connect`

=======================================================================

# install koreader on kobo

- [download OCP-KOReader-v2024.07.zip and install script](https://www.mobileread.com/forums/showthread.php?t=314220)
- [video tutorial](https://www.youtube.com/watch?v=rEouRrPKj-c)

=======================================================================

# pyenv and pyenv-virtualenv

1. [how to install pyenv in zsh and bash](https://medium.com/@b10932006/%E5%A6%82%E4%BD%95%E5%9C%A8ubuntu%E4%B8%AD%E5%AE%89%E8%A3%9Dpyenv%E4%B8%A6%E4%BD%BF%E7%94%A8%E5%A4%9A%E7%A8%AE%E7%89%88%E6%9C%AC%E7%9A%84python-6626c1fbc76e)
2. [pyenv-virtualenv github](https://github.com/pyenv/pyenv-virtualenv)

=======================================================================

# manage multiple ssh keys

1. [How to use Multiple SSH Keys | Managing Different SSH Keys on your System](https://www.youtube.com/watch?v=pE3EuiyShoM)

=======================================================================

# virt-manager set the static ip for virtual machine

1. [step by step guide](https://www.cyberciti.biz/faq/linux-kvm-libvirt-dnsmasq-dhcp-static-ip-address-configuration-for-guest-os/)

=======================================================================

# virt-manager share the directories between host and vm

## vm is linux

1. [step-by-step-article](https://blog.sergeantbiggs.net/posts/file-sharing-with-qemu-and-virt-manager/)

`sudo mount -t virtiofs <dir_name> /home/suinming/<dir_name>` the command should be typed every time open the vm to sync two directories


## vm is windows10

[tutorial](https://www.youtube.com/watch?v=oVHkvx9ZLJc&t=0s)

1. on windows vm need to install [winfsp](https://winfsp.dev/) , [virtio driver](https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/)

=======================================================================

# use yadm to manage dotfiles

1. # [是時候同步你的 dotfiles 了——我選擇 yadm ](https://blog.kyomind.tw/yadm/)

=======================================================================

#

=======================================================================

#

=======================================================================

#
