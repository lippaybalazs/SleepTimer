async function set_shutdown_timer(seconds) {
    await eel.cancel_shutdown_timer()();
    await eel.set_shutdown_timer(seconds)();
}

async function cancel_shutdown_timer() {
    await eel.cancel_shutdown_timer()();
}