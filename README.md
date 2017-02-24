## 安装方法
我们使用virtualenv来管理Python环境，yum安装需切到root账号
```bash
yum install -y python-virtualenv

$ cd /path/to/weixin_api/
$ virtualenv ./env

$ ./env/bin/pip install -r pip_requirements.txt
```
## 进程管理
统一使用的minos的管理工具control
```bash
./control start 启动进程
./control stop 停止进程
./control restart 重启进程
./control status 查看进程状态
./control tail 用tail -f的方式查看var/app.log
```
