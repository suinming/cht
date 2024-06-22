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

# Copy file contents to the clipboard in Linux terminal

1. `sudo apt install xclip`
2. `xclip -sel c < input_file.txt` (c stand for clipboard)

=======================================================================

# curl cmd

[article source](https://www.cjkuo.net/linux-curl-detail/)

curl <options> <URL>
-A/--user-agent <string> 設定使用者代理發送給伺服器
-b/--cookie <name=string/file> cookie字串或檔案讀取位置
-c/--cookie-jar <file> 操作結束後把cookie寫入到這個檔案中
-C/--continue-at <offset> 斷點續轉
-d/--data "data"攜帶 HTTP POST Data
-D/--dump-header <file> 把header資訊寫入到該檔案中
-e/--referer 來源網址
-f/--fail 連線失敗時不顯示http錯誤
-F/用來向主機上傳二進制文件，可以指定MIME 類型，也可以指定文件名
-H/--header 設定 request 裡所攜帶的 header
-i/--include 在 output 顯示 response 的 header
-k：指定跳过 SSL 檢測
-L：会让 HTTP 请求跟随服务器的重定向。curl 默认不跟随重定向
--limit-rate：用来限制 HTTP 请求和回应的带宽，模拟慢网速的环境
-o/--output 把輸出寫到該檔案中，等同於wget指令
-O/--remote-name 把輸出寫到該檔案中,保留遠端檔案的檔名
-r/--range <range> 檢索來自HTTP/1.1或FTP伺服器位元組範圍
--resolve HOST:PORT:ADDRESS 強制將 HOST:PORT 解析到指定的IP ADDRESS
-s/--silent 靜音模式。不輸出任何東西
-T/--upload-file <file> 上傳檔案
-u/--user <user[:password]> 設定伺服器的使用者和密碼
-v/--verbose 輸出更多的訊息方便 debug
-w/--write-out [format] 什麼輸出完成後
-x/--proxy <host[:port]> 在給定的埠上使用HTTP代理
-X/--request [GET|POST|PUT|DELETE|PATCH] 使用指定的 http method 來發出 http request
-#/--progress-bar 進度條顯示當前的傳送狀態

=======================================================================

# Static IP assignment for KVM guest

[article_link](https://dyiwu.github.io/2020/06/kvm-guest-dhcp-ip/)

=======================================================================

# copy file between local pc and server

- on my local pc, copy the file from `local pc` to `server`:
  `scp /path_on_local/to/destination_dir root@<server_ip>:/path_on_server/to/target.file`

- on my local pc, copy the file from `server` to `local pc`:
  `scp root@<server_ip>:/path_on_server/to/target.file /path_on_local/to/destination_dir`

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
