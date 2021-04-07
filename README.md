# appCrawler
这只是一个app爬虫的探索，简单记录一下步骤


1.使用Android Studio管理安卓SDK
安装以后设置环境变量，使adb可以在命令行使用
adb(Android debug bridge)可查看手机、模拟器和系统的连接是否成功：
adb devices 显示已连接的所有设备

2.装配Appium（解压缩非常耗时）
需要在设置里手动配置AndroidHome，或者直接在环境变量里添加
配置完了以后启动服务
appium-doctor没有配置成功

3.python安装驱动：
pip install Appium-Python-Client

4.动起来
options = {
    "platformName":"Android",
    "deviceName":"Emulator"    #随意了
    "appPackage":"com.ss.android.ugc.aweme"    #xml里抓到的包名
    "appActivity":"com.ss.android.ugc.aweme.main.MainActivity"
}

driver  = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options)
地址就是appium的服务地址和端口

启动后appium会安装Appium Settings
需要使用apk、包和解包工具来填参数

使用SDK文件夹下build-tools中的appt2尝试获取main activity的名称
aapt2 dump badging "packagepath" #在结果中寻找launchable-activity 
部分apk无法获取该项，使用解包的方式寻找

解包：下载并配置apktool
apktool d package.apk -f
在AndroidManifest.xml中查找MainActivity


5.元素查找：
理论上可以用SDK的工具uiautomatorviewer，半天弄不明白怎么装（SDK和工具使用了Android Studio来管理）

暂用最新版的Appium来查找元素
启动Appium服务后点击放大镜，录入上面提到的启动参数然后开跑，切换页面后可按刷新来更新Appium内的抓取内容
（实际上webdriver.page_source也一样，只是更容易看一些）

点击元素
driver.find_element_by_id("elementId").click()

输入文字
edit_text = driver.find_element_by_id("edit_text")
edit_text.click()
edit_text.send_keys(u"搜索词")

输入中文时考虑关掉软键盘，并以unicodeKeyboard形式发送
options ={
    .........
    "unicodeKeyboard":True,
    "resetKeyboard":True
    .........
}
