var ui_input;

async function SetShutdownTimer(seconds) {
    await eel.cancel_shutdown_timer()();
    await eel.set_shutdown_timer(seconds)(() => GetTimeLeft());
}

async function CancelShutdownTimer() {
    await eel.cancel_shutdown_timer()(() => GetTimeLeft());
}

async function OnLoad() {
    ui_input = document.getElementById("ui_input");
    GetTimeLeft();
    setInterval(function() {GetTimeLeft()}, 30000);
}

function GetTimeLeft() {
    eel.get_shutdown_time_left()(time_left => {
        if (time_left == -1) {
            ui_input.value = "";
        } else {
            hours = Math.floor(time_left / 3600);
            seconds = time_left % 3600;
            minutes = Math.round(seconds / 60);
            if (minutes == 60) {
                hours += 1;
                minutes = 0;
            }
            hours_text = hours.toString();
            while (hours_text.length < 2) hours_text = "0" + hours_text;
            minutes_text = minutes.toString();
            while (minutes_text.length < 2) minutes_text = "0" + minutes_text;
            ui_input.value = hours_text + ":" + minutes_text;
        }
    });
}