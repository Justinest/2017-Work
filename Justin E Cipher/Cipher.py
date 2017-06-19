def encrpyt():
    key = input("What key do you wish to input:")
    key_input = int(key)
    cipher = ' '
    print ("Your Choosen key is:")
    print (key_input)
    ciphertext = input("Enter the Message you Wish to Cipher:")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c in ciphertext:
        if c in alphabet:
            cipher += alphabet[ (alphabet.index(c)+key_input)%(len(alphabet))]
            
            print ("Your encrypted message is:" + cipher)

def decrypt():
    keydec = input("What key do you wish to decrypt with:")
    keydec_input = int(keydec)
    print ("Your Choosen key is:")
    print (keydec_input) 
    cipher1 = ' '
    deciphertext = input("Enter the Message you wish to Decipher:")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c in deciphertext:
        if c in alphabet:
            cipher1 += alphabet[ (alphabet.index(c)-keydec_input)%(len(alphabet))]
             
            print ("Your decrypted message is:" + cipher1)
    



def quit():
    done = False
    while not done:
        if cipher_msg == "q":
            q = True
            quit = input("Are you sure you want to quit:")
            if quit == "q":
                done = True
                
                
  

print("Welcome to my Ceaser Cipher")
done = False
while not done:
    cipher_msg = input("Do you want to encrypt, decrypt, or quit \n e to encrypt: \n d to decrypt: \n q to quit: \n:")
    if cipher_msg.lower() == "e":
        encrpyt()
    elif cipher_msg.lower() == "d":
        decrypt()
    elif cipher_msg.lower() == "q":
        quit()
        done = True 
    
    
   
   
        
       

