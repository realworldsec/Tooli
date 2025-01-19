#Tool For My Friends

#Tools for Basic Information of wesite
Input=input("livepwn(Web): ")
a="whois" # Basic Info of website
b="harvester" # Search Info about website using different Browsers
c="website" # Contains all websites use for web reconnaissance

#Tools for subdomains
d="sudomain" # Provide basic subdomains, 
e="sublister" # Same work
f="osrf"  # It,s important for reconnaissance because it,s a large framework
g="subfinder" #Same work provide subdomains
h="website subdomains" # Provide websites to findsubdomains 

#Tools for Website Directories

i="dirb" #Basic search for directory
j="gobuster" #Same work but more precise
k="dirsearch" #Search for directory as others
l="fuff" #Same work but provide more info

#Tools for DNS Info

m="dig" # Provide DNS info
n="fierce" #Same work provide DNS info but in detail
o="amass" #use for DNS enumeration
p="massdns" # Important tool because it checks all the DNS which was listed by amass that which are live and which are not 

#Basic Tools for Info
q="nmap"
#Done
r="tools"


if Input == a:
    print("whois example.com")
elif Input == b:
    print("theharvester -d example.com -b google")
elif Input == c:
    print("""
1:"https://whois.domaintools.com"(Find info of owner)
2:"https://sitereport.netcraft.com"(Tecnology in (Frontened and backened))
3:"https://www.robtex.com"(Detail information about the website)""")
elif Input == d:
    print("subfinder -d example.com")
elif Input == e:
    print("python3 sublist3r.py -d example.com")
elif Input == f:
    print("Please specify the command for the 'osrf' tool.")
elif Input == g:
    print("subfinder -d example.com")
elif Input == h:
    print("Please specify the command for the 'website subdomains' tool.")
elif Input == i:
    print("dirb http://example.com /usr/share/wordlists/dirb/common.txt")
elif Input == j:
    print("gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt -t 50 -o gobuster_results.txt")
elif Input == k:
    print("python3 dirsearch.py -u http://example.com -w /usr/share/wordlists/dirb/common.txt")
elif Input == l:
    print("fuff -u http://example.com -w /usr/share/wordlists/dirb/common.txt -mc all")
elif Input == m:
    print("dig example.com ANY")
elif Input == n:
    print("fierce --domain example.com")
elif Input == o:
    print("amass enum -d example.com")
elif Input == p:
    print("""massdns -r resolvers.txt -t A -o S -w massdns_results.txt example.com.txt

             This Command is for arranging the domains in your output.txt
             [sed 's/A. *//' livehosts.txt | sed 's/CN. *//' | sed 's/..$//'> live_subdomains.txt](use backslash after s/)""")
elif Input == q:
    print("nmap -sS -sV -A example.com")

elif Input==r:
	print( """
1. "whois"  
   Basic info of a website
   Command: whois example.com

2. "harvester"  
   Search info about a website using different sources
   Command: theharvester -d example.com -b google

3. "website"  
   Contains all websites used for web reconnaissance
   Command: Please specify the command for the 'website' tool.

4. "subdomain"  
   Provides basic subdomains
   Command: subfinder -d example.com

5. "sublister"  
   Performs similar tasks for subdomain enumeration
   Command: python3 sublist3r.py -d example.com

6. "osrf"  
   Important for reconnaissance; specific command needed.
   Command: Please specify the command for the 'osrf' tool.

7. "subfinder"  
   Provides subdomain enumeration
   Command: subfinder -d example.com

8. "website subdomains"  
   Tools for finding subdomains across websites
   Command: Please specify the command for the 'website subdomains' tool.

9. "dirb"  
   Basic search for directories
   Command: dirb http://example.com /usr/share/wordlists/dirb/common.txt

10. "gobuster"  
    Same function but more precise in results
    Command: gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt -t 50 -o gobuster_results.txt

11. "dirsearch"  
    Search for directories like others
    Command: python3 dirsearch.py -u http://example.com -w /usr/share/wordlists/dirb/common.txt

12. "fuff"  
    Similar to others but provides more detailed info
    Command: fuff -u http://example.com -w /usr/share/wordlists/dirb/common.txt -mc all

13. "dig"  
    Provides DNS info
    Command: dig example.com ANY

14. "fierce"  
    Provides detailed DNS info
    Command: fierce --domain example.com

15. "amass"  
    Used for DNS enumeration
    Command: amass enum -d example.com

16. "massdns"  
    Checks live DNS records listed by Amass
    Command: massdns -r resolvers.txt -t A -o S -w massdns_results.txt example.com.txt

17. "nmap"  
    Network scanning and discovery tool
    Command: nmap -sS -sV -A example.com
""")

else:
    print("Happy CTF")





