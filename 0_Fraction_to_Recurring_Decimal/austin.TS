function fractionToDecimal(numerator: number, denominator: number): string {
    if (numerator === 0) return "0";

    let result = "";
    
    // 둘중 하나 음수일때 마이너스 넣어주기
    if ((numerator < 0) !== (denominator < 0)) {
        result += "-";
    }
    
    // 음수 없에기
    let num = Math.abs(numerator);
    let den = Math.abs(denominator);
    
    // 정수 구하기
    let integerPart = Math.floor(num / den);
    result += integerPart.toString();
    
    // 나머지 구하기
    let remainder = num % den;
    if (remainder === 0) {
        return result;  // 소수점 없으면 여기서 반환됨
    }
    
    // 소주점이 있을때
    result += ".";
    
    // 반복되는 나머지 객체 
    const remainderMap: { [key: number]: number } = {}; // 객체의 키 숫자, 키의 밸류 값도 숫자의 탑입 설정
    
    while (remainder !== 0) {
        // 만약 현재 나머지가 remainderMap안에 있다면, ()로 감싸주고 리턴한다. 
        if (remainder in remainderMap) {
            const index = remainderMap[remainder];
            result = result.slice(0, index) + "(" + result.slice(index) + ")";
            return result;
        }
        
        
        remainderMap[remainder] = result.length;
        
        // 반복적으로 나머지 계산
        remainder *= 10;
        const fractionalPart = Math.floor(remainder / den);
        result += fractionalPart.toString();
        
        // 나머지 업데이트
        remainder %= den;
    }
    
    return result;
}

