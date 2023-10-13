import eel
import subprocess


@eel.expose
def set_shutdown_timer(seconds: int) -> None:
    subprocess.Popen(
        "C:\\Windows\\System32\\shutdown.exe -s -t " + str(seconds) + " -f",
        shell=True
    ).wait()


@eel.expose
def cancel_shutdown_timer() -> None:
    subprocess.Popen(
        "C:\\Windows\\System32\\shutdown.exe -a",
        shell=True
    ).wait()


eel.init('web')
eel.start('index.html', size=(300, 400), port=0)
