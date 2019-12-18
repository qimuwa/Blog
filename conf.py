# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog-With-GitHub-Boilerplate/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "qimuwa/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "七木"
site_logo = "${static_prefix}logo.png"
site_build_date = "2018-11-22T12:50+08:00"
author = "七木"
email = "qimuwa@gmail.com"
author_homepage = "https://www.imqimu.cn"
description = "一切看似逝去的，都不曾离开。"
key_words = ['Maverick', '七木', 'Galileo', 'blog', 'qimu', 'qimuwa', '七木哇']
language = 'zh-CN'
external_links = [
    {
        "name": "七木 | Qimu",
        "url": "https://www.imalan.cn",
        "brief": "七木的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/AlanDecode",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/AlanDecode",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5245109677/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
