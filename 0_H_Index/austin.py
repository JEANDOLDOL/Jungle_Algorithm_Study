"""
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

논문 중에서 "h번 이상 인용된 논문이 h편 이상"인 가장 큰 값을 찾아야한다. 
이 말인 뜻은, 인용횟수는 인용된 논문의 수에 제한된다. 그 반대도 마찬가지 이다. 

[11, 15] 둘의 공통된, 인용횟수는 11이지만, 총 두편 밖에 없어, 2번이상 인용된 논문이 2편이상인 것으로 된다. 

"""

class Solution(object):
    def hIndex(self, citations):
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))
        
