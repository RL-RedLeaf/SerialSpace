# 串口触发空格模拟器

一个在 Windows 上运行的 Python 脚本：当指定串口收到文本行 `"space"` 时，模拟按下空格键。

## 依赖
- Python 3.8+
- `pyserial`：安装命令 `pip install pyserial`

## 使用方法
1. 连接串口设备，确认端口号（如 `COM3`）。
2. 在项目目录运行：
   ```bash
   python serial_space.py --port COM3 --baud 9600
   ```
   - `--port` 必填：串口名称。
   - `--baud` 可选：波特率，默认 `9600`。
3. 串口设备需按行发送数据（带换行符）。当接收到一行内容为 `space`（不区分大小写）时，脚本会在本机模拟一次空格键。

## 注意事项
- 仅支持 Windows（使用 WinAPI 模拟键盘）。
- 请确保以有权限的用户运行（某些环境可能需要管理员权限才能发送键盘事件）。
- 停止程序：按 `Ctrl+C`。
