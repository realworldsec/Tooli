
#   S4Script

This is a tool build in python script . It contains .
Web recon and Cryptography tools "Commands".

## Authors

- [@1pwn](https://www.github.com/1pwn)
- [@livepwn](https://www.github.com/livepwn)

## Deployment

To deploy these Tools run

```bash
  git clone https://github.com/realworldsec/Tooli.git
  
  cd Tooli
  python Web.py
  python Crypto.py
```


## Features

- Time Saviour
- Donot want to remember any tool command now
- Just Copy the command and change url and run
- Specially build for (Ctf player and Bug Hunter)



## Usage
"Same for both Web.py and Crypto.py"
```python
livepwn(Web): tools 
                 OR
livepwn(Crypto): tools

--> Tools present in my tool will preview

livepwn(Web): website

--> Recon website will be preview

- For Tools that previewed using tools command
EXP: 
    livepwn(Web): gobuster
    gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt -t 50 -o gobuster_results.txt
```


## Credits
Tooli is created by [@livepwn](https://www.github.com/livepwn) and [@1pwn](https://www.github.com/1pwn)
![k](https://github.com/user-attachments/assets/cfe4dc4b-4948-4ba0-a492-731ca163e45b)
