[TOC]

![](http://zhgdg.qiniudn.com/ss.png)

众所周知Shadowsocks是一个可穿透防火墙的轻量级代理工具。我们就来说说如何在移动端使用Shadowsocks.

## Android端

###Step0 前提条件
*	JDK 1.6+
*	SBT 0.12.3
*	Android SDK r21+
*	Android NDK r9+


###Step1 下载


__GooglePlay__

[![https://play.google.com/store/apps/details?id=com.github.shadowsocks](http://zhgdg.qiniudn.com/android.png)](https://play.google.com/store/apps/details?id=com.github.shadowsocks)

__Github__

![https://play.google.com/store/apps/details?id=com.github.shadowsocks](http://zhgdg.qiniudn.com/qrcode_android.png)

###Step2 配置
*	打开左侧菜单栏
*	添加配置文件
*	关键数据
	*	服务器
	*	远程端口
	*	本地端口
	*	密码
	*	加密方式
*	通过路由选项实现只能路由
*	也可以通过取消全局代理使用部分应用代理
*	填写完配置后点击右上角打开，使用即可


![https://play.google.com/store/apps/details?id=com.github.shadowsocks](http://zhgdg.qiniudn.com/data_config.png)


## IOS端
对于没有越狱的ios客户端设备，Shadowsocks有两种运行模式。

*	web浏览器模式
*	具有一些限制条件的后台全局代理

###下载

__Applestore__

[![https://play.google.com/store/apps/details?id=com.github.shadowsocks](http://zhgdg.qiniudn.com/applestore.png)](https://itunes.apple.com/us/app/shadowsocks/id665729974?ls=1&mt=8)

###浏览器模式
*	点击+按钮打开菜单
*	将代理配置添加到配置项中
*	切换模式，需重启才会生效

###全局代理模式
~ （一定限制的运行在后台的全局PAC代理）

*	只支持wifi网络
*	服务经常断开，需要间歇性的重开应用
*	配置
	*	添加Shadowsocks配置
	*	复制http://127.0.0.1:8090/proxy.pac
	*	打开ios中的设置->WiFi->i图标->HTTP代理->选择自动并将链接复制进去
	*	定时确认服务在后台运行中
