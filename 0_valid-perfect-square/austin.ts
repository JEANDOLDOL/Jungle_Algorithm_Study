function isPerfectSquare(num: number): boolean {
    if (num == 1) {
        return true;
    }
    for (let i = 1; i <= num; i++) {
        if (i*i>num) {
            return false;
        }
        if (i*i == num) {
            return true;
        }
    }
};