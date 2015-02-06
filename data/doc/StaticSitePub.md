# 静态网站发布手册
[TOC]

## 背景
为了解决 中国Py社区离散, 新人无门得入,
大家成立了 蠎中国 ~ PyChina.org 

## 现象
但是, 加入的志愿者当头三问:

- 社区有什么?
- 我能作什么?
- 怎么作?

全部有关开源技术社区开放内容维护的基础问题

## 分析
目测几个原因造成的:

- 长期的 Office 驯化已经想象不能如何不用 GUI 在线发布网站了
- github/Markdow/git 常见工具链的经验缺乏,导致不知如何上手尝试
- 历史原因,杂合而成的快速发布方式,涉及多种工具的理解和灵活组合,进一步加强了志愿者的无措


## 手册
为解决以上问题, 特此专门设立此篇手册,期望作为一个开始,汇集所有社区开放内容的自由/自主/自发的增补

### gitcafe-pages

涉及工具:

- git
    + 要求: 本地安装, 基本命令理解, 有 gitcafe 帐号
- markdown
    + 要求: 基本语法理解, 安装合适的本地编辑环境
- python
    + pip
    + fabric
    + 要求: 本地环境配置好, 先 Python, 再 pip ,通过 pip 安装 fabric
- [qrsync 命令行同步工具 | 七牛云存储](http://developer.qiniu.com/docs/v6/tools/qrsync.html)
    + 要求: 本地安装好, 先在自己的 bucket 空间中测试理解了 7niu 的单向高速同步是什么概念

涉及权限:

- gitcafe 帐号
- 有关仓库权限:
    + 一般而言不需要
    + 获得社区信任后获得,以便直接对相关仓库进行操作
- qrsync 要求的本地配置文件
    + 一般是 `*.json` 格式文件
    + 在获得社区信任后分发
    + 本地进行合理修订后投入使用

#### 团队-pages

#### 项目-pages

### 7niu



# 修订记录

- 150203 [大妈](http://wiki.pychina.org/au/zoomquiet.html) 初稿
- 150201 [大妈](http://wiki.pychina.org/au/zoomquiet.html) 有感微信中的各种 FAQ 起意



