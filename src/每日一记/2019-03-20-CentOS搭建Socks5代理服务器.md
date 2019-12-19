---
layout: post
cid: 266
title: CentOS搭建Socks5代理服务器
slug: 266
date: 2019/03/20 10:15:00
updated: 2019/05/22 11:52:07
status: publish
author: 七木
categories: 
  - 每日一记
tags: 
banner: 
bannerascover: 1
bannerasheadimg: 1
excerpt: Socks5代理服务器
showfullcontent: 0
showTOC: 1
---


##环境：
###阿里云 1H 1G
###服务器操作系统：CentOS 7.3
##安装ss5
登陆到你的服务器
###安装ss5依赖包

    yum install gcc openldap-devel pam-devel openssl-devel
###安装ss5

    wget http://jaist.dl.sourceforge.net/project/ss5/ss5/3.8.9-8/ss5-3.8.9-8.tar.gz

###解压压缩包

    tar -vzx -f ss5-3.8.9-8.tar.gz

###进入解压目录

    cd ss5-3.8.9/

###运行’./configure’

    ./configure

###编译ss5

    make

###安装编译的程序

    make install

###修改权限

    chmod +x /etc/init.d/ss5

###启动ss5

    service ss5 start

###设置监听端口

    vi /etc/sysconfig/ss5  
    # Add startup option here  
    SS5_OPTS=" -u root -b 0.0.0.0:6666"

###修改ss5的配置文件

    vi /etc/opt/ss5/ss5.conf    
    删除auth,permit这两行的注释  
    auth 0.0.0.0/0 - -  
    permit - 0.0.0.0/0 - 0.0.0.0/0 - - - - -

###重启ss5

    service ss5 restart

##结束
接下来用软件测试一下
![][1]
看起来速度还是不错的


  [1]: https://qimu-1251828023.cos.ap-guangzhou.myqcloud.com/2019/03/20/1553061331.jpg