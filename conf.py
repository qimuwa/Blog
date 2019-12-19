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
author = "七木's Blog"
email = "qimuwa@gmail.com"
author_homepage = "https://www.imqimu.cn"
description = "一切看似逝去的，都不曾离开。"
key_words = ['Maverick', '七木', 'Galileo', 'blog', 'qimu', 'qimuwa', '七木哇']
language = 'zh-CN'
background_img = '${static_prefix}bg/bg_1.jpg'
external_links = [
    {
        "name": "七木 | Qimu",
        "url": "https://www.imqimu.cn",
        "brief": "七木的主页。"
    },
    {
        "name": "Love",
        "url": "https://love.imqimu.cn",
        "brief": "此生只有你。"
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
        "name": "GitHub",
        "url": "https://github.com/qimuwa",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5625238857/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="dns-prefetch" href="//blog.imqimu.cn" />
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="application-name" content="七木 | Qimu">
<meta name="apple-mobile-web-app-title" content="七木 | Qimu">
<link rel="shortcut icon" href="${static_prefix}favicon.ico">
<meta name="google-site-verification" content="t3OmqFng0xM4Abot0kdoBNGlMXkfv6yMGMuO5O5sTuo" />
'''

footer_addon = r'''
<a no-style href="http://www.miitbeian.gov.cn/" target="_blank">豫ICP备19037160号</a>
'''

body_addon = r'''
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?94ff98c7fab8d01d1b60fdc532c6c464";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
'''
