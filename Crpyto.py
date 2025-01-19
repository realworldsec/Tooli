#Tools for CTF

Input=input("livepwn(Crypto): ")

#Cryptography

a="featherduster"  #An automated, modular cryptanalysis tool
b="hashextender"  #A utility tool for performing hash length extension attacks
c="pkcrack"       #A tool for Breaking PkZip-encryption
d="rsactftool"   #A tool for recovering RSA private key with various attack
e="rsatool"      #Generate private key with knowledge of p and q
f="xortool"      #A tool to analyze multi-byte xor cipher
g="scrypt"        #A password-based key derivation function designed to be computationally intensive, making it resistant to brute-force attacks
h="cutycapt"       #Capture screenshots of websites and convert them into various formats, useful for web security assessments
i="hash-identifier" #A tool that identifies the type of hash based on its format and characteristics, helping users determine which hashing algorithm was used
j="hashpump"        #A tool for exploiting hash length extension vulnerabilities, allowing users to append data to a hashed message without knowing the secret
k="steghide"        #A steganography tool that embeds data within various media formats, such as images and audio files, to hide messages.
l="binwalk"         #firmware analysis tool that scans binary files for embedded files and executable code, useful for reverse engineering and analysis
m="echo"            # Use this to see how to decrypt through terminal
x="website"
n="tools"


if Input==a:
	print("featherduster -f <ciphertext> -m <module>")

elif Input==b:
	print("hashpump -s <original_hash> -a <data_to_append> -l <length_of_original_message>")

elif Input==c:
	print("pkcrack -f <encrypted_zip_file>")

elif Input==d:
	print("rsactftool -k <public_key> -c <ciphertext>")

elif Input==e:
	print("rsatool -p <p> -q <q>")

elif Input==f:
	print("xortool <encrypted_file>")

elif Input==g:
	print("")

elif Input==h:
	print("cutycapt --url=<website_url> --out=<screenshot.png>")

elif Input==i:
	print("hash-identifier <hash_value>")

elif Input==j:
	print("hashpump -s <original_hash> -a <data_to_append> -l <length_of_original_message>")

elif Input==k:
	print("steghide extract -sf <image_file> -xf <output_file>")

elif Input==l:
	print("binwalk -e file.bin")						

elif Input==m:
	print("echo 'encoded form' | base64 -d ")
elif Input==x:
	print("""
 1- https://gchq.github.io/CyberChef/
 2- https://www.dcode.fr/
 3- https://www.base64decode.org/ """)

elif Input==n:
	print ( """
1. "featherduster"  # An automated, modular cryptanalysis tool
2. "hashextender"   # A utility tool for performing hash length extension attacks
3. "pkcrack"        # A tool for breaking PkZip-encryption
4. "rsactftool"     # A tool for recovering RSA private key with various attacks
5. "rsatool"        # Generate private key with knowledge of p and q
6. "xortool"        # A tool to analyze multi-byte XOR cipher
7. "scrypt"         # A password-based key derivation function designed to be computationally intensive, making it resistant to brute-force attacks
8. "cutycapt"       # Capture screenshots of websites and convert them into various formats, useful for web security assessments
9. "hash-identifier" # A tool that identifies the type of hash based on its format and characteristics, helping users determine which hashing algorithm was used
10. "hashpump"       # A tool for exploiting hash length extension vulnerabilities, allowing users to append data to a hashed message without knowing the secret
11. "steghide"       # A steganography tool that embeds data within various media formats, such as images and audio files, to hide messages
12. "binwalk"        # A firmware analysis tool that scans binary files for embedded files and executable code, useful for reverse engineering and analysis
13. "echo"           # A command-line utility for outputting text or variables in shell scripts
""" )

else :
	print("Happy CTF")

	
