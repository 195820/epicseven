@echo off
:6
echo.
echo 输入1后按回车，每日任务(深渊、竞技场、迷宫商人、领天空石)
echo 输入2后按回车，刷书签
echo 输入3后按回车，远征
echo 输入4后按回车，刷9-4
echo 输入5后按回车，退出
echo.
set /p start=选择数字后按回车：
if "%start%"=="1" goto 1
if "%start%"=="2" goto 2
if "%start%"=="3" goto 3
if "%start%"=="4" goto 4
if "%start%"=="5" goto 5
:1
@echo off
cd C:\Users\%USERNAME%\Desktop\epicseven\daily
python daily.py
echo 执行完成
goto 6
:2
@echo off
C:
cd C:\Users\%USERNAME%\Desktop\epicseven\key
set /p num1=设置书签数量后按回车：
python key.py "%num1%"
echo 执行完成
goto 6
:3
@echo off
C:
cd C:\Users\%USERNAME%\Desktop\epicseven\expedition
set /p num3=设置执行的远征类型(按次序左上、右上、下)后按回车：
python expedition.py "%num3:~0,1%" "%num3:~2,1%" "%num3:~4,1%"
echo 执行完成
goto 6
:4
@echo off
C:
cd C:\Users\%USERNAME%\Desktop\epicseven\9-4
set /p num2=设置执行次数后按回车：
python 9-4.py "%num2%"
echo 执行完成
goto 6
:5
Exit
