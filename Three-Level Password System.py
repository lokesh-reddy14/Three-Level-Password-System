import hashlib
import time
import random

def textual_authentication():
    correct_password_hash = hashlib.sha256("Lokesh@123".encode()).hexdigest()
    password = input("Enter your textual password: ")
    if hashlib.sha256(password.encode()).hexdigest() == correct_password_hash:
        return True
    return False

def graphical_authentication():
    images = ["[Sun]", "[Moon]", "[Star]", "[Tree]", "[Cloud]"]
    correct_sequence = [2, 4, 1]
    random.shuffle(images)
    
    print("Select the images in the correct sequence:")
    for i, img in enumerate(images):
        print(f"{i+1}. {img}")
    
    user_sequence = list(map(int, input("Enter the sequence of numbers: ").split()))
    return user_sequence == correct_sequence

def behavioral_authentication():
    print("Type the following phrase: 'Secure and Fast'")
    start_time = time.time()
    input_text = input(">>> ")
    typing_speed = time.time() - start_time
    
    if input_text == "Secure and Fast" and typing_speed < 5:
        return True
    return False

def main():
    print("Welcome to the Three-Level Password System\n")
    
    if textual_authentication():
        print("Textual authentication successful.\n")
        
        if graphical_authentication():
            print("Graphical authentication successful.\n")
            
            if behavioral_authentication():
                print("Behavioral authentication successful.\n")
                print("Access Granted!")
            else:
                print("Behavioral authentication failed.")
        else:
            print("Graphical authentication failed.")
    else:
        print("Textual authentication failed.")

if __name__ == "__main__":
    main()
