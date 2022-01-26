Problem Description: https://leetcode.com/problems/detect-capital/
![image](https://user-images.githubusercontent.com/11685096/150978111-51debc99-15d3-454a-97f2-66430cfab565.png)

Solution
```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.lower() or word == word.capitalize()
```
