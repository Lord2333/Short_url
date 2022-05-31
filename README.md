# Short_url
短链接生成&amp;解析主程序
![image.png](https://s2.loli.net/2022/05/31/7hHQf3BO9WvUGec.png)

## 安装
本项目可直接只用[Deta](https://web.deta.sh)进行部署，可直接通过下方按钮将本项目配置到Deta。

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/Lord2333/Short_url/)

本项目默认解析**当前域名**为短链接域名，如果需要多链接选项如下图，则需要对`index.html`进行修改。

![image.png](https://s2.loli.net/2022/05/31/hXFKarpH3ZjROvU.png)

域名选择在74-81行处注释，根据选择显示相关链接的js在126、139行处和151-152行，在74行处取消注释并添加你的域名到value里，取消后面的三处注释，即可实现自定义域名。

如果想单独部署短链接跳转，可参考另一个repo，这个是单独的短链接解析，同样基于Deta。

## 注意事项
1. 本项目使用了Deta Base作为数据库，由于Deta官方并未给出具体的字符串长度限制，本人亦未进行测试，因此不建议使用本项目存放长文本生成短链接，以免造成数据丢失。

2. 如果想生成长效短链接，可以进入Deta后台，在Base里找到相应的储存项，将他的`time`改大即可，切勿修改`up_time`，因为定时清理失效链接的函数是用`up_time`进行的计算，大于当前时间时将会报错。
![image.png](https://s2.loli.net/2022/05/31/ngrzoJRSbq5LkCl.png)

3. 本项目的文本传送功能对于文本中的回车解析有问题（主要是Deta Base储存时不支持`\n`）后续将对此问题进行修改。
![image.png](https://s2.loli.net/2022/05/31/7aeFhJD2zsHgiXV.png)