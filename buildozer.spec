[app]
# 应用名称（手机上显示的名字）
title = 题库搜索神器

# 包名（必须全小写，不能有特殊符号）
package.name = myquestionapp
package.domain = org.example

# 核心配置：入口文件是 main.py
source.dir = .
source.main = main.py

# 必须包含的库
requirements = python3,kivy

# 【关键修复】指定 NDK 版本，防止自动下载出错
android.ndk = 25.1.8937393
# 指定 Android API 版本
android.api = 31
android.minapi = 21

# 权限设置（悬浮窗、存储、网络）
android.permissions = SYSTEM_ALERT_WINDOW, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET

# 版本信息
version = 1.0.2

# 架构设置（arm64-v8a 是目前主流手机架构）
android.arch = arm64-v8a

# 启动图标（如果没有 icon.png 文件，请注释掉下面这行，或者上传一个名为 icon.png 的图片）
# icon.filename = %(source.dir)s/icon.png
