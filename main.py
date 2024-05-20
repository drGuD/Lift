import kivy
import os
import csv
from datetime import datetime
import pandas as pd
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

#__FUNKCIONALNO__________________________________
### 1. PREVERI SAVE.csv, DRUGAČE USTVARI
# Define the file name Roke
file_name_roke = "Roke.csv"
# Check if the file exists Roke
if not os.path.isfile(file_name_roke):
    # Define the columns for ROKE
    columns = [
        'TxT_Id', 'Txt_Datum', 'Txt_butterfly', 'Slider_butterfly', 'Txt_delt', 'Slider_delt',
        'Txt_raise', 'Slider_raise', 'Txt_pull', 'Slider_pull', 'Txt_press', 'Slider_press',
        'Txt_row', 'Slider_row', 'Txt_abdomen', 'Slider_abdomen', 'Txt_back', 'Slider_back',
        'Txt_biceps', 'Slider_biceps', 'Txt_triceps', 'Slider_triceps'
    ]
    # Create an empty DataFrame with the columns
    df = pd.DataFrame(columns=columns)
    # Save the DataFrame to a CSV file with a semicolon delimiter
    df.to_csv(file_name_roke, index=False, sep=';')

# Define the file name Noge
file_name_noge = "Noge.csv"
# Check if the file exists Noge
if not os.path.isfile(file_name_noge):
    # Define the columns for NOGE
    columns = [
        'TxT_Id', 'Txt_Datum', 'Txt_calf', 'Slider_calf', 'Txt_curl', 'Slider_curl',
        'Txt_glute', 'Slider_glute', 'Txt_adductor', 'Slider_adductor', 'Txt_abductor', 'Slider_abductor',
        'Txt_extension', 'Slider_extension', 'Txt_leg', 'Slider_leg'
    ]
    # Create an empty DataFrame with the columns
    df = pd.DataFrame(columns=columns)
    # Save the DataFrame to a CSV file with a semicolon delimiter
    df.to_csv(file_name_noge, index=False, sep=';')
#___________________________________

class Home_Widget(Screen):
    name = StringProperty()

    def __init__(self, **kwargs):
        super(Home_Widget, self).__init__(**kwargs)
        self.name = kwargs.get('name', 'Home_Widget')

    def on_btn_roke_press(self):  # Define a method for button click
        self.manager.current = 'roke_widget'  # Switch to Roke_Widget screen

    def on_btn_noge_press(self):  # Define a method for button click
        self.manager.current = 'noge_widget'  # Switch to Roke_Widget screen

class Roke_Widget(Screen):
    navodila_text = StringProperty()
    dan_text = StringProperty()
    mesec_text = StringProperty()
    leto_text = StringProperty()
    butterfly_text = StringProperty()
    butterfly_value = NumericProperty()
    delt_text = StringProperty()
    delt_value = NumericProperty()
    raise_text = StringProperty()
    raise_value = NumericProperty()
    pull_text = StringProperty()
    pull_value = NumericProperty()
    press_text = StringProperty()
    press_value = NumericProperty()
    row_text = StringProperty()
    row_value = NumericProperty()
    abdomen_text = StringProperty()
    abdomen_value = NumericProperty()
    back_text = StringProperty()
    back_value = NumericProperty()
    biceps_text = StringProperty()
    biceps_value = NumericProperty()
    triceps_text = StringProperty()
    triceps_value = NumericProperty()

    def __init__(self, **kwargs):
        super(Roke_Widget, self).__init__(**kwargs)
        self.initialize_properties()

    def initialize_properties(self):
        self.navodila_text = ""
        self.dan_text = ""
        self.mesec_text = ""
        self.leto_text = ""
        self.butterfly_text = ""
        self.delt_text = ""
        self.raise_text = ""
        self.pull_text = ""
        self.press_text = ""
        self.row_text = ""
        self.abdomen_text = ""
        self.back_text = ""
        self.biceps_text = ""
        self.triceps_text = ""
        self.butterfly_value = 2.0
        self.delt_value = 2.0
        self.raise_value = 2.0
        self.pull_value = 2.0
        self.press_value = 2.0
        self.row_value = 2.0
        self.abdomen_value = 2.0
        self.back_value = 2.0
        self.biceps_value = 2.0
        self.triceps_value = 2.0


    def on_dan_text(self, instance, value):
        print("Dan spremenjen v:", value)
    def on_dan_value(self, instance, value):
        print("Dan_value spremenjen v:", value)
    def on_mesec_text(self, instance, value):
        print("Mesec spremenjen v:", value)
    def on_mesec_value(self, instance, value):
        print("Mesec_value spremenjen v:", value)
    def on_leto_text(self, instance, value):
        print("Leto spremenjen v:", value)
    def on_leto_value(self, instance, value):
        print("Leto_value spremenjen v:", value)
    def on_butterfly_text(self, instance, value):
        print("Butterfly spremenjen v:", value)
    def on_butterfly_value(self, instance, value):
        print("Butterfly_value spremenjen v:", value)
    def on_delt_text(self, instance, value):
        print("Delt spremenjen v:", value)
    def on_delt_value(self, instance, value):
        print("Delt_value spremenjen v:", value)
    def on_raise_text(self, instance, value):
        print("Raise spremenjen v:", value)
    def on_raise_value(self, instance, value):
        print("Raise_value spremenjen v:", value)
    def on_pull_text(self, instance, value):
        print("Pull spremenjen v:", value)
    def on_pull_value(self, instance, value):
        print("Pull_value spremenjen v:", value)
    def on_press_text(self, instance, value):
        print("Press spremenjen v:", value)
    def on_press_value(self, instance, value):
        print("Press_value spremenjen v:", value)
    def on_row_text(self, instance, value):
        print("Row spremenjen v:", value)
    def on_row_value(self, instance, value):
        print("Row_value spremenjen v:", value)
    def on_abdomen_text(self, instance, value):
        print("Abdomen spremenjen v:", value)
    def on_abdomen_value(self, instance, value):
        print("Abdomen_value spremenjen v:", value)
    def on_back_text(self, instance, value):
        print("Back spremenjen v:", value)
    def on_back_value(self, instance, value):
        print("Back_value spremenjen v:", value)
    def on_biceps_text(self, instance, value):
        print("Biceps spremenjen v:", value)
    def on_biceps_value(self, instance, value):
        print("Biceps_value spremenjen v:", value)
    def on_triceps_text(self, instance, value):
        print("Triceps spremenjen v:", value)
    def on_triceps_value(self, instance, value):
        print("Triceps_value spremenjen v:", value)

    def pocisti_vse(self):
        self.initialize_properties()
        self.ids.Txt_navodila.text = self.navodila_text

    def button_home(self):  # Define a method for button click
            self.manager.current = 'home_widget'  # Switch to Roke_Widget screen

    def button_save(self):
        # Ensure that the attributes are already set
        assert hasattr(self, 'dan_text')
        assert hasattr(self, 'mesec_text')
        assert hasattr(self, 'leto_text')
        assert hasattr(self, 'butterfly_text')
        assert hasattr(self, 'butterfly_value')
        assert hasattr(self, 'delt_text')
        assert hasattr(self, 'delt_value')
        assert hasattr(self, 'raise_text')
        assert hasattr(self, 'raise_value')
        assert hasattr(self, 'pull_text')
        assert hasattr(self, 'pull_value')
        assert hasattr(self, 'press_text')
        assert hasattr(self, 'press_value')
        assert hasattr(self, 'row_text')
        assert hasattr(self, 'row_value')
        assert hasattr(self, 'abdomen_text')
        assert hasattr(self, 'abdomen_value')
        assert hasattr(self, 'back_text')
        assert hasattr(self, 'back_value')
        assert hasattr(self, 'biceps_text')
        assert hasattr(self, 'biceps_value')
        assert hasattr(self, 'triceps_text')
        assert hasattr(self, 'triceps_value')

        # The filename
        filename = 'Roke.csv'

        # Check if the file exists in the current directory
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"File '{filename}' does not exist in the current directory")

        # Read the CSV file
        with open(filename, 'r', newline='') as csvfile:
            reader = list(csv.reader(csvfile, delimiter=';'))

        # Find the first completely empty row
        empty_row_index = None
        for i, row in enumerate(reader):
            if all(cell == '' for cell in row):
                empty_row_index = i
                break

        if empty_row_index is None:
            empty_row_index = len(reader)
            reader.append([])

        # Generate the new row to insert
        date_string = f"{self.dan_text}.{self.mesec_text}.{self.leto_text}"
        new_row = [
            empty_row_index,  # ID (empty_row_index to account for 0-based indexing)
            date_string,
            self.butterfly_text,
            self.butterfly_value,
            self.delt_text,
            self.delt_value,
            self.raise_text,
            self.raise_value,
            self.pull_text,
            self.pull_value,
            self.press_text,
            self.press_value,
            self.row_text,
            self.row_value,
            self.abdomen_text,
            self.abdomen_value,
            self.back_text,
            self.back_value,
            self.biceps_text,
            self.biceps_value,
            self.triceps_text,
            self.triceps_value
        ]

        # Ensure the row has enough columns by padding with empty strings if necessary
        if len(reader[empty_row_index]) < len(new_row):
            reader[empty_row_index].extend([''] * (len(new_row) - len(reader[empty_row_index])))

        # Insert the new row
        reader[empty_row_index][:len(new_row)] = new_row

        # Write back to the CSV file with semicolon delimiter
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerows(reader)

        print(f"Entry added to '{filename}' at row {empty_row_index + 1}")
        self.initialize_properties()
        self.ids.Txt_navodila.text = self.navodila_text

    def calculate_days(self, date_str):
        date_format = "%d.%m.%Y"
        last_training_date = datetime.strptime(date_str, date_format)
        today = datetime.now()
        delta = today - last_training_date
        return delta.days

    def get_text_from_csv(self):
        try:
            with open('Roke.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')  # Specify delimiter
                rows = list(reader)
                if len(rows) <= 1:  # Check if there is at most one row
                    return "Brez podatkov ..."
                else:
                    last_row = rows[-1]  # Accessing the last element directly
                    if len(last_row) >= 14:  # Ensure last row has enough elements
                        last_training_date = last_row[1]
                        days_since_last_training = self.calculate_days(last_training_date)
                        paragraph_suffix = "dnevi."
                        if days_since_last_training == 1:
                            paragraph_suffix = "dnevom."
                        elif days_since_last_training == 2:
                            paragraph_suffix = "dnevoma."
                        elif days_since_last_training > 2:
                            paragraph_suffix = "dnevi."

                        exercises = [
                            {"name": "Butterfly", "weight_index": 2, "difficulty_index": 3},
                            {"name": "Rear Delt fly", "weight_index": 4, "difficulty_index": 5},
                            {"name": "Lat. Raise", "weight_index": 6, "difficulty_index": 7},
                            {"name": "Div. Lat. Pull", "weight_index": 8, "difficulty_index": 9},
                            {"name": "Chest Press", "weight_index": 10, "difficulty_index": 11},
                            {"name": "Vertical row", "weight_index": 12, "difficulty_index": 13},
                            {"name": "Abdomen", "weight_index": 14, "difficulty_index": 15},
                            {"name": "Low Back", "weight_index": 16, "difficulty_index": 17},
                            {"name": "Biceps", "weight_index": 18, "difficulty_index": 19},
                            {"name": "Triceps", "weight_index": 20, "difficulty_index": 21}
                        ]

                        output = f"Zadnji trening je bil {last_row[1]},\n\nPred {days_since_last_training} {paragraph_suffix}\n\n"

                        for exercise in exercises:
                            weight_index = exercise["weight_index"]
                            difficulty_index = exercise["difficulty_index"]
                            weight = last_row[weight_index]
                            difficulty = last_row[difficulty_index]
                            weight_description = ""
                            if difficulty == "0.0":
                                weight_description = "Fail"
                            elif difficulty == "1.0":
                                weight_description = "Zelo težko"
                            elif difficulty == "2.0":
                                weight_description = "Naporno"
                            elif difficulty == "3.0":
                                weight_description = "Lahko"
                            elif difficulty == "4.0":
                                weight_description = "Zelo lahko"

                            output += f"{exercise['name']} = {weight} kg, {weight_description}\n"

                        return output
                    else:
                        return "Brez podatkov ..."
        except Exception as e:
            print("Error occurred:", e)  # Debugging print
            return "Brez podatkov ..."

    def button_lift_roke(self):
        # Get the current date
        current_date = datetime.now()

        # Extract day, month, and year
        dan_text = str(current_date.day)
        mesec_text = str(current_date.month)
        leto_text = str(current_date.year)

        # Update the TextInput widgets with the extracted values
        self.ids.Txt_dan.text = dan_text
        self.ids.Txt_mesec.text = mesec_text
        self.ids.Txt_leto.text = leto_text

        # Print the values
        print("dan_text =", dan_text)
        print("mesec_text =", mesec_text)
        print("leto_text =", leto_text)

        # Call navodila function to update Txt_navodila
        self.navodila()

    def navodila(self):
        navodila_text = self.get_text_from_csv()
        self.ids.Txt_navodila.text = navodila_text

class Noge_Widget(Screen):
    navodila_text_n = StringProperty()
    dan_text_n = StringProperty()
    mesec_text_n = StringProperty()
    leto_text_n = StringProperty()
    calf_text = StringProperty()
    calf_value = NumericProperty()
    curl_text = StringProperty()
    curl_value = NumericProperty()
    glute_text = StringProperty()
    glute_value = NumericProperty()
    adductor_text = StringProperty()
    adductor_value = NumericProperty()
    abductor_text = StringProperty()
    abductor_value = NumericProperty()
    extension_text = StringProperty()
    extension_value = NumericProperty()
    leg_text = StringProperty()
    leg_value = NumericProperty()


    def __init__(self, **kwargs):
        super(Noge_Widget, self).__init__(**kwargs)
        self.initialize_properties_n()

    def initialize_properties_n(self):
        self.navodila_text_n = ""
        self.dan_text_n = ""
        self.mesec_text_n = ""
        self.leto_text_n = ""
        self.calf_text = ""
        self.curl_text = ""
        self.glute_text = ""
        self.adductor_text = ""
        self.abductor_text = ""
        self.extension_text = ""
        self.leg_text = ""

        self.calf_value = 2.0
        self.curl_value = 2.0
        self.glute_value = 2.0
        self.adductor_value = 2.0
        self.abductor_value = 2.0
        self.extension_value = 2.0
        self.leg_value = 2.0

    #class debug_n:
    def on_dan_text_n(self, instance, value):
        print("Dan spremenjen v:", value)
    def on_mesec_text_n(self, instance, value):
        print("Mesec spremenjen v:", value)
    def on_leto_text_n(self, instance, value):
        print("Leto spremenjen v:", value)
    def on_calf_text(self, instance, value):
        print("Calf spremenjen v:", value)
    def on_calf_value(self, instance, value):
        print("Calf_value spremenjen v:", value)
    def on_curl_text(self, instance, value):
        print("Curl spremenjen v:", value)
    def on_curl_value(self, instance, value):
        print("Curl_value spremenjen v:", value)
    def on_glute_text(self, instance, value):
        print("Glute spremenjen v:", value)
    def on_glute_value(self, instance, value):
        print("Glute_value spremenjen v:", value)
    def on_adductor_text(self, instance, value):
        print("Adductor spremenjen v:", value)
    def on_adductor_value(self, instance, value):
        print("Adductor_value spremenjen v:", value)
    def on_abductor_text(self, instance, value):
        print("Abductor spremenjen v:", value)
    def on_abductor_value(self, instance, value):
        print("Abductor_value spremenjen v:", value)
    def on_extension_text(self, instance, value):
        print("Extension spremenjen v:", value)
    def on_extension_value(self, instance, value):
        print("Extension_value spremenjen v:", value)
    def on_leg_text(self, instance, value):
        print("Leg spremenjen v:", value)
    def on_leg_value(self, instance, value):
        print("Leg_value spremenjen v:", value)

    def pocisti_vse_n(self):
        self.initialize_properties_n()
        self.ids.Txt_navodila_n.text = self.navodila_text_n

    def button_home_n(self):  # Define a method for button click
            self.manager.current = 'home_widget'  # Switch to Roke_Widget screen

    def button_save_n(self):
        # Ensure that the attributes are already set
        assert hasattr(self, 'dan_text_n')
        assert hasattr(self, 'mesec_text_n')
        assert hasattr(self, 'leto_text_n')
        assert hasattr(self, 'calf_text')
        assert hasattr(self, 'calf_value')
        assert hasattr(self, 'curl_text')
        assert hasattr(self, 'curl_value')
        assert hasattr(self, 'glute_text')
        assert hasattr(self, 'glute_value')
        assert hasattr(self, 'adductor_text')
        assert hasattr(self, 'adductor_value')
        assert hasattr(self, 'abductor_text')
        assert hasattr(self, 'abductor_value')
        assert hasattr(self, 'extension_text')
        assert hasattr(self, 'extension_value')
        assert hasattr(self, 'leg_text')
        assert hasattr(self, 'leg_value')

        # The filename
        filename_n = 'Noge.csv'

        # Check if the file exists in the current directory
        if not os.path.isfile(filename_n):
            raise FileNotFoundError(f"File '{filename_n}' does not exist in the current directory")

        # Read the CSV file
        with open(filename_n, 'r', newline='') as csvfile:
            reader = list(csv.reader(csvfile, delimiter=';'))

        # Find the first completely empty row
        empty_row_index = None
        for i, row in enumerate(reader):
            if all(cell == '' for cell in row):
                empty_row_index = i
                break

        if empty_row_index is None:
            empty_row_index = len(reader)
            reader.append([])

        # Generate the new row to insert
        date_string = f"{self.dan_text_n}.{self.mesec_text_n}.{self.leto_text_n}"
        new_row = [
            empty_row_index,  # ID (empty_row_index to account for 0-based indexing)
            date_string,
            self.calf_text,
            self.calf_value,
            self.curl_text,
            self.curl_value,
            self.glute_text,
            self.glute_value,
            self.adductor_text,
            self.adductor_value,
            self.abductor_text,
            self.abductor_value,
            self.extension_text,
            self.extension_value,
            self.leg_text,
            self.leg_value,
        ]

        # Ensure the row has enough columns by padding with empty strings if necessary
        if len(reader[empty_row_index]) < len(new_row):
            reader[empty_row_index].extend([''] * (len(new_row) - len(reader[empty_row_index])))

        # Insert the new row
        reader[empty_row_index][:len(new_row)] = new_row

        # Write back to the CSV file with semicolon delimiter
        with open(filename_n, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerows(reader)

        print(f"Entry added to '{filename_n}' at row {empty_row_index + 1}")
        self.initialize_properties_n()
        self.ids.Txt_navodila_n.text = self.navodila_text_n

    def calculate_days_n(self, date_str):
        date_format = "%d.%m.%Y"
        last_training_date = datetime.strptime(date_str, date_format)
        today = datetime.now()
        delta = today - last_training_date
        return delta.days

    def get_text_from_csv_n(self):
        try:
            with open('Noge.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                rows = list(reader)
                if len(rows) <= 1:
                    return "Brez podatkov ..."
                else:
                    last_row = rows[-1]
                    if len(last_row) >= 16:  # Update this to the correct number of columns
                        last_training_date = last_row[1]
                        days_since_last_training = self.calculate_days_n(last_training_date)
                        paragraph_suffix = "dnevi."
                        if days_since_last_training == 1:
                            paragraph_suffix = "dnevom."
                        elif days_since_last_training == 2:
                            paragraph_suffix = "dnevoma."
                        elif days_since_last_training > 2:
                            paragraph_suffix = "dnevi."

                        exercises = [
                            {"name": "Standing calf", "weight_index": 2, "difficulty_index": 3},
                            {"name": "Leg curl", "weight_index": 4, "difficulty_index": 5},
                            {"name": "Standing glute", "weight_index": 6, "difficulty_index": 7},
                            {"name": "Adductor", "weight_index": 8, "difficulty_index": 9},
                            {"name": "Abductor", "weight_index": 10, "difficulty_index": 11},
                            {"name": "Leg extension", "weight_index": 12, "difficulty_index": 13},
                            {"name": "Leg press", "weight_index": 14, "difficulty_index": 15},
                        ]

                        output = f"Zadnji trening je bil {last_row[1]},\n\nPred {days_since_last_training} {paragraph_suffix}\n\n"

                        for exercise in exercises:
                            weight_index = exercise["weight_index"]
                            difficulty_index = exercise["difficulty_index"]
                            weight = last_row[weight_index]
                            difficulty = last_row[difficulty_index]
                            weight_description = ""
                            if difficulty == "0.0":
                                weight_description = "Fail"
                            elif difficulty == "1.0":
                                weight_description = "Zelo težko"
                            elif difficulty == "2.0":
                                weight_description = "Naporno"
                            elif difficulty == "3.0":
                                weight_description = "Lahko"
                            elif difficulty == "4.0":
                                weight_description = "Zelo lahko"

                            output += f"{exercise['name']} = {weight} kg, {weight_description}\n"

                        return output
                    else:
                        return "Brez podatkov ..."
        except Exception as e:
            print("Error occurred:", e)
            return "Brez podatkov ..."

    def button_lift_noge(self):
        # Get the current date
        current_date = datetime.now()

        # Extract day, month, and year
        dan_text_n = str(current_date.day)
        mesec_text_n = str(current_date.month)
        leto_text_n = str(current_date.year)

        # Update the TextInput widgets with the extracted values
        self.ids.Txt_dan_n.text = dan_text_n
        self.ids.Txt_mesec_n.text = mesec_text_n
        self.ids.Txt_leto_n.text = leto_text_n

        # Print the values
        print("dan_text =", dan_text_n)
        print("mesec_text =", mesec_text_n)
        print("leto_text =", leto_text_n)

        # Call navodila function to update Txt_navodila
        self.navodila_n()

    def navodila_n(self):
        navodila_text_n = self.get_text_from_csv_n()
        self.ids.Txt_navodila_n.text = navodila_text_n

class Lift(App):
    def build(self):
        # Create a screen manager and add both screens
        sm = ScreenManager()
        sm.add_widget(Home_Widget(name='home_widget'))
        sm.add_widget(Roke_Widget(name='roke_widget'))
        sm.add_widget(Noge_Widget(name='noge_widget'))
        return sm

if __name__ == "__main__":
    app = Lift()
    app.run()
