import smtplib
from email.message import EmailMessage

# Emergency cases
emergencies = {
    "1": "Medical Emergency",
    "2": "Fire Emergency",
    "3": "Natural Disaster",
    "4": "Burglary",
    "5": "Road Accident",
    "6": "Lost Person",
    "7": "Domestic Violence",
    "8": "Power Outage",
    "9": "Gas Leak",
    "10": "Animal Attack"
}

def send_email(name, lat, lon, emergency_type):
    msg = EmailMessage()
    msg['Subject'] = f'Emergency Alert: {emergency_type}'
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = 'prevanth.data@gmail.com'
    
    msg.set_content(f"""
    Name: {name}
    Emergency Type: {emergency_type}
    Location Coordinates: Latitude {lat}, Longitude {lon}
    """)

    # Login and send email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('your_email@gmail.com', 'your_app_password')
            smtp.send_message(msg)
            print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

def chatbot():
    print("🚨 Welcome to Emergency Bot 🚨\nSelect your emergency:")
    for key, val in emergencies.items():
        print(f"{key}. {val}")

    choice = input("\nEnter your emergency number (1-10): ")

    if choice in emergencies:
        if choice == "1":
            name = input("Please enter your name: ")
            try:
                lat = float(input("Enter your latitude: "))
                lon = float(input("Enter your longitude: "))
            except ValueError:
                print("Invalid coordinates. Please enter numeric values.")
                return
            send_email(name, lat, lon, emergencies[choice])
        else:
            print(f"You selected: {emergencies[choice]}")
            print("👉 This case does not send an email (only Option 1 does in this demo).")
    else:
        print("❌ Invalid option selected.")

if __name__ == "__main__":
    chatbot()

