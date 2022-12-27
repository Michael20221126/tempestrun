# tempestrun（暴风雨奔跑）

一个汉化版的游戏，内部有玩法介绍

# 如何运行
  
  ## 法一：下载setup.exe,可运行exe版（win64）
  
    git clone https://github.com/Michael20221126/tempestrun
    cd tempestrun/TempestRun
    ./setup.exe

  ## 法二：源代码运行
  
    git clone https://github.com/Michael20221126/tempestrun
    cd tempestrun/TempestRun
    pip install -r requirements.txt
    python main.py

  ## 法三：打包成可执行文件
  
    git clone https://github.com/Michael20221126/tempestrun
    cd tempestrun/TempestRun
    python -m venv venv
    ./venv/Scripts/activate.bat
    pip install -r requirements.txt
    pip install cx_freeze
    python cxsetup.py

# 最后，祝你玩的开心愉快
