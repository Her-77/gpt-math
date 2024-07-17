# gpt-math

## 文件结构
.
├───backend         // 后端目录  
│   ├───agents      // agents 定义  
│   └───templates   // 网页模板  
├───frontend        // 前端目录  
├───app.py          // 运行脚本文件，运行该文件即可运行本项目  
├───false_res.csv   // 系统测试输入，该文件包含一些 gpt-4 回答错误的问题及答案  
├───package.json  
├───package-lock.json  
├───requirements.txt  
└───outputs         // 系统测试输出  

## 环境配置
在Windows环境： 
conda create -n gpt-math python=3.12  
pip install -r requirements.txt  
缺啥补啥，报啥错解决啥错，环境配置可以参考 github 上的 gpt-newspaper 项目  
OpenAI API及Windows环境变量需要自行配置  

## 测试运行
python app.py
