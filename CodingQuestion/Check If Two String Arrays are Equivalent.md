Problem Description: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
![image](https://user-images.githubusercontent.com/11685096/154831724-f6736d96-411a-4aad-90b8-787f1af5a9c0.png)

```python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Solution 1
        # return "".join(word1) == "".join(word2)
        
        # Solution 2
        str_of_word1 = ""
        str_of_word2 = ""
        for each in word1:
            str_of_word1 += each
        for each in word2:
            str_of_word2 += each
        return str_of_word1 == str_of_word2
```
