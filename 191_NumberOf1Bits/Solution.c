int hammingWeight(uint32_t n) {
    int i = 0, t = n, count = 0;
    for ( ; i < 32; i++) {
        if ((t>>i)&0x0001) count++;
        t = n;
    }
    return count;
}
