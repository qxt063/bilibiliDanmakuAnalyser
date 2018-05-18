bilibili弹幕爬取分析工具
========================

emmm综合实验的爬虫。都是一些简单的东西<br/><br/>
能够通过av号爬取弹幕信息，写入mongoDB，写入excel<br/>
能够生成五种图形<br/><br/>
弹幕数量与视频时间关系图<br/>
弹幕颜色占比饼图<br/>
发送弹幕数量相同的用户数量占比饼图（就是10个人发了1条，5个人发了两条这种。。）<br/>
弹幕总体数量随日期增长情况图<br/>
弹幕词云<br/><br/>
有一个假装是gui的gui。。啥都干不了的gui<br/>
外面的main函数是假的，那个是不带gui的版本，程序入口点在src/gui/window.py里面<br/>
老师要求做gui我没做临时补得。。listview没看懂就没时间了就算了<br/><br/>
其实还有好多想完善的坑。。不过不打算填坑了，除非哪天有时间了...<br/><br/>
另外，b站最近好像换了弹幕api。。新的api是<br/>
danmakuUrl='https://api.bilibili.com/x/v1/dm/list.so?oid=' + cid<br/>