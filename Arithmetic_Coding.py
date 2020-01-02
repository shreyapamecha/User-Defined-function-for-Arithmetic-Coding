#The code written for the question 6th on Arithmetic Coding takes a lot of time because of the user-defined functions: 'optimized_value' as it deciphers binary equivalents for enormous float numbers between the range lower_limit and upper_limit to determine the optimized value and 'Instance_matrix' 
#------------------------------------------------------------------------------------------------------------------------------------------
#Inputs given to the main function: 'ArithmeticCoding_17110150'
#A: is the matrix of an input image consisting of 2 columns; 1st representing the source symbols and the 2nd representing the probabilities
#N: a number representing number of symbols which are to be coded together
#flag: can be either decimal or binary
#B: a list of symbols of the message signal (single-channel image) which is to be encoded
#------------------------------------------------------------------------------------------------------------------------------------------

#importing libraries
import cv2
import numpy as np

#User-defined function for deciphering normalized histogram of a single channel(grayscale image) input image
#the output of the function is A which a matrix consisting of two columns where the 1st is representing the intensity values of the pixels in a grayscale image and
#the 2nd: probability of occurrence of that intensity value in the input image
def Instance_matrix(f):
    #print(f)
    A=np.zeros((256,2))
    #for grayscale image
    for i in range(0,256):
        A[i][0]=i;

    #raster-order scan
    for i in range(len(f)):
        for j in range(len(f[0])):
            for k in range(len(A)):
               if f[i][j]==k:
                   A[k][1]+=1;

    for i in range(0,256): 
        A[i][1]=A[i][1]/(len(f)*len(f[0]));
    #for normalizing, dividing the number of a particular intensity value by the total number of pixels (product of rows and columns of the input matrix)
    
    return A


#converting the message image matrix to a list (raster order scan). Now, the message in this list is encoded
def matrix_to_array(message):
    m=[];
    for i in range(len(message)):
        for j in range(len(message[0])):
            m.append(message[i][j])
    return m


#Arithmetic Coding as taught in class
def coding(A,B):
    lower_limit=0; #Normalization
    upper_limit=1;
    no_symbols=len(A); #representing number of symbols

    for i in B:
        C=np.zeros((no_symbols,2));
        for j in range(no_symbols):
            C[j][0]=int(A[j][0]);
            if j==0:
                C[j][1]=lower_limit+((upper_limit-lower_limit)*A[j][1]);
            else:
                C[j][1]=C[j-1][1]+((upper_limit-lower_limit)*A[j][1]);

        for k in range(no_symbols):
            if (C[0][0]==int(i)):
                upper_limit=C[0][1];
            elif (C[k][0]==int(i)):
                lower_limit=C[k-1][1];
                upper_limit=C[k][1];

        #print(lower_limit, ' ', upper_limit, ' ',i)
        
    return (lower_limit,upper_limit)


#converting decimal fraction to binary fraction
def decimal_to_binary(decimal,N):
    whole,dec=str(decimal).split('.')
    #print(whole,dec)
    binary=str(whole) + '.'
    #print(float(dec))
 
    while (float(dec)!=0):
        if len(str(binary))==(3*N): #we are stopping the calculation of binary equivalent(just a value which i have set)
            break

        #print(binary)

        dec = '0.' + str(dec)
        dec=str(float(dec)*2)
        #print(dec)
        whole,dec=str(dec).split('.')
        binary=str(binary) + str(whole)

    binary=float(binary)
    
    return binary

#finding an optimized decimal and binary equivalent
#method used is going through all the float numbers within the range[lower_limit, upper_limit) and the increment value set is 'step_up' here.
#This step_up is chosen on the basis of maximum characters out of 'lower_limit' and 'upper_limit'. For eg: lower_limit=0.07654 and upper_limit=0.078, here maximum=7 and step_up chosen would be 0.00001.
#Now, a loop will run from [0.07654,0.078) with the increment value of 0.00001. For every value of 'i', binary equivalent is calculated and then stored in a matrix.
#Then, the optimized value is found using the following procedure:
#(i)checking if we are obtaining less characters for both decimal and binary at the same time or not
#(ii)checking only if one of them is getting minimized
#comparing the characters required for both the options, and hence, finding an optimized value. 
def optimized_value(lower_limit,upper_limit,flag,N):
    maximum=max(len(str(float(lower_limit))),len(str(float(upper_limit)))); 
    #print(maximum)
    step_up='0.'
    if maximum>10: 
        maximum=10;
        
    for i in range(maximum-3):
        step_up+='0';
    step_up=float(str(step_up)+'1');
    #print(step_up)
    number_of_steps=round(((upper_limit-lower_limit)/step_up)+1);
    #print(number_of_steps)
    A=np.zeros((int(number_of_steps),2))
    if A[int(number_of_steps)-1][0]==upper_limit:
        A.delete(A,int(number_of_steps)-1,0)

    j=0
    for i in np.arange(lower_limit,upper_limit,step_up):
        A[j][0]=i;
        A[j][1]=decimal_to_binary(i,N);
        j+=1;   


    #searching for the binary equivalent with least number of bits required to represent the decimal equivalent
    a1=A[0][0];
    b1=A[0][1];

    #(i)
    #checking if we are able to minimize both the equivalents: binary and decimal at the same time or not
    for i in range(1,len(A)):
        if(len(str(A[i][1]))<len(str(b1))) and (len(str(A[i][0]))<len(str(a1))):
            a1=A[i][0];
            b1=A[i][1];

    #print(a1,b1)

    #(ii)
    a2=A[0][0];
    b2=A[0][1];
    for i in range(1,len(A)):
        if (len(str(A[i][1]))<len(str(b2))) or (len(str(A[i][0]))<len(str(a2))):
            b2=A[i][1];
            a2=A[i][0];

    #print(a2,b2)
    #checking which one is more efficient (i) or (ii)
    #(by equal to sign, i'm giving more weightage to when we are able to minimize both the fractions)
    if ((len(str(a1))+len(str(b1)))<=(len(str(a2))+len(str(b2)))):
        a=a1;
        b=b1;
    else:
        a=a2;
        b=b2;

    #print(a,b)
    if flag=='decimal':
        return a
    elif flag=='binary':
        return b
    

def ArithmeticCoding_17110150(A,N,flag,m):
    counter=0; #aids in keeping a track on how many groups with 'N' elements each have already been encoded 
    output=[]; #output, giving a matrix of either all the decimal equivalents or all the binary equivalents, according to the 'flag' value
    for i in range(int(len(m)/N)):
        B=[];
        for j in range(N):
            B.append(m[counter]); #appending 'N' values to this list from the message input
            counter+=1; 
        [lower_limit,upper_limit]=coding(A,B); #calling this user-defined function which encodes the elements present B and renders a range(arithmetic encoding)

        dec_bin=optimized_value(lower_limit,upper_limit,flag,N); #can be decimal or binary depending upon the flag 
        output.append(dec_bin); #appending the optimized value and then, proceeding further for the next group of 'N' elements

    print('done1')
    #this same operation is done on the left intensity values 
    if (len(m)%N!=0):
        B=[];
        for i in range(counter,len(m),1):
            B.append(m[i]);
        [lower_limit,upper_limit]=coding(A,B); 

        dec_bin=optimized_value(lower_limit,upper_limit,flag,N); #can be decimal or binary depending upon the flag
        output.append(dec_bin);

    print('done2')
    return output
                

if __name__ == '__main__':
    #input to the 'encode' function where 1st column is representing the symbol and 2nd column is the probability of the occurrence of the symbol
    #---------Finding normalized histogram of a single channel input image--------------
    path_to_image = 'C:\\Users\\ympam\\Downloads\\image2.jpg';
    f=cv2.imread(path_to_image,cv2.IMREAD_GRAYSCALE); #array of an input image
    A=Instance_matrix(f);
    #------------------------------Message signal---------------------------------------
    path_message = 'C:\\Users\\ympam\\Downloads\\image3.jpg';
    message=cv2.imread(path_message,cv2.IMREAD_GRAYSCALE); #array of the message signal
    #print(message)
    m=matrix_to_array(message);
    #-----------------------------------------------------------------------------------
    flag='binary';
    N=7; 
    #-----------------------------------------------------------------------------------
    output=ArithmeticCoding_17110150(A,N,flag,m)
    #print(B)
    
    print(output)
    
#if the sizes of the input image and the message image are high, this aforementioned code is taking a lot of time.
