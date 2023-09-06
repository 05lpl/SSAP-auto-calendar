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

6.输入启动命令 python3 auto_calendar.py        
注意：当第一次启动该程序的时候需要输入：python3 auto_calendar.py --first        

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
4.可以自定义不显示课程的名称 (使用 --exclude --exclude_class class_name).      

Q5: 如果我的课表并不整齐(比如第三节没课) 或者 有一天因为放假全天没课，这个还可以正常显示吗？
A5: 可以的。
