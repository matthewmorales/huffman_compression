from heapq import heappush, heappop, heapify
from collections import defaultdict
import sys
import array
import binascii

def encode(charquantity):
    heap = [[weight, [character, ""]] for character, weight in charquantity.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
 
text_file = open("ascii.txt","r")
text = text_file.read()
text_file.close()

charquantity = defaultdict(int)
for ch in text:
    charquantity[ch] += 1

huff = encode(charquantity)
print "Symbol\tWeight\tHuffman Code"
for entry in huff:
    print "%s\t%s\t%s" % (entry[0], charquantity[entry[0]], entry[1])
print "****************************\n"


def compress():
    print('Generating ascii_compressed.txt\n') 
    comp_text = ""
    append_count = 0
    byte_split =""
    temp_byte =""
    compressed_data =""
    data = array.array('B')
    name = 'ascii_compressed.txt'  # Name of text file coerced with +.txt

    try:
        file = open(name,'wb')   # Trying to create a new file or open one
        for p in huff:
            file.write("%s-%s;" % (p[0], p[1]))
        file.write("HUFFMANCOMPRESSIONHEADERABOVE")
        for ch in text:
            for i in range(0, 26):
                if ch == huff[i][0]:
                    byte_split = byte_split + huff[i][1]
        for ch in byte_split:
            temp_byte = temp_byte + ch
            append_count += 1
            if append_count % 8 == 0:
                append_count = 0
                compressed_data = compressed_data + chr(int(temp_byte, 2))
                temp_byte =""

        file.write(compressed_data)
        file.close()
        
    except:
        print('File Creation Failed')
        sys.exit(0) # quit Python


compress()


def decompress():
    print "Generating ascii_decompressed.txt\n"
    decomp_keys = {}
    inter_key_split = []
    compressed_file = open("ascii_compressed.txt")
    compression = compressed_file.read()
    compressed_file.close()
    comp_to_binary=""
    test_key =""
    decompressed_text=""

    name = "ascii_decompressed.txt"

    header = compression.split('HUFFMANCOMPRESSIONHEADERABOVE')[0]

    for x in range(0, 26):
        inter_key_split.append(header.split(';')[x])
    #print inter_key_split

    for entry in inter_key_split:
        decomp_keys[entry.split('-')[1]] = entry.split('-')[0]

    #print decomp_keys

    compression = compression.split('HUFFMANCOMPRESSIONHEADERABOVE')[1]

    #print header

    #test = binascii.a2b_uu(compression[1])
    for ch in compression:
        comp_to_binary = comp_to_binary + '{0:08b}'.format(ord(ch))

    for ch in comp_to_binary:
        test_key = test_key + ch
        if test_key in decomp_keys:
            decompressed_text = decompressed_text + decomp_keys[test_key]
            test_key = ""

    try:
        file = open(name,'wb')   # Trying to create a new file or open one
        file.write(decompressed_text)
        file.close()
        
    except:
        print('File Creation Failed')
        sys.exit(0) # quit Python

            





decompress()
