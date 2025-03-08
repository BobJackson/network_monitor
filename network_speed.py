import rumps
import psutil
import time

class NetworkSpeedApp(rumps.App):
    def __init__(self):
        super(NetworkSpeedApp, self).__init__("🌐")
        self.last_received = psutil.net_io_counters().bytes_recv
        self.last_sent = psutil.net_io_counters().bytes_sent
        self.timer = rumps.Timer(self.update_speed, 1)
        self.timer.start()

    def format_speed(self, bytes_per_sec):
        """将字节速度转换为人类可读格式"""
        if bytes_per_sec >= 1024 * 1024:  # MB/s
            return f"{bytes_per_sec / (1024 * 1024):.1f} MB/s"
        elif bytes_per_sec >= 1024:  # KB/s
            return f"{bytes_per_sec / 1024:.1f} KB/s"
        else:  # B/s
            return f"{bytes_per_sec:.1f} B/s"

    def update_speed(self, _):
        """更新网速显示"""
        current = psutil.net_io_counters()
        current_received = current.bytes_recv
        current_sent = current.bytes_sent

        down_speed = current_received - self.last_received
        up_speed = current_sent - self.last_sent

        self.last_received = current_received
        self.last_sent = current_sent

        self.title = f"↓{self.format_speed(down_speed)} ↑{self.format_speed(up_speed)}"

if __name__ == "__main__":
    NetworkSpeedApp().run()
    