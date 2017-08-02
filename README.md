#Spider of lianjia
简单的爬虫，爬取上海地区链家挂牌二手房信息。无代理。。。。。


<pre>
.
├── README.md
├── lianjia
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── items.py
│   ├── items.pyc
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── pipelines.pyc
│   ├── settings.py
│   ├── settings.pyc
│   └── spiders
│       ├── __init__.py
│       ├── __init__.pyc
│       ├── lianjia_sh.py
│       └── lianjia_sh.pyc
├── requirements.txt
└── scrapy.cfg

使用方法
1.安装依赖
pip install -r requirements.txt

2.安装mongodb
Xiemx➜  lianjia : master ✘ :✭ ᐅ  mongod --version
db version v3.4.2
git version: 3f76e40c105fc223b3e5aac3e20dcd026b83b38b
OpenSSL version: OpenSSL 1.0.2l  25 May 2017
allocator: system
modules: none
build environment:
    distarch: x86_64
    target_arch: x86_64

3.查看／运行爬虫
Xiemx➜  lianjia : master ✘ :✭ ᐅ  scrapy list
Xiemx➜  lianjia : master ✘ :✭ ᐅ  scrapy crawl lianjia_sh

4.安利一下tableau，数据出图如下

ps：mongo已经出了驱动，tableu可以用mysql驱动连接数据库。
</pre>

![Alt text](http://xiemx.com/images/tableau.png "xiemx")

