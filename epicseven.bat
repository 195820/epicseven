@echo off
:7
echo.
echo ����1�󰴻س���ÿ������(��Ԩ��������npc���Թ����ˡ������ʯ)
echo ����2�󰴻س���ˢ��ǩ
echo ����3�󰴻س���Զ��(�������ǹ���)
echo ����4�󰴻س���ˢ9-4
echo ����5�󰴻س����Թ�
echo ����6�󰴻س����˳�
echo.
set /p start=ѡ�����ֺ󰴻س���
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
echo ִ�����
goto 7
:2
@echo off
C:
cd C:\Users\%USERNAME%\Desktop\epicseven\key
set /p num1=������ǩ�����󰴻س���
python key.py "%num1%"
echo ִ�����
goto 7
:3
@echo off
C:
cd C:\Users\%USERNAME%\Desktop\epicseven\expedition
echo ����1�󰴻س����ǹ���Զ��
echo ����2�󰴻س�������Զ��
echo.
set /p start1=ѡ�����ֺ󰴻س���
if "%start1%"=="2" goto 8
set /p num3=����ִ�е�Զ������(���������ϡ����ϡ���)�󰴻س���
python expedition.py "%num3:~0,1%" "%num3:~2,1%" "%num3:~4,1%"
echo ִ�����
goto 7
��8
set /p num3=����ִ�е�Զ������(���������ϡ����ϡ���)�󰴻س���
python expedition1.py "%num3:~0,1%" "%num3:~2,1%" "%num3:~4,1%"
echo ִ�����
goto 7
:4
@echo off
C:
cd C:\Users\%USERNAME%\Desktop\epicseven\9-4
set /p num2=����ִ�д����󰴻س���
python 9-4.py "%num2%"
echo ִ�����
goto 7
:5
cd C:\Users\%USERNAME%\Desktop\epicseven\mazen
set /p num4=�Թ�����(2,3)��
if "%num4%"=="2" python mazen.py
if "%num4%"=="3" python mazen1.py
:6
Exit
