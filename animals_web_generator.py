"""
Zootopia Animal Generator - A program that generates HTML pages with animal information.

This program fetches animal data from the API Ninjas platform and creates beautiful
HTML cards displaying information about the requested animals. If an animal is not found,
it generates an HTML page with an appropriate error message.
"""

import sys
from data_fetcher import fetch_data

def read_template(template_path: str) -> str:
    """
    Read the HTML template file from the specified path.

    Args:
        template_path (str): The path to the template file

    Returns:
        str: The contents of the template file or None if file not found
    """
    try:
        with open(template_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"⚠️ Template file {template_path} not found!")
        return None

def create_animal_card(animal: dict) -> str:
    """
    Create an HTML card for a single animal.

    Args:
        animal (dict): Dictionary containing animal data from the API

    Returns:
        str: HTML string representing the animal card
    """
    # Safe extraction of required keys
    name = animal.get('name', 'Unknown')

    # Extract taxonomy information safely
    taxonomy = animal.get('taxonomy', {})
    scientific_name = taxonomy.get('scientific_name', 'Not available')
    family = taxonomy.get('family', 'Not available')

    # Extract characteristics safely
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet', 'Not available')
    habitat = characteristics.get('habitat', 'Not available')

    # Create the locations list safely
    locations = animal.get('locations', ['Not available'])
    locations_html = '<br>'.join(locations) if locations else 'Not available'

    return f"""
        <li class="cards__item">
            <div class="card__content">
                <div class="card__title">{name}</div>
                <p class="card__text">
                    <strong>Scientific Name:</strong> {scientific_name}<br>
                    <strong>Family:</strong> {family}<br>
                    <strong>Diet:</strong> {diet}<br>
                    <strong>Habitat:</strong> {habitat}<br>
                    <strong>Distribution:</strong><br> {locations_html}
                </p>
            </div>
        </li>
    """

def create_error_message(animal_name: str) -> str:
    """
    Create an HTML error message when an animal is not found.

    Args:
        animal_name (str): The name of the animal that was searched for

    Returns:
        str: HTML string containing the error message
    """
    return f"""
        <li class="cards__item">
            <div class="card__content">
                <div class="card__title">Animal Not Found</div>
                <p class="card__text">
                    <strong>Note:</strong> The animal "{animal_name}" could not be found in the database.<br>
                    Please try another animal name (e.g., "Lion", "Elephant", "Penguin").
                </p>
            </div>
        </li>
    """

def generate_html_content(animals: list, search_term: str) -> str:
    """
    Generate HTML content for either the animal cards or an error message.

    Args:
        animals (list): List of animal dictionaries from the API
        search_term (str): The animal name that was searched for

    Returns:
        str: Complete HTML content for the animal cards or error message
    """
    if not animals:
        return create_error_message(search_term)
    return ''.join(create_animal_card(animal) for animal in animals)

def write_output_file(content: str, output_path: str) -> None:
    """
    Write the generated HTML content to an output file.

    Args:
        content (str): The complete HTML content to write
        output_path (str): The path where the file should be written

    Returns:
        None
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"\n✅ Website was successfully generated to {output_path}")
        print(f"   You can now open the file in your browser!")
    except Exception as e:
        print(f"\n⚠️ Error writing file: {str(e)}")

def main():
    """
    Main function that coordinates the animal information retrieval and HTML generation process.

    This function:
    1. Prompts the user for an animal name
    2. Fetches animal data from the API
    3. Generates an HTML page with either animal information or an error message
    4. Saves the result to a file
    """
    # Constants
    TEMPLATE_PATH = 'animals_template.html'
    OUTPUT_PATH = 'animals.html'

    # User input
    print("\n🔍 Welcome to Zootopia Animal Generator!")
    print("   Enter an animal name to get information about it.")
    animal_name = input("\nAnimal name: ").strip()

    if not animal_name:
        print("\n⚠️ Please enter an animal name!")
        return

    print(f"\n🌐 Searching for information about '{animal_name}'...")

    # Read template
    template = read_template(TEMPLATE_PATH)
    if not template:
        return

    # Fetch animal data from API
    animals = fetch_data(animal_name)

    # Generate HTML content (either animal cards or error message)
    html_content = generate_html_content(animals, animal_name)

    # Replace template and write file
    final_html = template.replace('__REPLACE_ANIMALS_INFO__', html_content)
    write_output_file(final_html, OUTPUT_PATH)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program terminated.")
        sys.exit(0)
