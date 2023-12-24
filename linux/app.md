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

## install nvim from source

1. for no prerequisites

```shell
git clone https://github.com/neovim/neovim.git

cd neovim

# checkout the stable version of neovim
git checkout stable

# to the build dir
cd build

make CMAKE_BUILD_TYPE=RelWithDebInfo

# This should help ensuring the clean removal of installed files
cpack -G DEB && sudo dpkg -i nvim-linux64.deb

# install the package
sudo make install
```

2. have prerequisites

```shell
git checkout v9.x.x
make CMAKE_BUILD_TYPE=Release
sudo make install
```

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

[安裝無蝦米的教學文](https://ithelp.ithome.com.tw/articles/10257501?sc=rss.qu)

```shell
sudo apt install fcitx
sudo apt install fcitx-table-boshiamy
sudo apt install fcitx-chewing
```

1. 安裝完fcitx 與輸入法後，要**重新開機**
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

#

=======================================================================

```

```
