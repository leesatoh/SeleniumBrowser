import subprocess
from os.path import expanduser

import SearchExe


class MyChrome:
    popen = None

    def __init__(self, port):
        self.exe_path = SearchExe.do_search("google", "Chrome.exe")
        self.debugging_port_option = f'--remote-debugging-port={port}'
        self.user_data_option = f'--user-data-dir={expanduser("~")}\AppData\Local\Google\Chrome\AutoBrowserProfile-{port}'

    def __del__(self):
        self.stop()

    def start(self):
        if self.exe_path is None:
            print("Chrome.exeを見つけることができませんでした。Chrome.exeの場所を管理者に提示して改修する必要があります。")
            return
        try:
            # TODO:OPTIONは配列で渡せるほうが良いか
            print(f"path:{self.exe_path} を実行します。")
            self.popen = subprocess.Popen((self.exe_path, self.debugging_port_option, self.user_data_option))
            if self.popen is not None and self.popen.returncode is not None and self.popen.returncode != 0:
                print(f"return : {self.popen.returncode}")
                print(self.popen)
                # TODO:エラー処理が必要
        except subprocess.SubprocessError as e:
            print(f"SubprocessError:{e}")
        except subprocess.CalledProcessError as e:
            print(f"CalledProcessError:{e}")

    def stop(self):
        if self.popen is not None:
            self.popen.kill()
            self.popen = None
