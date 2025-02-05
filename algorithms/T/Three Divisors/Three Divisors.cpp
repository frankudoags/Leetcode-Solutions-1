class Solution {
public:
    bool isPrime(int n) {
        for (int i = 2; i <= sqrt(n); i++) if (n % i == 0) return false;
        return true;
    }
    
    bool isThree(int n) {
        return n != 1 && n != 2 && (int)sqrt(n)*sqrt(n) == n && isPrime(sqrt(n));
    }
};
