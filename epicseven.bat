@echo off
:6
echo.
echo ����1�󰴻س���ÿ������(��Ԩ�����������Թ����ˡ������ʯ)
echo ����2�󰴻س���ˢ��ǩ
echo ����3�󰴻س���Զ��
echo ����4�󰴻س���ˢ9-4
echo ����5�󰴻س����˳�
echo.
set /p start=ѡ�����ֺ󰴻س���
if "%start%"=="1" goto 1
if "%start%"=="2" goto 2
if "%start%"=="3" goto 3
if "%start%"=="4" goto 4
if "%start%"=="5" goto 5
:1
@echo off
cd C:\Users\%USERNAME%\Desktop\epicseven\daily
python daily.py
echo ִ�����
goto 6
:2
@echo off
C:
cd C:\Users\%USERNAME%\Desktop\epicseven\key
set /p num1=������ǩ�����󰴻س���
python key.py "%num1%"
echo ִ�����
goto 6
:3
@echo off
C:
cd C:\Users\%USERNAME%\Desktop\epicseven\expedition
set /p num3=����ִ�е�Զ������(���������ϡ����ϡ���)�󰴻س���
python expedition.py "%num3:~0,1%" "%num3:~2,1%" "%num3:~4,1%"
echo ִ�����
goto 6
:4
@echo off
C:
cd C:\Users\%USERNAME%\Desktop\epicseven\9-4
set /p num2=����ִ�д����󰴻س���
python 9-4.py "%num2%"
echo ִ�����
goto 6
:5
Exit
