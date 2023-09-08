# SSAP-auto-calendar
# 需要安装 python 3.4 及以上版本 和 pip

python推荐安装最新版[安装教程](https://zhuanlan.zhihu.com/p/344887837)          
按照上面步骤一步步来，不可能安不上。 
~~实在不行就打劫身边一个会python的同学帮你装~~          
~~或者花8元在lpl那买个包月售后[doge]~~         
python 3.4 及以上版本都预装了 pip   

## SSAP-autp-calendar for mac 教程：

1.打开schoolpal的我的日程

2.使用Chrome/Edge下载HTML文件 注意选择 网页，全部  （此时会下载一个 我的日程.html 文件和一个文件夹）

3.在右边的Release中下载mac版本并解压

4.把“我的日程.html”移动至刚才解压出来的文件夹

5.右键文件夹 点击新建文件夹位置的终端窗口

6.输入启动命令 python3 main.py        
注意：当第一次启动该程序的时候请先输入这条指令安装环境，然后再输入上面那条指令：python3 first.py     

7.把export.ics拖动至日历

## SSAP-autp-calendar for Windows 教程：   

1.打开schoolpal的我的日程

2.使用Chrome/Edge下载HTML文件 注意选择 网页，全部 （此时会下载一个 我的日程.html 文件和一个文件夹）

3.在右边的Release中下载Windows版本并解压

4.把“我的日程.html”移动至刚解压出来的文件夹

5.双击start.bat启动
第一次启动时请点击start_first.bat

6.把export.ics拖动至日历


## Q&A
Q1: 每一次使用的时候需要删除export.ics吗？       
A1: 不需要。

Q2: 为什么我双击了 start.bat 跳出来了 Windows store？      
A2: 因为没有设置环境变量，请卸载python并按照上面的教程重新装载(推荐)          
或者参考[这个教程](https://www.jianshu.com/p/a5c5148b7434)的解决方案(不推荐)          
原因一般是环境变量没有设置好，所以方法二一般没有用。          
如果确认了python已经安装并且会调整环境变量(此处特指Path变量)，请自行调整，但请自负风险。                

Q3: 我用的是虚拟机，我已经按照教程装载了 python ,为什么还是没有办法使用 python ？      
A3: 虚拟机的路径不太一样，建议在 C:/ 下重新装python, 否则环境变量可能无法识别。             

Q4: 有什么自定义功能吗？      
A4:       
1.可以自定义读取的文件 (使用 --read_path your_path),    
2.可以自定义输出的文件 (使用 --save_path your_path),            
3.可以自定义是否不显示某些课程 (使用 --exclude 默认不显示升旗和早自习),              
4.可以自定义不显示课程的名称 (使用 --exclude --exclude_class class_name 注：只要名字有包含添加的字符就会删去，支持添加多个课程，课程之间用空格连接). 
5.可以自定义是否使用开始前提示 (使用 --alarms 默认提前5分钟, 使用 --alarm_set_time minutes 来修改提前的时间)
6.可以自定义提醒的方式 (使用 --alarm_mode mode 目前支持 "display" 和 "audio" 两种模式)
7.可以自定义是否重复日历(按周重复，默认开启，默认20周 使用 --repeat 关闭该功能 使用 --repeat_weeks week 来修改默认值)

Q5: 如果我的课表并不整齐(比如第三节没课) 或者 有一天因为放假全天没课，这个还可以正常显示吗？      
A5: 可以的。但是这个方法目前仍然在公测阶段，需要各位的bug反馈来敲定最终的方法      

Q6: 为什么有换回第一次用另外一个文件下载环境了？
A6: 不然代码会很丑很抽象，还不如这样写。
