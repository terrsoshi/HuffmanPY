# -*- coding: utf-8 -*-
"""
@author: Wong Tian Jie
"""
   
import heapq        

#calculate frequency of each character exists in inputText and returns a list of tuples with each pair containing the frequency and label of each character
def calculateCharFreq(inputText):
    charFreq = {}
    for char in inputText:
            if char in charFreq:
                charFreq[char] += 1
            else:
                charFreq[char] = 1
    freqList = [ (frequency, character) for character, frequency in charFreq.items()]
    return freqList
    

def createTree(freq):
    # letterFrequencies: list of (frequency, letter) tuples
    heap = []
    for f in freq:
        heapq.heappush(heap, [f])
        
    while(len(heap)>1):
        L_Child = heapq.heappop(heap)
        R_Child = heapq.heappop(heap)
        L_Freq, L_Label = L_Child[0]
        R_Freq, R_Label = R_Child[0]
        freq = L_Freq + R_Freq
        label = ''.join(sorted(L_Label + R_Label))
        heapNode = [(freq, label), L_Child, R_Child]
        heapq.heappush(heap, heapNode)
    return heap.pop()

def setBinaryTree(binaryTree, binaryMap, binaryPrefix):
    if(len(binaryTree) == 1):
        freq, label = binaryTree[0]
        binaryMap[label] = binaryPrefix
    else:
        value, L_Child, R_Child = binaryTree
        # set binary value to the left child of its  parent as value of '0' 
        setBinaryTree(L_Child, binaryMap, binaryPrefix + '0')
        # set binary value to the right child of its parent as value of '1'
        setBinaryTree(R_Child, binaryMap, binaryPrefix + '1')
        return binaryMap

def createBinaryMap(binaryTree):
    binaryMap = dict()
    setBinaryTree(binaryTree, binaryMap, '')
    return binaryMap

def encode(msg, freq):
    # first, take the frequency of the letter to turn it into binary tree 
    # then, create a binary map from the binary tree for these frequency
    binaryMap = createBinaryMap(createTree(freq)) 
    
    return ''.join([binaryMap[x] for x in msg])

def decode(msg, freq):
    # create tree of frequency
    wholeTree = createTree(freq)
    binaryTree = wholeTree
    
    letter = []
    for x in msg:
        if(x == '0'):
            binaryTree = binaryTree[1]
        else:
            binaryTree = binaryTree[2]
        
        if(len(binaryTree) == 1):
            freq, label = binaryTree[0]
            letter.append(label)
            
            binaryTree = wholeTree
    return ''.join(letter)

#Edit input_text variable to perform Huffman Coding algorithm on a different String
input_text = 'corgi is love'

freq = calculateCharFreq(input_text)
node = createTree(freq)

print('Huffman Coding Tree:\n' + str(node))
print()
print('Huffman Code for each character:\n' + str(createBinaryMap(node)))
print()
encoded_bits = encode(input_text, freq)
print('Encoding from the letters, ' + "'" + input_text + "':\nOutput: " + encoded_bits)
print()
result = decode(encoded_bits, freq)
print('Decoding from the code, ' + "'" + encoded_bits + "':\nOutput: " + result)
print()
print("Comparing result text decoded from new code words to input text to check if they are the same:")
print("Input text: " + input_text)
print("Result text: " + result)
if result == input_text:
    print("\nResult text decoded from new code words are the same as input text, the encoding is successful.\n")
print('Total number of bits required to store the String in ASCII encoding: ' + str(len(input_text) * 8) + ' bits\n')
print('Total number of bits required to store the String in Unicode encoding: ' + str(len(input_text) * 16) + ' bits\n')
print('Total number of bits required to store the String in Huffman encoding: ' + str(len(encoded_bits)) + ' bits\n')
print("Number of bits saved in Huffman encoding compared to ASCII encoding: " + str((len(input_text) * 8) - len(encoded_bits)) + ' bits')
