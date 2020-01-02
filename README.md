# User-Defined-function-for-Arithmetic-Coding
The input of the function for Arithmetic Coding should be:

1) either a matrix with two columns (the first column is symbol number, the second column is a probability, and each row indicating a symbol) or a single channel image

 2) a number ‘N’ which shows the number of symbols which are to be coded together (if the total length of the message to be encrypted is not a multiple of N, then last message sequence will contain fewer than N symbols)
 
3) a flag indicating whether the output should be binary fractions or decimal fractions (in either case the function should give the binary/decimal number with least number of bits/digits needed to represent a sequence of symbols)

4) (optional argument) a 1-D array listing symbols/numbers in the message to be coded (if this argument is missing, then the function should return the result of applying Arithmetic Coding on the input single-channel image.) 

The output of the function should be there result of applying Arithmetic Coding on the specified data, specified as a column vector of appropriate size and the probability table used for encoding.

Description

The algorithm works as follows: first of all, the RGB input image is converted into a grayscale image; then, a normalized histogram of this single-channel image is determined. The message input signal matrix which needs to be encoded is converted to a list through a raster order scan. N indicates the number of symbols or elements of the list (message signal), which are to be coded together. A loop is run to accommodate N symbols from the message signal list to a diﬀerent list, which is then passed to a new function to encode it using Arithmetic Coding. Now, we have obtained a range [lower limit, upper limit), its optimized binary and decimal equivalent is calculated, regardless of the value of ﬂag. In the optimization process, binary fractions of many ﬂoat numbers within the range [lower limit, upper limit) are checked, and an optimized value is decided by considering two cases. In the first case, the number of characters present in both binary and decimal fractions should be less. In the second case, the number of characters present in any one of them should be less. The characters of the outputs (characters of binary fraction + characters of decimal fractions) from both the cases are determined, and the one for which a lesser number of characters are required is considered to be the optimized one. The optimized value is appended to a list, depending upon the value of the flag. This process continues for all such groups of N elements. The number of symbols may not be a multiple of N so that the last message sequence may contain a lesser number of symbols. The output obtained includes a list of all binary fractions or all the decimal fractions, depending upon the value of the flag.

Note: The running time of this code exponentially increases with the size of the input image taken. It is so because of the two user-deﬁned functions:

(i) 'optimized_value': it deciphers binary equivalents for enormous float numbers between the range lower_limit and upper_limit to determine the optimized values of decimal and binary equivalents.

(ii) 'Instance_matrix': it deciphers the normalized histogram of a single channel (grayscale) input image. More the size of the input image more will be the computation time.

Parameters Chosen

• f: Input image represented as a 2D matrix 

• A: the array of an input image consisting of 2 columns; 1st representing the source symbols and the 2nd representing the probabilities 

• N: a number representing a number of symbols which are to be coded together 

• flag: can be either decimal or binary 

• B: list of symbols of the message signal (single-channel image) which is to be encoded 

• lower_limit: lower limit of the encoded group of N symbols 

• upper_limit: upper limit of the encoded group of N symbols

User-Defined Functions

• Instance_matrix: It deciphers the normalized histogram of a single channel(grayscale image) input image. The output of the function is a matrix consisting of two columns where the 1st represents the intensity values of the pixels in a grayscale image, and the 2nd represents the probability of occurrence of that intensity value in the input image. 

• matrix_to_array: It converts the input message 2D matrix to a list through a raster order scan, and the output of the function is needed to be encoded through Arithmetic coding. 

• coding: It is encoding the message symbol in groups of N. The output of this userdeﬁned function is the range [lower limit, upper limit). 

• decimal_to_binary: It simply converts decimal fractions into binary fractions. 

• optimized_value: The input of this function is lower_limit, upper_limit, ﬂag, and N. It goes through enormous ﬂoat numbers within the range [lower_limit, upper_limit). It checks for their binary equivalents, and then, using two methods as discussed above, the optimized values are determined. For instance, lower_limit=0.07654, upper_limit=0.078. Here, the maximum characters required is 7. Therefore, step_up is chosen as 0.00001. A loop is run from 0.07654 to 0.078, with an increment of 0.00001. For every value of i, the binary equivalent is calculated and then stored in a matrix. The optimized values are found using the following procedure:

(i) checking whether we are obtaining fewer characters for both decimal and binary at the same time or not. 

(ii)checking if one of them is getting minimized and now, comparing the total characters required for both the options, and hence, finding the optimized one. 

• ArithmeticCoding_17110150: The primary function is calling all the user-defined functions mentioned above. The output obtained is a list of either the binary equivalents or the decimal equivalents, depending upon the value of the flag.







