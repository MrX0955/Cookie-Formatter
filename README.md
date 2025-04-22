# 🍪 Cookie Formatter

## 📝 About the Project
Cookie Formatter is a simple Python tool that converts cookies exported from browsers into a readable and usable format. It takes cookie files in JSON format and arranges each cookie in a "name=value" format.

## ✨ Features
- Process cookie files in JSON format
- Handle multiple JSON objects at once
- Format cookies in "name=value" format
- Save results to a text file

## 🚀 Usage
1. Clone the project:
   ```
   git clone https://github.com/MrX0955/Cookie_Formatter.git
   cd Cookie_Formatter
   ```

2. Run the Python script:
   ```
   python Cookie_Formatter.py
   ```

4. Once the process is complete, the formatted cookies will be saved to the `cookies.txt` file.

## 📋 Input File Format
The input file should be in JSON format, similar to the following structure:

```json
[
    {
        "domain": ".example.com",
        "expirationDate": 1775322283,
        "name": "cookie_name",
        "value": "cookie_value"
    },
    ...
]
```

The file can contain multiple JSON arrays. The program will automatically detect and process these arrays.

## 📤 Output Format
The program saves cookies to the `cookies.txt` file in the following format:

```
cookie_name1=cookie_value1; cookie_name2=cookie_value2; ...
```

A separate line is created for each JSON array.

## ⚠️ Important Notes
- The input file must be in valid JSON format.
- Each cookie object must have "name" and "value" fields.

## 🛠️ Requirements
- Python 3.x

## 📄 License
This project is licensed under the [MIT License](LICENSE). 

## ⚠️ DISCLAIMER 
**This github repo is for EDUCATIONAL PURPOSES ONLY. I am NOT under any responsibility if a problem occurs.**
