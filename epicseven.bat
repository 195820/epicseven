@echo off
:7
echo.
echo 输入1后按回车，每日任务(深渊、竞技场npc、迷宫商人、领天空石)
echo 输入2后按回车，刷书签
echo 输入3后按回车，远征(公开，非公开)
echo 输入4后按回车，刷9-4
echo 输入5后按回车，迷宫
echo 输入6后按回车，退出
echo.
set /p start=选择数字后按回车：
if "%start%"=="1" goto 1
if "%start%"=="2" goto 2
if "%start%"=="3" goto 3
if "%start%"=="4" goto 4
if "%start%"=="5" goto 5
if "%start%"=="6" goto 6
:1
@echo off
cd C:\Users\%USERNAME%\Desktop\epicseven\daily
python daily.py
echo 执行完成
goto 7
:2
@echo off
C:
cd C:\Users\%USERNAME%\Desktop\epicseven\key
set /p num1=设置书签数量后按回车：
python key.py "%num1%"
echo 执行完成
goto 7
:3
@echo off
C:
cd C:\Users\%USERNAME%\Desktop\epicseven\expedition
echo 输入1后按回车，非公开远征
echo 输入2后按回车，公开远征
echo.
set /p start1=选择数字后按回车：
if "%start1%"=="2" goto 8
set /p num3=设置执行的远征类型(按次序左上、右上、下)后按回车：
python expedition.py "%num3:~0,1%" "%num3:~2,1%" "%num3:~4,1%"
echo 执行完成
goto 7
：8
set /p num3=设置执行的远征类型(按次序左上、右上、下)后按回车：
python expedition1.py "%num3:~0,1%" "%num3:~2,1%" "%num3:~4,1%"
echo 执行完成
goto 7
:4
@echo off
C:
cd C:\Users\%USERNAME%\Desktop\epicseven\9-4
set /p num2=设置执行次数后按回车：
python 9-4.py "%num2%"
echo 执行完成
goto 7
:5
cd C:\Users\%USERNAME%\Desktop\epicseven\mazen
set /p num4=迷宫次数(2,3)：
if "%num4%"=="2" python mazen.py
if "%num4%"=="3" python mazen1.py
:6
Exit
