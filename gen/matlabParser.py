# Generated from C:/Users/Kira/PycharmProjects/MathLab_to_Python/grammar/matlab.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,544,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,1,0,3,0,116,8,0,1,0,1,0,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,134,
        8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,3,6,147,8,6,1,6,
        1,6,1,6,1,6,5,6,153,8,6,10,6,12,6,156,9,6,1,7,1,7,3,7,160,8,7,1,
        8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,173,8,10,10,
        10,12,10,176,9,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,
        13,1,13,3,13,189,8,13,1,14,1,14,1,14,3,14,194,8,14,1,15,1,15,1,16,
        1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,
        1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,
        1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,5,30,257,8,30,10,30,12,30,260,9,30,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,5,31,273,
        8,31,10,31,12,31,276,9,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,5,32,295,8,32,10,32,
        12,32,298,9,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,5,33,
        309,8,33,10,33,12,33,312,9,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,
        5,34,321,8,34,10,34,12,34,324,9,34,1,35,1,35,1,35,1,35,1,35,1,35,
        1,35,5,35,333,8,35,10,35,12,35,336,9,35,1,36,1,36,1,36,1,36,1,36,
        1,36,1,36,5,36,345,8,36,10,36,12,36,348,9,36,1,37,1,37,1,37,1,37,
        1,38,1,38,1,38,3,38,357,8,38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,
        3,39,366,8,39,1,40,1,40,1,40,1,40,1,40,5,40,373,8,40,10,40,12,40,
        376,9,40,1,41,1,41,1,41,1,41,1,41,5,41,383,8,41,10,41,12,41,386,
        9,41,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,44,
        3,44,400,8,44,1,45,1,45,1,45,1,46,1,46,3,46,407,8,46,1,47,1,47,1,
        47,1,47,1,47,5,47,414,8,47,10,47,12,47,417,9,47,1,48,1,48,1,48,1,
        48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,
        48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,
        48,3,48,449,8,48,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,
        49,5,49,461,8,49,10,49,12,49,464,9,49,1,50,1,50,1,50,1,50,1,50,1,
        50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,
        50,1,50,1,50,1,50,1,50,1,50,3,50,490,8,50,1,51,1,51,1,51,1,51,3,
        51,496,8,51,1,52,1,52,1,52,1,52,1,52,1,52,3,52,504,8,52,1,53,1,53,
        1,53,1,53,1,53,1,53,1,53,5,53,513,8,53,10,53,12,53,516,9,53,1,54,
        1,54,1,54,1,54,1,54,3,54,523,8,54,1,55,1,55,1,55,1,55,1,55,1,55,
        1,55,1,55,1,55,1,55,3,55,535,8,55,1,56,1,56,1,56,1,56,1,56,3,56,
        542,8,56,1,56,0,14,12,20,60,62,64,66,68,70,72,80,82,94,98,106,57,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,
        90,92,94,96,98,100,102,104,106,108,110,112,0,0,545,0,115,1,0,0,0,
        2,133,1,0,0,0,4,135,1,0,0,0,6,137,1,0,0,0,8,139,1,0,0,0,10,141,1,
        0,0,0,12,146,1,0,0,0,14,159,1,0,0,0,16,161,1,0,0,0,18,163,1,0,0,
        0,20,165,1,0,0,0,22,177,1,0,0,0,24,179,1,0,0,0,26,188,1,0,0,0,28,
        193,1,0,0,0,30,195,1,0,0,0,32,197,1,0,0,0,34,199,1,0,0,0,36,201,
        1,0,0,0,38,203,1,0,0,0,40,205,1,0,0,0,42,207,1,0,0,0,44,209,1,0,
        0,0,46,211,1,0,0,0,48,213,1,0,0,0,50,215,1,0,0,0,52,217,1,0,0,0,
        54,219,1,0,0,0,56,221,1,0,0,0,58,223,1,0,0,0,60,225,1,0,0,0,62,261,
        1,0,0,0,64,277,1,0,0,0,66,299,1,0,0,0,68,313,1,0,0,0,70,325,1,0,
        0,0,72,337,1,0,0,0,74,349,1,0,0,0,76,356,1,0,0,0,78,365,1,0,0,0,
        80,367,1,0,0,0,82,377,1,0,0,0,84,387,1,0,0,0,86,391,1,0,0,0,88,399,
        1,0,0,0,90,401,1,0,0,0,92,406,1,0,0,0,94,408,1,0,0,0,96,448,1,0,
        0,0,98,450,1,0,0,0,100,489,1,0,0,0,102,495,1,0,0,0,104,503,1,0,0,
        0,106,505,1,0,0,0,108,522,1,0,0,0,110,534,1,0,0,0,112,541,1,0,0,
        0,114,116,3,80,40,0,115,114,1,0,0,0,115,116,1,0,0,0,116,117,1,0,
        0,0,117,118,5,0,0,1,118,1,1,0,0,0,119,134,5,42,0,0,120,134,5,43,
        0,0,121,134,5,41,0,0,122,123,3,4,2,0,123,124,3,72,36,0,124,125,3,
        6,3,0,125,134,1,0,0,0,126,127,3,8,4,0,127,128,3,10,5,0,128,134,1,
        0,0,0,129,130,3,8,4,0,130,131,3,94,47,0,131,132,3,10,5,0,132,134,
        1,0,0,0,133,119,1,0,0,0,133,120,1,0,0,0,133,121,1,0,0,0,133,122,
        1,0,0,0,133,126,1,0,0,0,133,129,1,0,0,0,134,3,1,0,0,0,135,136,5,
        1,0,0,136,5,1,0,0,0,137,138,5,2,0,0,138,7,1,0,0,0,139,140,5,3,0,
        0,140,9,1,0,0,0,141,142,5,4,0,0,142,11,1,0,0,0,143,144,6,6,-1,0,
        144,147,3,2,1,0,145,147,3,24,12,0,146,143,1,0,0,0,146,145,1,0,0,
        0,147,154,1,0,0,0,148,149,10,2,0,0,149,153,5,39,0,0,150,151,10,1,
        0,0,151,153,5,40,0,0,152,148,1,0,0,0,152,150,1,0,0,0,153,156,1,0,
        0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,13,1,0,0,0,156,154,1,0,0,
        0,157,160,3,16,8,0,158,160,3,72,36,0,159,157,1,0,0,0,159,158,1,0,
        0,0,160,15,1,0,0,0,161,162,5,5,0,0,162,17,1,0,0,0,163,164,5,6,0,
        0,164,19,1,0,0,0,165,166,6,10,-1,0,166,167,3,14,7,0,167,174,1,0,
        0,0,168,169,10,1,0,0,169,170,3,22,11,0,170,171,3,14,7,0,171,173,
        1,0,0,0,172,168,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,175,
        1,0,0,0,175,21,1,0,0,0,176,174,1,0,0,0,177,178,5,7,0,0,178,23,1,
        0,0,0,179,180,5,42,0,0,180,181,3,4,2,0,181,182,3,20,10,0,182,183,
        3,6,3,0,183,25,1,0,0,0,184,189,3,12,6,0,185,186,3,28,14,0,186,187,
        3,12,6,0,187,189,1,0,0,0,188,184,1,0,0,0,188,185,1,0,0,0,189,27,
        1,0,0,0,190,194,3,30,15,0,191,194,3,32,16,0,192,194,3,38,19,0,193,
        190,1,0,0,0,193,191,1,0,0,0,193,192,1,0,0,0,194,29,1,0,0,0,195,196,
        5,8,0,0,196,31,1,0,0,0,197,198,5,9,0,0,198,33,1,0,0,0,199,200,5,
        10,0,0,200,35,1,0,0,0,201,202,5,11,0,0,202,37,1,0,0,0,203,204,5,
        12,0,0,204,39,1,0,0,0,205,206,5,13,0,0,206,41,1,0,0,0,207,208,5,
        14,0,0,208,43,1,0,0,0,209,210,5,15,0,0,210,45,1,0,0,0,211,212,5,
        16,0,0,212,47,1,0,0,0,213,214,5,17,0,0,214,49,1,0,0,0,215,216,5,
        18,0,0,216,51,1,0,0,0,217,218,5,36,0,0,218,53,1,0,0,0,219,220,5,
        35,0,0,220,55,1,0,0,0,221,222,5,38,0,0,222,57,1,0,0,0,223,224,5,
        19,0,0,224,59,1,0,0,0,225,226,6,30,-1,0,226,227,3,26,13,0,227,258,
        1,0,0,0,228,229,10,8,0,0,229,230,3,34,17,0,230,231,3,26,13,0,231,
        257,1,0,0,0,232,233,10,7,0,0,233,234,3,36,18,0,234,235,3,26,13,0,
        235,257,1,0,0,0,236,237,10,6,0,0,237,238,3,46,23,0,238,239,3,26,
        13,0,239,257,1,0,0,0,240,241,10,5,0,0,241,242,3,40,20,0,242,243,
        3,26,13,0,243,257,1,0,0,0,244,245,10,4,0,0,245,246,5,20,0,0,246,
        257,3,26,13,0,247,248,10,3,0,0,248,249,5,21,0,0,249,257,3,26,13,
        0,250,251,10,2,0,0,251,252,5,22,0,0,252,257,3,26,13,0,253,254,10,
        1,0,0,254,255,5,23,0,0,255,257,3,26,13,0,256,228,1,0,0,0,256,232,
        1,0,0,0,256,236,1,0,0,0,256,240,1,0,0,0,256,244,1,0,0,0,256,247,
        1,0,0,0,256,250,1,0,0,0,256,253,1,0,0,0,257,260,1,0,0,0,258,256,
        1,0,0,0,258,259,1,0,0,0,259,61,1,0,0,0,260,258,1,0,0,0,261,262,6,
        31,-1,0,262,263,3,60,30,0,263,274,1,0,0,0,264,265,10,2,0,0,265,266,
        3,30,15,0,266,267,3,60,30,0,267,273,1,0,0,0,268,269,10,1,0,0,269,
        270,3,32,16,0,270,271,3,60,30,0,271,273,1,0,0,0,272,264,1,0,0,0,
        272,268,1,0,0,0,273,276,1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,
        275,63,1,0,0,0,276,274,1,0,0,0,277,278,6,32,-1,0,278,279,3,62,31,
        0,279,296,1,0,0,0,280,281,10,4,0,0,281,282,3,50,25,0,282,283,3,62,
        31,0,283,295,1,0,0,0,284,285,10,3,0,0,285,286,3,48,24,0,286,287,
        3,62,31,0,287,295,1,0,0,0,288,289,10,2,0,0,289,290,5,35,0,0,290,
        295,3,62,31,0,291,292,10,1,0,0,292,293,5,36,0,0,293,295,3,62,31,
        0,294,280,1,0,0,0,294,284,1,0,0,0,294,288,1,0,0,0,294,291,1,0,0,
        0,295,298,1,0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,65,1,0,0,0,
        298,296,1,0,0,0,299,300,6,33,-1,0,300,301,3,64,32,0,301,310,1,0,
        0,0,302,303,10,2,0,0,303,304,5,37,0,0,304,309,3,64,32,0,305,306,
        10,1,0,0,306,307,5,38,0,0,307,309,3,64,32,0,308,302,1,0,0,0,308,
        305,1,0,0,0,309,312,1,0,0,0,310,308,1,0,0,0,310,311,1,0,0,0,311,
        67,1,0,0,0,312,310,1,0,0,0,313,314,6,34,-1,0,314,315,3,66,33,0,315,
        322,1,0,0,0,316,317,10,1,0,0,317,318,3,42,21,0,318,319,3,66,33,0,
        319,321,1,0,0,0,320,316,1,0,0,0,321,324,1,0,0,0,322,320,1,0,0,0,
        322,323,1,0,0,0,323,69,1,0,0,0,324,322,1,0,0,0,325,326,6,35,-1,0,
        326,327,3,68,34,0,327,334,1,0,0,0,328,329,10,1,0,0,329,330,3,44,
        22,0,330,331,3,68,34,0,331,333,1,0,0,0,332,328,1,0,0,0,333,336,1,
        0,0,0,334,332,1,0,0,0,334,335,1,0,0,0,335,71,1,0,0,0,336,334,1,0,
        0,0,337,338,6,36,-1,0,338,339,3,70,35,0,339,346,1,0,0,0,340,341,
        10,1,0,0,341,342,3,16,8,0,342,343,3,70,35,0,343,345,1,0,0,0,344,
        340,1,0,0,0,345,348,1,0,0,0,346,344,1,0,0,0,346,347,1,0,0,0,347,
        73,1,0,0,0,348,346,1,0,0,0,349,350,3,12,6,0,350,351,3,58,29,0,351,
        352,3,72,36,0,352,75,1,0,0,0,353,357,3,22,11,0,354,357,3,18,9,0,
        355,357,5,44,0,0,356,353,1,0,0,0,356,354,1,0,0,0,356,355,1,0,0,0,
        357,77,1,0,0,0,358,366,3,84,42,0,359,366,3,86,43,0,360,366,3,90,
        45,0,361,366,3,88,44,0,362,366,3,96,48,0,363,366,3,100,50,0,364,
        366,3,102,51,0,365,358,1,0,0,0,365,359,1,0,0,0,365,360,1,0,0,0,365,
        361,1,0,0,0,365,362,1,0,0,0,365,363,1,0,0,0,365,364,1,0,0,0,366,
        79,1,0,0,0,367,368,6,40,-1,0,368,369,3,78,39,0,369,374,1,0,0,0,370,
        371,10,1,0,0,371,373,3,78,39,0,372,370,1,0,0,0,373,376,1,0,0,0,374,
        372,1,0,0,0,374,375,1,0,0,0,375,81,1,0,0,0,376,374,1,0,0,0,377,378,
        6,41,-1,0,378,379,5,42,0,0,379,384,1,0,0,0,380,381,10,1,0,0,381,
        383,5,42,0,0,382,380,1,0,0,0,383,386,1,0,0,0,384,382,1,0,0,0,384,
        385,1,0,0,0,385,83,1,0,0,0,386,384,1,0,0,0,387,388,5,30,0,0,388,
        389,3,82,41,0,389,390,3,76,38,0,390,85,1,0,0,0,391,392,5,32,0,0,
        392,393,3,82,41,0,393,394,3,76,38,0,394,87,1,0,0,0,395,400,3,76,
        38,0,396,397,3,72,36,0,397,398,3,76,38,0,398,400,1,0,0,0,399,395,
        1,0,0,0,399,396,1,0,0,0,400,89,1,0,0,0,401,402,3,74,37,0,402,403,
        3,76,38,0,403,91,1,0,0,0,404,407,3,72,36,0,405,407,3,88,44,0,406,
        404,1,0,0,0,406,405,1,0,0,0,407,93,1,0,0,0,408,409,6,47,-1,0,409,
        410,3,92,46,0,410,415,1,0,0,0,411,412,10,1,0,0,412,414,3,92,46,0,
        413,411,1,0,0,0,414,417,1,0,0,0,415,413,1,0,0,0,415,416,1,0,0,0,
        416,95,1,0,0,0,417,415,1,0,0,0,418,419,5,31,0,0,419,420,3,72,36,
        0,420,421,3,80,40,0,421,422,5,29,0,0,422,423,3,76,38,0,423,449,1,
        0,0,0,424,425,5,31,0,0,425,426,3,72,36,0,426,427,3,80,40,0,427,428,
        5,33,0,0,428,429,3,80,40,0,429,430,5,29,0,0,430,431,3,76,38,0,431,
        449,1,0,0,0,432,433,5,31,0,0,433,434,3,72,36,0,434,435,3,80,40,0,
        435,436,3,98,49,0,436,437,5,29,0,0,437,438,3,76,38,0,438,449,1,0,
        0,0,439,440,5,31,0,0,440,441,3,72,36,0,441,442,3,80,40,0,442,443,
        3,98,49,0,443,444,5,33,0,0,444,445,3,80,40,0,445,446,5,29,0,0,446,
        447,3,76,38,0,447,449,1,0,0,0,448,418,1,0,0,0,448,424,1,0,0,0,448,
        432,1,0,0,0,448,439,1,0,0,0,449,97,1,0,0,0,450,451,6,49,-1,0,451,
        452,5,34,0,0,452,453,3,72,36,0,453,454,3,80,40,0,454,462,1,0,0,0,
        455,456,10,1,0,0,456,457,5,34,0,0,457,458,3,72,36,0,458,459,3,80,
        40,0,459,461,1,0,0,0,460,455,1,0,0,0,461,464,1,0,0,0,462,460,1,0,
        0,0,462,463,1,0,0,0,463,99,1,0,0,0,464,462,1,0,0,0,465,466,5,28,
        0,0,466,467,3,72,36,0,467,468,3,80,40,0,468,469,5,29,0,0,469,470,
        3,76,38,0,470,490,1,0,0,0,471,472,5,27,0,0,472,473,5,42,0,0,473,
        474,3,58,29,0,474,475,3,72,36,0,475,476,3,80,40,0,476,477,5,29,0,
        0,477,478,3,76,38,0,478,490,1,0,0,0,479,480,5,27,0,0,480,481,3,4,
        2,0,481,482,5,42,0,0,482,483,3,58,29,0,483,484,3,72,36,0,484,485,
        3,6,3,0,485,486,3,80,40,0,486,487,5,29,0,0,487,488,3,76,38,0,488,
        490,1,0,0,0,489,465,1,0,0,0,489,471,1,0,0,0,489,479,1,0,0,0,490,
        101,1,0,0,0,491,492,5,24,0,0,492,496,3,76,38,0,493,494,5,25,0,0,
        494,496,3,76,38,0,495,491,1,0,0,0,495,493,1,0,0,0,496,103,1,0,0,
        0,497,504,3,80,40,0,498,499,5,26,0,0,499,500,3,112,56,0,500,501,
        3,76,38,0,501,502,3,80,40,0,502,504,1,0,0,0,503,497,1,0,0,0,503,
        498,1,0,0,0,504,105,1,0,0,0,505,506,6,53,-1,0,506,507,5,42,0,0,507,
        514,1,0,0,0,508,509,10,1,0,0,509,510,3,22,11,0,510,511,5,42,0,0,
        511,513,1,0,0,0,512,508,1,0,0,0,513,516,1,0,0,0,514,512,1,0,0,0,
        514,515,1,0,0,0,515,107,1,0,0,0,516,514,1,0,0,0,517,523,5,42,0,0,
        518,519,3,8,4,0,519,520,3,106,53,0,520,521,3,10,5,0,521,523,1,0,
        0,0,522,517,1,0,0,0,522,518,1,0,0,0,523,109,1,0,0,0,524,535,5,42,
        0,0,525,526,5,42,0,0,526,527,3,4,2,0,527,528,3,6,3,0,528,535,1,0,
        0,0,529,530,5,42,0,0,530,531,3,4,2,0,531,532,3,106,53,0,532,533,
        3,6,3,0,533,535,1,0,0,0,534,524,1,0,0,0,534,525,1,0,0,0,534,529,
        1,0,0,0,535,111,1,0,0,0,536,542,3,110,55,0,537,538,3,108,54,0,538,
        539,3,58,29,0,539,540,3,110,55,0,540,542,1,0,0,0,541,536,1,0,0,0,
        541,537,1,0,0,0,542,113,1,0,0,0,36,115,133,146,152,154,159,174,188,
        193,256,258,272,274,294,296,308,310,322,334,346,356,365,374,384,
        399,406,415,448,462,489,495,503,514,522,534,541
    ]

class matlabParser ( Parser ):

    grammarFileName = "matlab.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "']'", "':'", "';'", 
                     "','", "'+'", "'-'", "'*'", "'/'", "'~'", "'^'", "'&'", 
                     "'|'", "'\\'", "'>'", "'<'", "'='", "'.*'", "'.\\'", 
                     "'./'", "'.^'", "'break'", "'return'", "'function'", 
                     "'for'", "'while'", "'end'", "'global'", "'if'", "'clear'", 
                     "'else'", "'elseif'", "'<='", "'>='", "'=='", "'~='", 
                     "'transpose'", "'.''" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ARRAYMUL", "ARRAYDIV", "ARRAYRDIV", "ARRAYPOW", "BREAK", 
                      "RETURN", "FUNCTION", "FOR", "WHILE", "END", "GLOBAL", 
                      "IF", "CLEAR", "ELSE", "ELSEIF", "LE_OP", "GE_OP", 
                      "EQ_OP", "NE_OP", "TRANSPOSE", "NCTRANSPOSE", "STRING_LITERAL", 
                      "IDENTIFIER", "CONSTANT", "CR", "WS" ]

    RULE_file_ = 0
    RULE_primary_expression = 1
    RULE_open_par = 2
    RULE_close_par = 3
    RULE_open_bracket = 4
    RULE_close_bracket = 5
    RULE_postfix_expression = 6
    RULE_index_expression = 7
    RULE_colon = 8
    RULE_semicolon = 9
    RULE_index_expression_list = 10
    RULE_comma = 11
    RULE_array_expression = 12
    RULE_unary_expression = 13
    RULE_unary_operator = 14
    RULE_op_sum = 15
    RULE_op_sub = 16
    RULE_op_mul = 17
    RULE_op_div = 18
    RULE_op_not = 19
    RULE_op_pow = 20
    RULE_op_and = 21
    RULE_op_or = 22
    RULE_op_doble_backslash = 23
    RULE_op_greater = 24
    RULE_op_less = 25
    RULE_op_greater_equal = 26
    RULE_op_less_equal = 27
    RULE_op_not_equal = 28
    RULE_op_equal = 29
    RULE_multiplicative_expression = 30
    RULE_additive_expression = 31
    RULE_relational_expression = 32
    RULE_equality_expression = 33
    RULE_and_expression = 34
    RULE_or_expression = 35
    RULE_expression = 36
    RULE_assignment_expression = 37
    RULE_eostmt = 38
    RULE_statement = 39
    RULE_statement_list = 40
    RULE_identifier_list = 41
    RULE_global_statement = 42
    RULE_clear_statement = 43
    RULE_expression_statement = 44
    RULE_assignment_statement = 45
    RULE_array_element = 46
    RULE_array_list = 47
    RULE_selection_statement = 48
    RULE_elseif_clause = 49
    RULE_iteration_statement = 50
    RULE_jump_statement = 51
    RULE_translation_unit = 52
    RULE_func_ident_list = 53
    RULE_func_return_list = 54
    RULE_function_declare_lhs = 55
    RULE_function_declare = 56

    ruleNames =  [ "file_", "primary_expression", "open_par", "close_par", 
                   "open_bracket", "close_bracket", "postfix_expression", 
                   "index_expression", "colon", "semicolon", "index_expression_list", 
                   "comma", "array_expression", "unary_expression", "unary_operator", 
                   "op_sum", "op_sub", "op_mul", "op_div", "op_not", "op_pow", 
                   "op_and", "op_or", "op_doble_backslash", "op_greater", 
                   "op_less", "op_greater_equal", "op_less_equal", "op_not_equal", 
                   "op_equal", "multiplicative_expression", "additive_expression", 
                   "relational_expression", "equality_expression", "and_expression", 
                   "or_expression", "expression", "assignment_expression", 
                   "eostmt", "statement", "statement_list", "identifier_list", 
                   "global_statement", "clear_statement", "expression_statement", 
                   "assignment_statement", "array_element", "array_list", 
                   "selection_statement", "elseif_clause", "iteration_statement", 
                   "jump_statement", "translation_unit", "func_ident_list", 
                   "func_return_list", "function_declare_lhs", "function_declare" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    ARRAYMUL=20
    ARRAYDIV=21
    ARRAYRDIV=22
    ARRAYPOW=23
    BREAK=24
    RETURN=25
    FUNCTION=26
    FOR=27
    WHILE=28
    END=29
    GLOBAL=30
    IF=31
    CLEAR=32
    ELSE=33
    ELSEIF=34
    LE_OP=35
    GE_OP=36
    EQ_OP=37
    NE_OP=38
    TRANSPOSE=39
    NCTRANSPOSE=40
    STRING_LITERAL=41
    IDENTIFIER=42
    CONSTANT=43
    CR=44
    WS=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class File_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(matlabParser.EOF, 0)

        def statement_list(self):
            return self.getTypedRuleContext(matlabParser.Statement_listContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_file_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_" ):
                listener.enterFile_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_" ):
                listener.exitFile_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile_" ):
                return visitor.visitFile_(self)
            else:
                return visitor.visitChildren(self)




    def file_(self):

        localctx = matlabParser.File_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32993318015946) != 0):
                self.state = 114
                self.statement_list(0)


            self.state = 117
            self.match(matlabParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(matlabParser.IDENTIFIER, 0)

        def CONSTANT(self):
            return self.getToken(matlabParser.CONSTANT, 0)

        def STRING_LITERAL(self):
            return self.getToken(matlabParser.STRING_LITERAL, 0)

        def open_par(self):
            return self.getTypedRuleContext(matlabParser.Open_parContext,0)


        def expression(self):
            return self.getTypedRuleContext(matlabParser.ExpressionContext,0)


        def close_par(self):
            return self.getTypedRuleContext(matlabParser.Close_parContext,0)


        def open_bracket(self):
            return self.getTypedRuleContext(matlabParser.Open_bracketContext,0)


        def close_bracket(self):
            return self.getTypedRuleContext(matlabParser.Close_bracketContext,0)


        def array_list(self):
            return self.getTypedRuleContext(matlabParser.Array_listContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_primary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression" ):
                listener.enterPrimary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression" ):
                listener.exitPrimary_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expression" ):
                return visitor.visitPrimary_expression(self)
            else:
                return visitor.visitChildren(self)




    def primary_expression(self):

        localctx = matlabParser.Primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_primary_expression)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(matlabParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(matlabParser.CONSTANT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(matlabParser.STRING_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 122
                self.open_par()
                self.state = 123
                self.expression(0)
                self.state = 124
                self.close_par()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 126
                self.open_bracket()
                self.state = 127
                self.close_bracket()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.open_bracket()
                self.state = 130
                self.array_list(0)
                self.state = 131
                self.close_bracket()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Open_parContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_open_par

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpen_par" ):
                listener.enterOpen_par(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpen_par" ):
                listener.exitOpen_par(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpen_par" ):
                return visitor.visitOpen_par(self)
            else:
                return visitor.visitChildren(self)




    def open_par(self):

        localctx = matlabParser.Open_parContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_open_par)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(matlabParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Close_parContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_close_par

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClose_par" ):
                listener.enterClose_par(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClose_par" ):
                listener.exitClose_par(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClose_par" ):
                return visitor.visitClose_par(self)
            else:
                return visitor.visitChildren(self)




    def close_par(self):

        localctx = matlabParser.Close_parContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_close_par)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(matlabParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Open_bracketContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_open_bracket

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpen_bracket" ):
                listener.enterOpen_bracket(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpen_bracket" ):
                listener.exitOpen_bracket(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpen_bracket" ):
                return visitor.visitOpen_bracket(self)
            else:
                return visitor.visitChildren(self)




    def open_bracket(self):

        localctx = matlabParser.Open_bracketContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_open_bracket)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(matlabParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Close_bracketContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_close_bracket

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClose_bracket" ):
                listener.enterClose_bracket(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClose_bracket" ):
                listener.exitClose_bracket(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClose_bracket" ):
                return visitor.visitClose_bracket(self)
            else:
                return visitor.visitChildren(self)




    def close_bracket(self):

        localctx = matlabParser.Close_bracketContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_close_bracket)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(matlabParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Postfix_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expression(self):
            return self.getTypedRuleContext(matlabParser.Primary_expressionContext,0)


        def array_expression(self):
            return self.getTypedRuleContext(matlabParser.Array_expressionContext,0)


        def postfix_expression(self):
            return self.getTypedRuleContext(matlabParser.Postfix_expressionContext,0)


        def TRANSPOSE(self):
            return self.getToken(matlabParser.TRANSPOSE, 0)

        def NCTRANSPOSE(self):
            return self.getToken(matlabParser.NCTRANSPOSE, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_postfix_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix_expression" ):
                listener.enterPostfix_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix_expression" ):
                listener.exitPostfix_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix_expression" ):
                return visitor.visitPostfix_expression(self)
            else:
                return visitor.visitChildren(self)



    def postfix_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.Postfix_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_postfix_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 144
                self.primary_expression()
                pass

            elif la_ == 2:
                self.state = 145
                self.array_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 154
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 152
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = matlabParser.Postfix_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expression)
                        self.state = 148
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 149
                        self.match(matlabParser.TRANSPOSE)
                        pass

                    elif la_ == 2:
                        localctx = matlabParser.Postfix_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expression)
                        self.state = 150
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 151
                        self.match(matlabParser.NCTRANSPOSE)
                        pass

             
                self.state = 156
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Index_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def colon(self):
            return self.getTypedRuleContext(matlabParser.ColonContext,0)


        def expression(self):
            return self.getTypedRuleContext(matlabParser.ExpressionContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_index_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_expression" ):
                listener.enterIndex_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_expression" ):
                listener.exitIndex_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expression" ):
                return visitor.visitIndex_expression(self)
            else:
                return visitor.visitChildren(self)




    def index_expression(self):

        localctx = matlabParser.Index_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_index_expression)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.colon()
                pass
            elif token in [1, 3, 8, 9, 12, 41, 42, 43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.expression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_colon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColon" ):
                listener.enterColon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColon" ):
                listener.exitColon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColon" ):
                return visitor.visitColon(self)
            else:
                return visitor.visitChildren(self)




    def colon(self):

        localctx = matlabParser.ColonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_colon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(matlabParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SemicolonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_semicolon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSemicolon" ):
                listener.enterSemicolon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSemicolon" ):
                listener.exitSemicolon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSemicolon" ):
                return visitor.visitSemicolon(self)
            else:
                return visitor.visitChildren(self)




    def semicolon(self):

        localctx = matlabParser.SemicolonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_semicolon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(matlabParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_expression(self):
            return self.getTypedRuleContext(matlabParser.Index_expressionContext,0)


        def index_expression_list(self):
            return self.getTypedRuleContext(matlabParser.Index_expression_listContext,0)


        def comma(self):
            return self.getTypedRuleContext(matlabParser.CommaContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_index_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_expression_list" ):
                listener.enterIndex_expression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_expression_list" ):
                listener.exitIndex_expression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expression_list" ):
                return visitor.visitIndex_expression_list(self)
            else:
                return visitor.visitChildren(self)



    def index_expression_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.Index_expression_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_index_expression_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.index_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = matlabParser.Index_expression_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expression_list)
                    self.state = 168
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 169
                    self.comma()
                    self.state = 170
                    self.index_expression() 
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CommaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_comma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComma" ):
                listener.enterComma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComma" ):
                listener.exitComma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComma" ):
                return visitor.visitComma(self)
            else:
                return visitor.visitChildren(self)




    def comma(self):

        localctx = matlabParser.CommaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(matlabParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(matlabParser.IDENTIFIER, 0)

        def open_par(self):
            return self.getTypedRuleContext(matlabParser.Open_parContext,0)


        def index_expression_list(self):
            return self.getTypedRuleContext(matlabParser.Index_expression_listContext,0)


        def close_par(self):
            return self.getTypedRuleContext(matlabParser.Close_parContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_array_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_expression" ):
                listener.enterArray_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_expression" ):
                listener.exitArray_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_expression" ):
                return visitor.visitArray_expression(self)
            else:
                return visitor.visitChildren(self)




    def array_expression(self):

        localctx = matlabParser.Array_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(matlabParser.IDENTIFIER)
            self.state = 180
            self.open_par()
            self.state = 181
            self.index_expression_list(0)
            self.state = 182
            self.close_par()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfix_expression(self):
            return self.getTypedRuleContext(matlabParser.Postfix_expressionContext,0)


        def unary_operator(self):
            return self.getTypedRuleContext(matlabParser.Unary_operatorContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_unary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_expression" ):
                listener.enterUnary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_expression" ):
                listener.exitUnary_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expression" ):
                return visitor.visitUnary_expression(self)
            else:
                return visitor.visitChildren(self)




    def unary_expression(self):

        localctx = matlabParser.Unary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_unary_expression)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 41, 42, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.postfix_expression(0)
                pass
            elif token in [8, 9, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.unary_operator()
                self.state = 186
                self.postfix_expression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op_sum(self):
            return self.getTypedRuleContext(matlabParser.Op_sumContext,0)


        def op_sub(self):
            return self.getTypedRuleContext(matlabParser.Op_subContext,0)


        def op_not(self):
            return self.getTypedRuleContext(matlabParser.Op_notContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_unary_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_operator" ):
                listener.enterUnary_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_operator" ):
                listener.exitUnary_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_operator" ):
                return visitor.visitUnary_operator(self)
            else:
                return visitor.visitChildren(self)




    def unary_operator(self):

        localctx = matlabParser.Unary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_unary_operator)
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.op_sum()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.op_sub()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                self.op_not()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_sumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_op_sum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_sum" ):
                listener.enterOp_sum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_sum" ):
                listener.exitOp_sum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_sum" ):
                return visitor.visitOp_sum(self)
            else:
                return visitor.visitChildren(self)




    def op_sum(self):

        localctx = matlabParser.Op_sumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_op_sum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(matlabParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_subContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_op_sub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_sub" ):
                listener.enterOp_sub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_sub" ):
                listener.exitOp_sub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_sub" ):
                return visitor.visitOp_sub(self)
            else:
                return visitor.visitChildren(self)




    def op_sub(self):

        localctx = matlabParser.Op_subContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_op_sub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(matlabParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_mulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_op_mul

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_mul" ):
                listener.enterOp_mul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_mul" ):
                listener.exitOp_mul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_mul" ):
                return visitor.visitOp_mul(self)
            else:
                return visitor.visitChildren(self)




    def op_mul(self):

        localctx = matlabParser.Op_mulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_op_mul)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(matlabParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_divContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_op_div

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_div" ):
                listener.enterOp_div(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_div" ):
                listener.exitOp_div(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_div" ):
                return visitor.visitOp_div(self)
            else:
                return visitor.visitChildren(self)




    def op_div(self):

        localctx = matlabParser.Op_divContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_op_div)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(matlabParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_notContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_op_not

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_not" ):
                listener.enterOp_not(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_not" ):
                listener.exitOp_not(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_not" ):
                return visitor.visitOp_not(self)
            else:
                return visitor.visitChildren(self)




    def op_not(self):

        localctx = matlabParser.Op_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_op_not)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(matlabParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_powContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_op_pow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_pow" ):
                listener.enterOp_pow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_pow" ):
                listener.exitOp_pow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_pow" ):
                return visitor.visitOp_pow(self)
            else:
                return visitor.visitChildren(self)




    def op_pow(self):

        localctx = matlabParser.Op_powContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_op_pow)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(matlabParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_andContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_op_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_and" ):
                listener.enterOp_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_and" ):
                listener.exitOp_and(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_and" ):
                return visitor.visitOp_and(self)
            else:
                return visitor.visitChildren(self)




    def op_and(self):

        localctx = matlabParser.Op_andContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_op_and)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(matlabParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_op_or

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_or" ):
                listener.enterOp_or(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_or" ):
                listener.exitOp_or(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_or" ):
                return visitor.visitOp_or(self)
            else:
                return visitor.visitChildren(self)




    def op_or(self):

        localctx = matlabParser.Op_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_op_or)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(matlabParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_doble_backslashContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_op_doble_backslash

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_doble_backslash" ):
                listener.enterOp_doble_backslash(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_doble_backslash" ):
                listener.exitOp_doble_backslash(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_doble_backslash" ):
                return visitor.visitOp_doble_backslash(self)
            else:
                return visitor.visitChildren(self)




    def op_doble_backslash(self):

        localctx = matlabParser.Op_doble_backslashContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_op_doble_backslash)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(matlabParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_greaterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_op_greater

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_greater" ):
                listener.enterOp_greater(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_greater" ):
                listener.exitOp_greater(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_greater" ):
                return visitor.visitOp_greater(self)
            else:
                return visitor.visitChildren(self)




    def op_greater(self):

        localctx = matlabParser.Op_greaterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_op_greater)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(matlabParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_lessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_op_less

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_less" ):
                listener.enterOp_less(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_less" ):
                listener.exitOp_less(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_less" ):
                return visitor.visitOp_less(self)
            else:
                return visitor.visitChildren(self)




    def op_less(self):

        localctx = matlabParser.Op_lessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_op_less)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(matlabParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_greater_equalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GE_OP(self):
            return self.getToken(matlabParser.GE_OP, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_op_greater_equal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_greater_equal" ):
                listener.enterOp_greater_equal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_greater_equal" ):
                listener.exitOp_greater_equal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_greater_equal" ):
                return visitor.visitOp_greater_equal(self)
            else:
                return visitor.visitChildren(self)




    def op_greater_equal(self):

        localctx = matlabParser.Op_greater_equalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_op_greater_equal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(matlabParser.GE_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_less_equalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LE_OP(self):
            return self.getToken(matlabParser.LE_OP, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_op_less_equal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_less_equal" ):
                listener.enterOp_less_equal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_less_equal" ):
                listener.exitOp_less_equal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_less_equal" ):
                return visitor.visitOp_less_equal(self)
            else:
                return visitor.visitChildren(self)




    def op_less_equal(self):

        localctx = matlabParser.Op_less_equalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_op_less_equal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(matlabParser.LE_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_not_equalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NE_OP(self):
            return self.getToken(matlabParser.NE_OP, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_op_not_equal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_not_equal" ):
                listener.enterOp_not_equal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_not_equal" ):
                listener.exitOp_not_equal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_not_equal" ):
                return visitor.visitOp_not_equal(self)
            else:
                return visitor.visitChildren(self)




    def op_not_equal(self):

        localctx = matlabParser.Op_not_equalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_op_not_equal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(matlabParser.NE_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_equalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return matlabParser.RULE_op_equal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_equal" ):
                listener.enterOp_equal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_equal" ):
                listener.exitOp_equal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_equal" ):
                return visitor.visitOp_equal(self)
            else:
                return visitor.visitChildren(self)




    def op_equal(self):

        localctx = matlabParser.Op_equalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_op_equal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(matlabParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplicative_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_expression(self):
            return self.getTypedRuleContext(matlabParser.Unary_expressionContext,0)


        def multiplicative_expression(self):
            return self.getTypedRuleContext(matlabParser.Multiplicative_expressionContext,0)


        def op_mul(self):
            return self.getTypedRuleContext(matlabParser.Op_mulContext,0)


        def op_div(self):
            return self.getTypedRuleContext(matlabParser.Op_divContext,0)


        def op_doble_backslash(self):
            return self.getTypedRuleContext(matlabParser.Op_doble_backslashContext,0)


        def op_pow(self):
            return self.getTypedRuleContext(matlabParser.Op_powContext,0)


        def ARRAYMUL(self):
            return self.getToken(matlabParser.ARRAYMUL, 0)

        def ARRAYDIV(self):
            return self.getToken(matlabParser.ARRAYDIV, 0)

        def ARRAYRDIV(self):
            return self.getToken(matlabParser.ARRAYRDIV, 0)

        def ARRAYPOW(self):
            return self.getToken(matlabParser.ARRAYPOW, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_multiplicative_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative_expression" ):
                listener.enterMultiplicative_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative_expression" ):
                listener.exitMultiplicative_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative_expression" ):
                return visitor.visitMultiplicative_expression(self)
            else:
                return visitor.visitChildren(self)



    def multiplicative_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.Multiplicative_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_multiplicative_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.unary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 256
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = matlabParser.Multiplicative_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expression)
                        self.state = 228
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 229
                        self.op_mul()
                        self.state = 230
                        self.unary_expression()
                        pass

                    elif la_ == 2:
                        localctx = matlabParser.Multiplicative_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expression)
                        self.state = 232
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 233
                        self.op_div()
                        self.state = 234
                        self.unary_expression()
                        pass

                    elif la_ == 3:
                        localctx = matlabParser.Multiplicative_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expression)
                        self.state = 236
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 237
                        self.op_doble_backslash()
                        self.state = 238
                        self.unary_expression()
                        pass

                    elif la_ == 4:
                        localctx = matlabParser.Multiplicative_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expression)
                        self.state = 240
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 241
                        self.op_pow()
                        self.state = 242
                        self.unary_expression()
                        pass

                    elif la_ == 5:
                        localctx = matlabParser.Multiplicative_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expression)
                        self.state = 244
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 245
                        self.match(matlabParser.ARRAYMUL)
                        self.state = 246
                        self.unary_expression()
                        pass

                    elif la_ == 6:
                        localctx = matlabParser.Multiplicative_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expression)
                        self.state = 247
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 248
                        self.match(matlabParser.ARRAYDIV)
                        self.state = 249
                        self.unary_expression()
                        pass

                    elif la_ == 7:
                        localctx = matlabParser.Multiplicative_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expression)
                        self.state = 250
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 251
                        self.match(matlabParser.ARRAYRDIV)
                        self.state = 252
                        self.unary_expression()
                        pass

                    elif la_ == 8:
                        localctx = matlabParser.Multiplicative_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expression)
                        self.state = 253
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 254
                        self.match(matlabParser.ARRAYPOW)
                        self.state = 255
                        self.unary_expression()
                        pass

             
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Additive_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative_expression(self):
            return self.getTypedRuleContext(matlabParser.Multiplicative_expressionContext,0)


        def additive_expression(self):
            return self.getTypedRuleContext(matlabParser.Additive_expressionContext,0)


        def op_sum(self):
            return self.getTypedRuleContext(matlabParser.Op_sumContext,0)


        def op_sub(self):
            return self.getTypedRuleContext(matlabParser.Op_subContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_additive_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive_expression" ):
                listener.enterAdditive_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive_expression" ):
                listener.exitAdditive_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive_expression" ):
                return visitor.visitAdditive_expression(self)
            else:
                return visitor.visitChildren(self)



    def additive_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.Additive_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_additive_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.multiplicative_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 272
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = matlabParser.Additive_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_expression)
                        self.state = 264
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 265
                        self.op_sum()
                        self.state = 266
                        self.multiplicative_expression(0)
                        pass

                    elif la_ == 2:
                        localctx = matlabParser.Additive_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_expression)
                        self.state = 268
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 269
                        self.op_sub()
                        self.state = 270
                        self.multiplicative_expression(0)
                        pass

             
                self.state = 276
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Relational_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_expression(self):
            return self.getTypedRuleContext(matlabParser.Additive_expressionContext,0)


        def relational_expression(self):
            return self.getTypedRuleContext(matlabParser.Relational_expressionContext,0)


        def op_less(self):
            return self.getTypedRuleContext(matlabParser.Op_lessContext,0)


        def op_greater(self):
            return self.getTypedRuleContext(matlabParser.Op_greaterContext,0)


        def LE_OP(self):
            return self.getToken(matlabParser.LE_OP, 0)

        def GE_OP(self):
            return self.getToken(matlabParser.GE_OP, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_relational_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_expression" ):
                listener.enterRelational_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_expression" ):
                listener.exitRelational_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expression" ):
                return visitor.visitRelational_expression(self)
            else:
                return visitor.visitChildren(self)



    def relational_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.Relational_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_relational_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.additive_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 294
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = matlabParser.Relational_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expression)
                        self.state = 280
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 281
                        self.op_less()
                        self.state = 282
                        self.additive_expression(0)
                        pass

                    elif la_ == 2:
                        localctx = matlabParser.Relational_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expression)
                        self.state = 284
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 285
                        self.op_greater()
                        self.state = 286
                        self.additive_expression(0)
                        pass

                    elif la_ == 3:
                        localctx = matlabParser.Relational_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expression)
                        self.state = 288
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 289
                        self.match(matlabParser.LE_OP)
                        self.state = 290
                        self.additive_expression(0)
                        pass

                    elif la_ == 4:
                        localctx = matlabParser.Relational_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relational_expression)
                        self.state = 291
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 292
                        self.match(matlabParser.GE_OP)
                        self.state = 293
                        self.additive_expression(0)
                        pass

             
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Equality_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expression(self):
            return self.getTypedRuleContext(matlabParser.Relational_expressionContext,0)


        def equality_expression(self):
            return self.getTypedRuleContext(matlabParser.Equality_expressionContext,0)


        def EQ_OP(self):
            return self.getToken(matlabParser.EQ_OP, 0)

        def NE_OP(self):
            return self.getToken(matlabParser.NE_OP, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_equality_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality_expression" ):
                listener.enterEquality_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality_expression" ):
                listener.exitEquality_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality_expression" ):
                return visitor.visitEquality_expression(self)
            else:
                return visitor.visitChildren(self)



    def equality_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.Equality_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_equality_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.relational_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 310
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 308
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = matlabParser.Equality_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equality_expression)
                        self.state = 302
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 303
                        self.match(matlabParser.EQ_OP)
                        self.state = 304
                        self.relational_expression(0)
                        pass

                    elif la_ == 2:
                        localctx = matlabParser.Equality_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equality_expression)
                        self.state = 305
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 306
                        self.match(matlabParser.NE_OP)
                        self.state = 307
                        self.relational_expression(0)
                        pass

             
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class And_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality_expression(self):
            return self.getTypedRuleContext(matlabParser.Equality_expressionContext,0)


        def and_expression(self):
            return self.getTypedRuleContext(matlabParser.And_expressionContext,0)


        def op_and(self):
            return self.getTypedRuleContext(matlabParser.Op_andContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_and_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_expression" ):
                listener.enterAnd_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_expression" ):
                listener.exitAnd_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_expression" ):
                return visitor.visitAnd_expression(self)
            else:
                return visitor.visitChildren(self)



    def and_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.And_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_and_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.equality_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 322
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = matlabParser.And_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_and_expression)
                    self.state = 316
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 317
                    self.op_and()
                    self.state = 318
                    self.equality_expression(0) 
                self.state = 324
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Or_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_expression(self):
            return self.getTypedRuleContext(matlabParser.And_expressionContext,0)


        def or_expression(self):
            return self.getTypedRuleContext(matlabParser.Or_expressionContext,0)


        def op_or(self):
            return self.getTypedRuleContext(matlabParser.Op_orContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_or_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_expression" ):
                listener.enterOr_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_expression" ):
                listener.exitOr_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr_expression" ):
                return visitor.visitOr_expression(self)
            else:
                return visitor.visitChildren(self)



    def or_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.Or_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_or_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.and_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = matlabParser.Or_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_or_expression)
                    self.state = 328
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 329
                    self.op_or()
                    self.state = 330
                    self.and_expression(0) 
                self.state = 336
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_expression(self):
            return self.getTypedRuleContext(matlabParser.Or_expressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(matlabParser.ExpressionContext,0)


        def colon(self):
            return self.getTypedRuleContext(matlabParser.ColonContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.or_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 346
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = matlabParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 340
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 341
                    self.colon()
                    self.state = 342
                    self.or_expression(0) 
                self.state = 348
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Assignment_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfix_expression(self):
            return self.getTypedRuleContext(matlabParser.Postfix_expressionContext,0)


        def op_equal(self):
            return self.getTypedRuleContext(matlabParser.Op_equalContext,0)


        def expression(self):
            return self.getTypedRuleContext(matlabParser.ExpressionContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_assignment_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_expression" ):
                listener.enterAssignment_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_expression" ):
                listener.exitAssignment_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_expression" ):
                return visitor.visitAssignment_expression(self)
            else:
                return visitor.visitChildren(self)




    def assignment_expression(self):

        localctx = matlabParser.Assignment_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assignment_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.postfix_expression(0)
            self.state = 350
            self.op_equal()
            self.state = 351
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EostmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comma(self):
            return self.getTypedRuleContext(matlabParser.CommaContext,0)


        def semicolon(self):
            return self.getTypedRuleContext(matlabParser.SemicolonContext,0)


        def CR(self):
            return self.getToken(matlabParser.CR, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_eostmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEostmt" ):
                listener.enterEostmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEostmt" ):
                listener.exitEostmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEostmt" ):
                return visitor.visitEostmt(self)
            else:
                return visitor.visitChildren(self)




    def eostmt(self):

        localctx = matlabParser.EostmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_eostmt)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.comma()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.semicolon()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 355
                self.match(matlabParser.CR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def global_statement(self):
            return self.getTypedRuleContext(matlabParser.Global_statementContext,0)


        def clear_statement(self):
            return self.getTypedRuleContext(matlabParser.Clear_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(matlabParser.Assignment_statementContext,0)


        def expression_statement(self):
            return self.getTypedRuleContext(matlabParser.Expression_statementContext,0)


        def selection_statement(self):
            return self.getTypedRuleContext(matlabParser.Selection_statementContext,0)


        def iteration_statement(self):
            return self.getTypedRuleContext(matlabParser.Iteration_statementContext,0)


        def jump_statement(self):
            return self.getTypedRuleContext(matlabParser.Jump_statementContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = matlabParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_statement)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.global_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.clear_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 360
                self.assignment_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 361
                self.expression_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 362
                self.selection_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 363
                self.iteration_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 364
                self.jump_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(matlabParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(matlabParser.Statement_listContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_statement_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_list" ):
                listener.enterStatement_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_list" ):
                listener.exitStatement_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)



    def statement_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.Statement_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_statement_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = matlabParser.Statement_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement_list)
                    self.state = 370
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 371
                    self.statement() 
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(matlabParser.IDENTIFIER, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(matlabParser.Identifier_listContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_identifier_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier_list" ):
                listener.enterIdentifier_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier_list" ):
                listener.exitIdentifier_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier_list" ):
                return visitor.visitIdentifier_list(self)
            else:
                return visitor.visitChildren(self)



    def identifier_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.Identifier_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_identifier_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(matlabParser.IDENTIFIER)
            self._ctx.stop = self._input.LT(-1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = matlabParser.Identifier_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_identifier_list)
                    self.state = 380
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 381
                    self.match(matlabParser.IDENTIFIER) 
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Global_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GLOBAL(self):
            return self.getToken(matlabParser.GLOBAL, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(matlabParser.Identifier_listContext,0)


        def eostmt(self):
            return self.getTypedRuleContext(matlabParser.EostmtContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_global_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_statement" ):
                listener.enterGlobal_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_statement" ):
                listener.exitGlobal_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal_statement" ):
                return visitor.visitGlobal_statement(self)
            else:
                return visitor.visitChildren(self)




    def global_statement(self):

        localctx = matlabParser.Global_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_global_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(matlabParser.GLOBAL)
            self.state = 388
            self.identifier_list(0)
            self.state = 389
            self.eostmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Clear_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLEAR(self):
            return self.getToken(matlabParser.CLEAR, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(matlabParser.Identifier_listContext,0)


        def eostmt(self):
            return self.getTypedRuleContext(matlabParser.EostmtContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_clear_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClear_statement" ):
                listener.enterClear_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClear_statement" ):
                listener.exitClear_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClear_statement" ):
                return visitor.visitClear_statement(self)
            else:
                return visitor.visitChildren(self)




    def clear_statement(self):

        localctx = matlabParser.Clear_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_clear_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(matlabParser.CLEAR)
            self.state = 392
            self.identifier_list(0)
            self.state = 393
            self.eostmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eostmt(self):
            return self.getTypedRuleContext(matlabParser.EostmtContext,0)


        def expression(self):
            return self.getTypedRuleContext(matlabParser.ExpressionContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_expression_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_statement" ):
                listener.enterExpression_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_statement" ):
                listener.exitExpression_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_statement" ):
                return visitor.visitExpression_statement(self)
            else:
                return visitor.visitChildren(self)




    def expression_statement(self):

        localctx = matlabParser.Expression_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expression_statement)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.eostmt()
                pass
            elif token in [1, 3, 8, 9, 12, 41, 42, 43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.expression(0)
                self.state = 397
                self.eostmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_expression(self):
            return self.getTypedRuleContext(matlabParser.Assignment_expressionContext,0)


        def eostmt(self):
            return self.getTypedRuleContext(matlabParser.EostmtContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_assignment_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_statement" ):
                listener.enterAssignment_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_statement" ):
                listener.exitAssignment_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = matlabParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.assignment_expression()
            self.state = 402
            self.eostmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(matlabParser.ExpressionContext,0)


        def expression_statement(self):
            return self.getTypedRuleContext(matlabParser.Expression_statementContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_array_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_element" ):
                listener.enterArray_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_element" ):
                listener.exitArray_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = matlabParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_array_element)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.expression_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(matlabParser.Array_elementContext,0)


        def array_list(self):
            return self.getTypedRuleContext(matlabParser.Array_listContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_array_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_list" ):
                listener.enterArray_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_list" ):
                listener.exitArray_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)



    def array_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.Array_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_array_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.array_element()
            self._ctx.stop = self._input.LT(-1)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = matlabParser.Array_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_array_list)
                    self.state = 411
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 412
                    self.array_element() 
                self.state = 417
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Selection_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(matlabParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(matlabParser.ExpressionContext,0)


        def statement_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matlabParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(matlabParser.Statement_listContext,i)


        def END(self):
            return self.getToken(matlabParser.END, 0)

        def eostmt(self):
            return self.getTypedRuleContext(matlabParser.EostmtContext,0)


        def ELSE(self):
            return self.getToken(matlabParser.ELSE, 0)

        def elseif_clause(self):
            return self.getTypedRuleContext(matlabParser.Elseif_clauseContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_selection_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelection_statement" ):
                listener.enterSelection_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelection_statement" ):
                listener.exitSelection_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelection_statement" ):
                return visitor.visitSelection_statement(self)
            else:
                return visitor.visitChildren(self)




    def selection_statement(self):

        localctx = matlabParser.Selection_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_selection_statement)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(matlabParser.IF)
                self.state = 419
                self.expression(0)
                self.state = 420
                self.statement_list(0)
                self.state = 421
                self.match(matlabParser.END)
                self.state = 422
                self.eostmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.match(matlabParser.IF)
                self.state = 425
                self.expression(0)
                self.state = 426
                self.statement_list(0)
                self.state = 427
                self.match(matlabParser.ELSE)
                self.state = 428
                self.statement_list(0)
                self.state = 429
                self.match(matlabParser.END)
                self.state = 430
                self.eostmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 432
                self.match(matlabParser.IF)
                self.state = 433
                self.expression(0)
                self.state = 434
                self.statement_list(0)
                self.state = 435
                self.elseif_clause(0)
                self.state = 436
                self.match(matlabParser.END)
                self.state = 437
                self.eostmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 439
                self.match(matlabParser.IF)
                self.state = 440
                self.expression(0)
                self.state = 441
                self.statement_list(0)
                self.state = 442
                self.elseif_clause(0)
                self.state = 443
                self.match(matlabParser.ELSE)
                self.state = 444
                self.statement_list(0)
                self.state = 445
                self.match(matlabParser.END)
                self.state = 446
                self.eostmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(matlabParser.ELSEIF, 0)

        def expression(self):
            return self.getTypedRuleContext(matlabParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(matlabParser.Statement_listContext,0)


        def elseif_clause(self):
            return self.getTypedRuleContext(matlabParser.Elseif_clauseContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_elseif_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseif_clause" ):
                listener.enterElseif_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseif_clause" ):
                listener.exitElseif_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_clause" ):
                return visitor.visitElseif_clause(self)
            else:
                return visitor.visitChildren(self)



    def elseif_clause(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.Elseif_clauseContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_elseif_clause, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(matlabParser.ELSEIF)
            self.state = 452
            self.expression(0)
            self.state = 453
            self.statement_list(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = matlabParser.Elseif_clauseContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_elseif_clause)
                    self.state = 455
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 456
                    self.match(matlabParser.ELSEIF)
                    self.state = 457
                    self.expression(0)
                    self.state = 458
                    self.statement_list(0) 
                self.state = 464
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Iteration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(matlabParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(matlabParser.ExpressionContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(matlabParser.Statement_listContext,0)


        def END(self):
            return self.getToken(matlabParser.END, 0)

        def eostmt(self):
            return self.getTypedRuleContext(matlabParser.EostmtContext,0)


        def FOR(self):
            return self.getToken(matlabParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(matlabParser.IDENTIFIER, 0)

        def op_equal(self):
            return self.getTypedRuleContext(matlabParser.Op_equalContext,0)


        def open_par(self):
            return self.getTypedRuleContext(matlabParser.Open_parContext,0)


        def close_par(self):
            return self.getTypedRuleContext(matlabParser.Close_parContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_iteration_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIteration_statement" ):
                listener.enterIteration_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIteration_statement" ):
                listener.exitIteration_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIteration_statement" ):
                return visitor.visitIteration_statement(self)
            else:
                return visitor.visitChildren(self)




    def iteration_statement(self):

        localctx = matlabParser.Iteration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_iteration_statement)
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.match(matlabParser.WHILE)
                self.state = 466
                self.expression(0)
                self.state = 467
                self.statement_list(0)
                self.state = 468
                self.match(matlabParser.END)
                self.state = 469
                self.eostmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
                self.match(matlabParser.FOR)
                self.state = 472
                self.match(matlabParser.IDENTIFIER)
                self.state = 473
                self.op_equal()
                self.state = 474
                self.expression(0)
                self.state = 475
                self.statement_list(0)
                self.state = 476
                self.match(matlabParser.END)
                self.state = 477
                self.eostmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 479
                self.match(matlabParser.FOR)
                self.state = 480
                self.open_par()
                self.state = 481
                self.match(matlabParser.IDENTIFIER)
                self.state = 482
                self.op_equal()
                self.state = 483
                self.expression(0)
                self.state = 484
                self.close_par()
                self.state = 485
                self.statement_list(0)
                self.state = 486
                self.match(matlabParser.END)
                self.state = 487
                self.eostmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Jump_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(matlabParser.BREAK, 0)

        def eostmt(self):
            return self.getTypedRuleContext(matlabParser.EostmtContext,0)


        def RETURN(self):
            return self.getToken(matlabParser.RETURN, 0)

        def getRuleIndex(self):
            return matlabParser.RULE_jump_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJump_statement" ):
                listener.enterJump_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJump_statement" ):
                listener.exitJump_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJump_statement" ):
                return visitor.visitJump_statement(self)
            else:
                return visitor.visitChildren(self)




    def jump_statement(self):

        localctx = matlabParser.Jump_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_jump_statement)
        try:
            self.state = 495
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.match(matlabParser.BREAK)
                self.state = 492
                self.eostmt()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.match(matlabParser.RETURN)
                self.state = 494
                self.eostmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Translation_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_list(self):
            return self.getTypedRuleContext(matlabParser.Statement_listContext,0)


        def FUNCTION(self):
            return self.getToken(matlabParser.FUNCTION, 0)

        def function_declare(self):
            return self.getTypedRuleContext(matlabParser.Function_declareContext,0)


        def eostmt(self):
            return self.getTypedRuleContext(matlabParser.EostmtContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_translation_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTranslation_unit" ):
                listener.enterTranslation_unit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTranslation_unit" ):
                listener.exitTranslation_unit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTranslation_unit" ):
                return visitor.visitTranslation_unit(self)
            else:
                return visitor.visitChildren(self)




    def translation_unit(self):

        localctx = matlabParser.Translation_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_translation_unit)
        try:
            self.state = 503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 6, 7, 8, 9, 12, 24, 25, 27, 28, 30, 31, 32, 41, 42, 43, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.statement_list(0)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
                self.match(matlabParser.FUNCTION)
                self.state = 499
                self.function_declare()
                self.state = 500
                self.eostmt()
                self.state = 501
                self.statement_list(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_ident_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(matlabParser.IDENTIFIER, 0)

        def func_ident_list(self):
            return self.getTypedRuleContext(matlabParser.Func_ident_listContext,0)


        def comma(self):
            return self.getTypedRuleContext(matlabParser.CommaContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_func_ident_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_ident_list" ):
                listener.enterFunc_ident_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_ident_list" ):
                listener.exitFunc_ident_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_ident_list" ):
                return visitor.visitFunc_ident_list(self)
            else:
                return visitor.visitChildren(self)



    def func_ident_list(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = matlabParser.Func_ident_listContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_func_ident_list, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(matlabParser.IDENTIFIER)
            self._ctx.stop = self._input.LT(-1)
            self.state = 514
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = matlabParser.Func_ident_listContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_func_ident_list)
                    self.state = 508
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 509
                    self.comma()
                    self.state = 510
                    self.match(matlabParser.IDENTIFIER) 
                self.state = 516
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Func_return_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(matlabParser.IDENTIFIER, 0)

        def open_bracket(self):
            return self.getTypedRuleContext(matlabParser.Open_bracketContext,0)


        def func_ident_list(self):
            return self.getTypedRuleContext(matlabParser.Func_ident_listContext,0)


        def close_bracket(self):
            return self.getTypedRuleContext(matlabParser.Close_bracketContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_func_return_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_return_list" ):
                listener.enterFunc_return_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_return_list" ):
                listener.exitFunc_return_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_return_list" ):
                return visitor.visitFunc_return_list(self)
            else:
                return visitor.visitChildren(self)




    def func_return_list(self):

        localctx = matlabParser.Func_return_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_func_return_list)
        try:
            self.state = 522
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 517
                self.match(matlabParser.IDENTIFIER)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 518
                self.open_bracket()
                self.state = 519
                self.func_ident_list(0)
                self.state = 520
                self.close_bracket()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declare_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(matlabParser.IDENTIFIER, 0)

        def open_par(self):
            return self.getTypedRuleContext(matlabParser.Open_parContext,0)


        def close_par(self):
            return self.getTypedRuleContext(matlabParser.Close_parContext,0)


        def func_ident_list(self):
            return self.getTypedRuleContext(matlabParser.Func_ident_listContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_function_declare_lhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declare_lhs" ):
                listener.enterFunction_declare_lhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declare_lhs" ):
                listener.exitFunction_declare_lhs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declare_lhs" ):
                return visitor.visitFunction_declare_lhs(self)
            else:
                return visitor.visitChildren(self)




    def function_declare_lhs(self):

        localctx = matlabParser.Function_declare_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_function_declare_lhs)
        try:
            self.state = 534
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.match(matlabParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
                self.match(matlabParser.IDENTIFIER)
                self.state = 526
                self.open_par()
                self.state = 527
                self.close_par()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 529
                self.match(matlabParser.IDENTIFIER)
                self.state = 530
                self.open_par()
                self.state = 531
                self.func_ident_list(0)
                self.state = 532
                self.close_par()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_declare_lhs(self):
            return self.getTypedRuleContext(matlabParser.Function_declare_lhsContext,0)


        def func_return_list(self):
            return self.getTypedRuleContext(matlabParser.Func_return_listContext,0)


        def op_equal(self):
            return self.getTypedRuleContext(matlabParser.Op_equalContext,0)


        def getRuleIndex(self):
            return matlabParser.RULE_function_declare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declare" ):
                listener.enterFunction_declare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declare" ):
                listener.exitFunction_declare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declare" ):
                return visitor.visitFunction_declare(self)
            else:
                return visitor.visitChildren(self)




    def function_declare(self):

        localctx = matlabParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_function_declare)
        try:
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 536
                self.function_declare_lhs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 537
                self.func_return_list()
                self.state = 538
                self.op_equal()
                self.state = 539
                self.function_declare_lhs()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.postfix_expression_sempred
        self._predicates[10] = self.index_expression_list_sempred
        self._predicates[30] = self.multiplicative_expression_sempred
        self._predicates[31] = self.additive_expression_sempred
        self._predicates[32] = self.relational_expression_sempred
        self._predicates[33] = self.equality_expression_sempred
        self._predicates[34] = self.and_expression_sempred
        self._predicates[35] = self.or_expression_sempred
        self._predicates[36] = self.expression_sempred
        self._predicates[40] = self.statement_list_sempred
        self._predicates[41] = self.identifier_list_sempred
        self._predicates[47] = self.array_list_sempred
        self._predicates[49] = self.elseif_clause_sempred
        self._predicates[53] = self.func_ident_list_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def postfix_expression_sempred(self, localctx:Postfix_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def index_expression_list_sempred(self, localctx:Index_expression_listContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def multiplicative_expression_sempred(self, localctx:Multiplicative_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 1)
         

    def additive_expression_sempred(self, localctx:Additive_expressionContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 1)
         

    def relational_expression_sempred(self, localctx:Relational_expressionContext, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 1)
         

    def equality_expression_sempred(self, localctx:Equality_expressionContext, predIndex:int):
            if predIndex == 17:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 1)
         

    def and_expression_sempred(self, localctx:And_expressionContext, predIndex:int):
            if predIndex == 19:
                return self.precpred(self._ctx, 1)
         

    def or_expression_sempred(self, localctx:Or_expressionContext, predIndex:int):
            if predIndex == 20:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 21:
                return self.precpred(self._ctx, 1)
         

    def statement_list_sempred(self, localctx:Statement_listContext, predIndex:int):
            if predIndex == 22:
                return self.precpred(self._ctx, 1)
         

    def identifier_list_sempred(self, localctx:Identifier_listContext, predIndex:int):
            if predIndex == 23:
                return self.precpred(self._ctx, 1)
         

    def array_list_sempred(self, localctx:Array_listContext, predIndex:int):
            if predIndex == 24:
                return self.precpred(self._ctx, 1)
         

    def elseif_clause_sempred(self, localctx:Elseif_clauseContext, predIndex:int):
            if predIndex == 25:
                return self.precpred(self._ctx, 1)
         

    def func_ident_list_sempred(self, localctx:Func_ident_listContext, predIndex:int):
            if predIndex == 26:
                return self.precpred(self._ctx, 1)
         




