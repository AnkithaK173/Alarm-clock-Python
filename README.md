
# Alarm Clock Application

## Project Overview

This project is a Python-based **Alarm Clock** application with a graphical user interface (GUI) created using the Tkinter library. The application allows users to set an alarm for a specific time. When the current time matches the user-set time, a message is displayed, and a sound is played.

## Features

- **Set Alarm Time**: Choose a time in hours, minutes, and seconds.
- **Audio Alert**: Plays an alarm sound at the set time.
- **Real-time Clock Check**: Continuously monitors the current time to trigger the alarm when it matches the set time.

## How to Run the Application

1. **Install Requirements**:
   - Ensure that `Tkinter` and `simpleaudio` are installed. You can install `simpleaudio` with:
     ```bash
     pip install simpleaudio
     ```

2. **Run the Script**:
   - Run the script using Python:
     ```bash
     python alarm_clock.py
     ```

3. **Set Alarm**:
   - Open the application, set the desired time using the dropdowns, and click "Set Alarm" to start the alarm clock.

## File Structure

- **alarm_clock.py**: Contains the main script, including functions for setting the alarm and the GUI.
- **sound.wav**: The sound file played as the alarm.

## Project Code Explanation

### Key Functions

1. **`set_alarm`**: Checks the current time against the user-specified alarm time.
2. **`alarm_message`**: Plays the alarm sound and displays the alert message.
3. **Tkinter GUI**: Provides a user interface for selecting the alarm time and setting it.

### Dependencies

- **Python 3**
- **Tkinter**: Standard Python library for GUI applications.
- **simpleaudio**: For playing the alarm sound.

## Example Interface

The GUI shows three dropdowns to select hours, minutes, and seconds, a "Set Time" button, and an area to display the current alarm status.

## Future Improvements

- Add a snooze button to allow temporary dismissal of the alarm.
- Add multiple alarm settings.
- Display the remaining time until the alarm triggers.

---

This project demonstrates the use of Tkinter for building GUIs and the `simpleaudio` library for audio playback in Python.


<img src="Screenshot 2022-11-27 122619.png">
