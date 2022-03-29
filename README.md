# epicseven脚本
## 环境配置
* 需要安装pytohn3.9及以下python环境；
* 安装airtest包，airtest包安装命令:
    ```
    pip install --user airtest
    ```
* 默认使用夜神模拟器，其它模拟器需要自行去.py文件修改端口号:  
auto_setup(\__file\__,devices=["Android://127.0.0.1:5037/127.0.0.1:**62001**?cap_method=JAVACAP&&ori_method=ADBORI"])</p>
不同模拟器需要修改**粗体部分**端口号
* 各个模拟器常用端口号：  
Genymotion 5555  
夜神模拟器 62001  
海马玩模拟器 26944  
网易mumu模拟器 7555  
天天模拟器 6555  
逍遥游 21503  
安卓模拟器大师 54001  
BlueStacks 5555
## 具体运行
* 模拟器脚本，文件夹放在**桌面**上，运行
epicseven.bat文件执行（乱码是编码格式错误）
* 所有脚本运行都从大厅开始，结束后会自动回到大厅
* 现阶段实现自动竞技场npc、圣域收菜，刷商店，远征（旧版，未实现公开远征），自动9-4，迷宫（暂时是我自己用的）。
