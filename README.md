# 🦁 Zootopia Animal Generator

A Python project that fetches animal information from the API Ninjas platform and generates a beautiful HTML page with animal cards.

## 📋 Project Description

This project allows users to:
- Enter animal names and receive information about these animals
- View the information in the form of attractive HTML cards
- See scientific names, family, diet, habitat, and distribution of animals

## 🛠 Installation

1. Clone the repository (use HTTPS):
```bash
git clone https://github.com/Ozancico/Zootopia-API.git
cd Zootopia-API
```

2. Create a new .env file and add your API key:
```bash
echo "API_KEY=your_api_key_here" > .env
```

3. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # For Unix/macOS
# OR
venv\Scripts\activate  # For Windows
```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

⚠️ **Important Note**: The `.env` file is not cloned with the repository. You must create it in each environment and add your API key.

## 🚀 Usage

1. Run the main program:
```bash
python animals_web_generator.py
```

2. Enter an animal name when prompted
3. The generated HTML page will be saved as `animals.html`
4. Open `animals.html` in your browser to see the animal cards

## 🌟 Features

- Dynamic querying of animal information via the API Ninjas platform
- Beautiful, responsive HTML cards for each animal
- Error handling for animals not found
- Secure handling of API keys through environment variables

## 📝 Notes

- You need an API key from [API Ninjas](https://api-ninjas.com)
- Make sure your API key is correctly configured in the `.env` file
- The program handles errors gracefully and provides helpful feedback

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:
- Suggest new features
- Report bugs
- Submit code improvements
- Improve documentation

## 📄 License

This project is licensed under the MIT License.
