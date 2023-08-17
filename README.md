# WeChat_Run
注意！本项目必须下载注册**Zepp_life**并绑定微信 账号（Email or phone）和密码 就是你的Zeep_life的账号和密码<br>
使用Python和Github Actions每日定时WeChat（微信）刷步
# 使用 & 配置
## 请先Fork本项目
如下配置完后在Actions启动试试<br>
`Setting - Secrets and variables - Actinos - New repository secret`<br>
Secrets按如下填写：
| Name        | secret      |
| ----------- | ----------- |
| PHONE       | (填写你的账号) |
| PASSWORD    | (填写你的密码) |
| RUN         | (填写跑步数量) |
| RUN_END     | (填写结束数量) |

注：`PHONE`、`PASSWORD`、`RUN`为必填项<br>
想在某个数量之间的话请多添加一个`RUN_END`，最终结果将会在`RUN`和`RUN_END`之间<br>
时间相关的修改`.github/workflows/test.yml`旁边有相关的注释
``` bash
  schedule:
  # 定时任务，在每天的5点执行
    - cron: '0 21 * * *'
```
注意！北京时间比Github所使用时区快8个小时<br>
所以这里的`- cron: '0 21 * * *'`其实就是`(21 + 8) % 24 = 5`其中的 5 就是我们时间的早上5点
