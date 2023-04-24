from PIL import Image, ImageDraw, ImageFont

def create_stats_image(player_name, stats, background_path):
    # Open the background image
    img = Image.open(background_path)

    # If the background image is not 600x600, resize it
    if img.width != 600 or img.height != 600:
        img = img.resize((600, 600))

    draw = ImageDraw.Draw(img)
    
    #Font family for the stat image generation
    skill_font_fam = 'Verdana'
    title_font_fam = 'OLD'

    # Load the font for skill stats
    font = ImageFont.truetype(f"./resources/{skill_font_fam}.ttf", 16)
    
    # Load a separate font for the title with a larger size and different style, if desired
    title_font = ImageFont.truetype(f"./resources/{title_font_fam}.ttf", 36)


    # Draw the title
    title = f"Stats for {player_name}"
    title_size = draw.textsize(title, font=title_font)
    draw.text(((img.width - title_size[0]) // 2, 10), title, (0, 0, 0), font=title_font)

    # Draw the stats in a grid
    columns = 4
    spacing = 60
    x_offset = 35
    y_offset = 80

    # Text color (change these values to get better contrast)
    text_color = (255, 255, 255)
    outline_color = (0, 0, 0)
    outline_width = 1

    # Dictionary with logical shortened names for the skills (max 6 characters)
    shortened_skill_names = {
        'Archaeology' : 'Arch',
        'Attack': 'Attack',
        'Strength': 'Str',
        'Defence': 'Def',
        'Ranged': 'Ranged',
        'Prayer': 'Prayer',
        'Magic': 'Magic',
        'Runecrafting': 'Runecr',
        'Construction': 'Constr',
        'Dungeoneering': 'Dung',
        'Constitution': 'Const',
        'Agility': 'Agil',
        'Herblore': 'Herb',
        'Thieving': 'Thieve',
        'Crafting': 'Craft',
        'Fletching': 'Fletch',
        'Slayer': 'Slayer',
        'Hunter': 'Hunter',
        'Divination': 'Divin',
        'Mining': 'Mining',
        'Smithing': 'Smith',
        'Fishing': 'Fish',
        'Cooking': 'Cook',
        'Firemaking': 'Firemk',
        'Woodcutting': 'Woodct',
        'Farming': 'Farm',
        'Summoning': 'Summ',
        'Invention': 'Invent',
    }

    # Sort stats alphabetically by skill name
    sorted_stats = sorted(stats, key=lambda x: x['skillname'].lower())

    spacing_reduction = 10  # Adjust this value to change column spacing
    
    for i, stat in enumerate(sorted_stats):
        row = i // columns
        col = i % columns
        x = x_offset + col * ((img.width // columns) - spacing_reduction)
        y = y_offset + row * spacing

        # Use the shortened skill name if it exists
        skill_name = shortened_skill_names.get(stat['skillname'].capitalize(), stat['skillname'].capitalize())


        # Capitalize the first letter of the skill name
        skill_name = skill_name.capitalize()

        skill_text = f"{skill_name}: {stat['level']}"
        xp_text = f"XP: {stat['xp'] / 1_000_000:.1f}M"

        # Draw skill text outline
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width + 1):
                draw.text((x + dx, y + dy), skill_text, outline_color, font=font)

        # Draw skill text
        draw.text((x, y), skill_text, text_color, font=font)

        # Draw XP text outline
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width + 1):
                draw.text((x + dx, y + dy + 20), xp_text, outline_color, font=font)

        # Draw XP text
        draw.text((x, y + 20), xp_text, text_color, font=font)

    return img