import eel
import subprocess
import tempfile
import os
import json
import time

TEMP_FILE_PATH = os.path.join(tempfile.gettempdir(), "sleep_timer.json")


@eel.expose
def set_shutdown_timer(seconds: int) -> None:
    subprocess.Popen(
        "C:\\Windows\\System32\\shutdown.exe -s -t " + str(seconds) + " -f",
        shell=True
    ).wait()
    with open(TEMP_FILE_PATH, 'w') as file:
        json.dump(
            {
                "set time": int(time.time()),
                "amount": seconds
            },
            file,
            indent=4
        )


@eel.expose
def cancel_shutdown_timer() -> None:
    subprocess.Popen(
        "C:\\Windows\\System32\\shutdown.exe -a",
        shell=True
    ).wait()
    try:
        os.remove(TEMP_FILE_PATH)
    except Exception:
        pass


@eel.expose
def get_shutdown_time_left() -> int:
    try:
        with open(TEMP_FILE_PATH) as file:
            data = json.load(file)
            now = time.time()
            return data["amount"] + data["set time"] - int(now)
    except Exception:
        try:
            os.remove(TEMP_FILE_PATH)
        except Exception:
            pass
        return -1


if __name__ == "__main__":
    eel.init('web')
    eel.start('index.html', size=(300, 450), port=0)
