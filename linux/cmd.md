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

# install deb package

1. remember to type in the full path of the deb package
2. type in `./` is important to specify the location

```shell
sudo apt install ./path.to.the.deb
```

=======================================================================

#

=======================================================================

#

=======================================================================

#

=======================================================================

#

=======================================================================

#

=======================================================================
