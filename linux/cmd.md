# compress or decompress(extract) the file

.tar  
打包：tar cvf FileName.tar DirName  
解包： tar xvf FileName.tar

.gz  
壓縮：gzip FileName  
解壓 1：gunzip FileName.gz  
解壓 2：gzip -d FileName.gz

.tar.gz  
壓縮：tar zcvf FileName.tar.gz DirName  
解壓：tar zxvf FileName.tar.gz

.bz2  
壓縮： bzip2 -z FileName  
解壓 1：bzip2 -d FileName.bz2  
解壓 2：bunzip2 FileName.bz2

.tar.bz2  
壓縮：tar jcvf FileName.tar.bz2 DirName  
解壓：tar jxvf FileName.tar.bz2

.bz  
壓縮：unkown  
解壓 1：bzip2 -d FileName.bz  
解壓 2：bunzip2 FileName.bz

.tar.bz  
壓縮：unkown  
解壓：tar jxvf FileName.tar.bz

.Z  
壓縮：compress FileName  
解壓：uncompress FileName.Z

.tar.Z  
壓縮：tar Zcvf FileName.tar.Z DirName  
解壓：tar Zxvf FileName.tar.Z

.tgz  
壓縮：unkown  
解壓：tar zxvf FileName.tgz

.tar.tgz  
壓縮：tar zcvf FileName.tar.tgz FileName  
解壓：tar zxvf FileName.tar.tgz

.zip  
壓縮：zip FileName.zip DirName  
解壓：unzip FileName.zip

.rar  
壓縮：rar e FileName.rar  
解壓：rar a FileName.rar

.lha  
壓縮：lha -a FileName.lha FileName  
解壓：lha -e FileName.lha
=======================================================================

# install .deb package

```shell
# remember to type in the full path of the deb package
sudo apt install path.to.the.deb
```

=======================================================================

# install nvim from source

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

=======================================================================

# trash-cli

trash-put ( alias is tp) => trash files and directories.
trash-empty ( alias is tm) => empty the trashcan(s).
trash-list ( alias is tl) => list trashed files.
trash-restore => restore a trashed file.
trash-rm => remove individual files from the trashcan.

=======================================================================

#

=======================================================================
