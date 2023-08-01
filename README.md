# Text to Speech Converter

This is a simple Python script that converts text to speech using the `gtts` (Google Text-to-Speech) library. The script allows the user to input text, saves it to a file, and then converts the text to speech.

## How to Use

1. Run the Python script in a Python environment with the required dependencies installed.
2. The script will prompt you to enter the text you want to convert to speech.
3. After entering the text, the script will save it to a file called "a.txt" in the same directory.
4. The script will then use the `gtts` library to convert the text to speech in English.
5. The speech output will be saved as "welcome.mp3" in the same directory.
6. The converted speech will be played automatically.

## Concepts Used

1. **File Handling**: The script uses file handling to read the text from "a.txt" and write the user input into the file.

2. **Text-to-Speech Conversion**: The `gtts` library is used to convert the text to speech in English.

3. **Command-Line Input**: The script takes user input from the command line using the `input()` function.

4. **OS Interaction**: The script uses the `os` module to check if the "a.txt" file exists and to play the generated speech using the operating system's default player.

## Dependencies

The script requires the `gtts` library, which can be installed using the following command:
```
pip install gtts
```

## Acknowledgments

The Text to Speech Converter was created by Harsh Gupta (Desparete Enuf) as a simple utility to convert text to speech using the Google Text-to-Speech API. The code is provided here for reference and learning purposes.

## License

This project is open-source and licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code, but please provide proper attribution to the original creator, Harsh Gupta (Desparete Enuf).
