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

# check/kill the process by pid

## check process

1. `ps aux | grep -i <process_name>` fetch all the information of the process, -i flag means case incensitive
2. `pgrep <process_name>` get the process id only(useful when you want to kill the process)

## kill the process

1. `pkill <pid>` kill the process by pid

=======================================================================

# screen(really like the concept of tmux)

[ref](https://kawsing.gitbook.io/opensystem/andoid-shou-ji/untitled-4/linux-cli/yong-screen-guan-li-duo-zhong-duan)

## when you are outside the screen

1. `screen -S <screen_name>` create a screen session
2. `screen -ls` list all the screen session
3. `screen -XS <screen_id> quit` kill the screen by id
4. `screen -r <screen_id>` reattach to the screen session, i.e. screen -r 17851

## when you are inside the screen

1. `<C-a>c` create a window in the screen session
2. `<C-a>0~9` switch to certain window
3. `<C-a>w` window list(the asterisk point out the current window)
4. `<C-a>d` detach the current screen session

=======================================================================

#

=======================================================================

#

=======================================================================

#

=======================================================================
